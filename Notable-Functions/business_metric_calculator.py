# Gross Profit = (Revenue - Cost of Goods Sold)

def gross_profit(revenue, cost_of_goods_sold):
    return revenue - cost_of_goods_sold

# Gross Profit Margin = (Gross Profit / Revenue) * 100

def gross_profit_margin(revenue, cost_of_goods_sold):
    if revenue == 0:
        print('Warning!: Revenue is zero. Gross Profit Margin cannot be calculated.')
        return 0
    gp = gross_profit(revenue, cost_of_goods_sold)
    margin = gp / revenue
    return margin

# Operating Profit = (Gross Profit - Operating Expenses)

def operating_profit(revenue, cost_of_goods_sold, operating_expenses):
    gp = gross_profit(revenue, cost_of_goods_sold)
    return gp - operating_expenses

# Operating Profit Margin = (Operating Profit / Revenue) * 100

def operating_profit_margin(revenue, cost_of_goods_sold, operating_expenses):
    if revenue == 0:
        print('Warning!: Revenue is zero. Operating Profit Margin cannot be calculated.')
        return 0
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
    if investment == 0:
        print('Warning!: Investment is zero. Return on Investment cannot be calculated.')
        return 0
    return (net_profit - investment) / investment

def return_on_investment_full(revenue, cost_of_goods_sold, operating_expenses,
                              taxes_and_loans, investment):
    if investment == 0:
        print('Warning!: Investment is zero. Return on Investment cannot be calculated.')
        return 0
    return return_on_investment(net_profit(revenue, cost_of_goods_sold, 
                                           operating_expenses, taxes_and_loans), investment)

# Conversion = Customers / Visitors

def conversion(customers, visitors):
    return customers / visitors

def calculate_customers_from_conversion(percentage, visitors):
    return (percentage * .01) * visitors

def calculate_visitors_from_conversion(percentage, customers):
    return customers / (percentage * .01)

########## Enter values into variables below ##########

if __name__ == '__main__':

    # update variables below for business metrics
    revenue = 12345
    cost_of_goods_sold = 678
    operating_expenses = 90
    tax_rate = .06
    taxes_and_loans = (revenue * tax_rate) + 1234
    investment = 5678

    print(f'Gross Profit: ${gross_profit(revenue, cost_of_goods_sold)}') 
    print(f'Gross Profit Margin: {gross_profit_margin(revenue, cost_of_goods_sold):.2%}')
    print(f'Operating Profit: ${operating_profit(revenue, cost_of_goods_sold, operating_expenses)}')
    print(f'Operating Profit Margin: {operating_profit_margin(
        revenue, cost_of_goods_sold, operating_expenses):.2%}')
    print(f'Net Profit: ${net_profit(
        revenue, cost_of_goods_sold, operating_expenses, taxes_and_loans)}')
    print(f'Return on Investment: {return_on_investment_full(
        revenue, cost_of_goods_sold, operating_expenses,
                              taxes_and_loans, investment):.2%}')
    
    # update variables below for conversion rate
    visitors = 12345
    customers = 678

    print(f'Conversion Rate: {conversion(customers, visitors):.2%}')

########## Output in terminal ##########