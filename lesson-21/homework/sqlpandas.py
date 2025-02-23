import pandas as pd

data_customers = {'CustomerID': [1, 2, 3, 4],
                  'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
                  'Country': ['USA', 'UK', 'Canada', 'Germany']}
customers = pd.DataFrame(data_customers)

data_orders = {'OrderID': [101, 102, 103, 104, 105, 106],
               'CustomerID': [1, 1, 2, 3, 3, 3],
               'OrderDate': ['2025-01-15', '2025-02-15', '2025-03-15', '2025-01-16', '2025-02-16', '2025-03-16'],
               'TotalAmount': [100, 200, 150, 50, 60, 70]}
orders = pd.DataFrame(data_orders)



joined = customers.merge(orders, on='CustomerID')

grouped = joined.groupby(['CustomerID', 'CustomerName']).agg(
    TotalOrders=('OrderID', 'nunique'),
    TotalSpent=('TotalAmount', 'sum'),
    AverageOrderValue=('TotalAmount', 'mean')
).reset_index()

filt1 = grouped['TotalOrders'] > 2
filt2 = grouped['AverageOrderValue'] > 50
final_filter = filt1 & filt2

filtered_customers = grouped[final_filter]


print(filtered_customers)
