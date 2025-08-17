# Gross Profit = (Revenue - Cost of Goods Sold)

def gross_profit(revenue, cost_of_goods_sold):
    return revenue - cost_of_goods_sold

# Gross Profit Margin = (Gross Profit / Revenue) * 100

def gross_profit_margin(revenue, cost_of_goods_sold):
    gp = gross_profit(revenue, cost_of_goods_sold)
    margin = gp / revenue
    return margin

# Operating Profit = (Gross Profit - Operating Expenses)

def operating_profit(revenue, cost_of_goods_sold, operating_expenses):
    gp = gross_profit(revenue, cost_of_goods_sold)
    return gp - operating_expenses

# Operating Profit Margin = (Operating Profit / Revenue) * 100

def operating_profit_margin(revenue, cost_of_goods_sold, operating_expenses):
    gp = gross_profit(revenue, cost_of_goods_sold)
    op = gp - operating_expenses
    margin = op / revenue
    return margin

# Net Profit = (Operating Profit - Taxes and Loans)

def net_profit(revenue, cost_of_goods_sold, operating_expenses, taxes_and_loans):
    gp = gross_profit(revenue, cost_of_goods_sold)
    op = gp - operating_expenses
    return op - taxes_and_loans

# Return on Investment = (Net Profit - Investment) / Investment

def return_on_investment(net_profit, investment):
    return (net_profit - investment) / investment

def return_on_investment_full(revenue, cost_of_goods_sold, operating_expenses,
                              taxes_and_loans, investment):
    gp = gross_profit(revenue, cost_of_goods_sold)
    op = gp - operating_expenses
    np = op - taxes_and_loans
    return (np - investment) / investment

# Conversion = Customers / Visitors

def conversion(customers, visitors):
    return customers / visitors

def conversion_visitors(percentage, visitors):
    return (percentage * .01) * visitors

def conversion_customers(percentage, customers):
    return customers / (percentage * .01)

########## Pre-coded variables below for easy input ##########

#### GP / GPM / OP / OPM / NP / ROI ####

#revenue = 
#cost_of_goods_sold = 
#operating_expenses = 
#taxes_and_loans = (revenue * .06) +
#net_profit = 
#investment = 

#### Conversion ####

#percentage = 
#customers = 
#visitors = 

########## Copy-Paste as needed for functions ##########

# revenue, cost_of_goods_sold, operating_expenses, taxes_and_loans, net_profit, investment
# percentage, customers, visitors

# print()