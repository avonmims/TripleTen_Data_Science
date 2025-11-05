
import numpy as np
import pandas as pd

import tensorflow as tf

from sklearn.model_selection import train_test_split

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam


def load_train(df_train, path):
    
    """
    It loads the train part of dataset from path
    """

    train_datagen = ImageDataGenerator(rescale=1/255)

    train_gen_flow = train_datagen.flow_from_dataframe(
        dataframe=df_train,
        directory=path + 'final_files',
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        seed=seed_value,
    )

    return train_gen_flow


def load_test(df_test, path):
    
    """
    It loads the validation/test part of dataset from path
    """

    test_datagen = ImageDataGenerator(rescale=1/255)

    test_gen_flow = test_datagen.flow_from_dataframe(
        dataframe=df_test,
        directory=path + 'final_files',
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        seed=seed_value,
    )

    return test_gen_flow


def create_model(input_shape):
    
    """
    It defines the model
    """
    
    backbone = ResNet50(weights='imagenet', 
                        input_shape=input_shape,
                        include_top=False)

    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(1))

    optimizer = Adam(learning_rate=0.0005)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])

    return model


def train_model(model, train_data, test_data, batch_size=None, epochs=20,
                steps_per_epoch=None, validation_steps=None):

    """
    Trains the model given the parameters
    """
    
    if steps_per_epoch is None:
        steps_per_epoch = len(train_data)
        
    if validation_steps is None:
        validation_steps = len(test_data)

    model.fit(train_data, 
              validation_data=test_data,
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=1)

    return model



# ----- imports -----
import random
import os

# ----- reproducibility -----
seed_value = 777
random.seed(seed_value)
np.random.seed(seed_value)
tf.keras.utils.set_random_seed(seed_value)
os.environ['TF_DETERMINISTIC_OPS'] = '1'

# ----- data splitting -----
data_path = 'data/'
full_labels = pd.read_csv(data_path + 'labels.csv')
df_train, df_test = train_test_split(full_labels, test_size=.25, random_state=seed_value)
print(f'Total images: {len(full_labels)}')
print(f'Train images: {len(df_train)} (75%)')
print(f'Test images: {len(df_test)} (25%)')

# ----- load data gen -----
print('Loading data generators..')
train_generator = load_train(df_train, data_path)
test_generator = load_test(df_test, data_path)
print(f'Train batches: {len(train_generator)}, Test batches: {len(test_generator)}')

# ----- model creation -----
input_shape=(224, 224, 3)
print(f'Creating model with {input_shape} input shape..')
model = create_model(input_shape)
print('Model initiation completed.')

# ----- model training -----
print('Training model..')
trained_model = train_model(model, train_generator, test_generator, epochs=20)
print('Traiing finished.')

