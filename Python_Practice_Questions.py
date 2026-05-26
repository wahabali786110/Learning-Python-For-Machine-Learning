# Question 1

# def aggregate_sales(data):
#     dict1={}
#     for item in data:
#         raw_amount=item.get('amount')
#         try:
#             amount=float(raw_amount)
#         except(ValueError,TypeError):
#             continue

#         category=item.get('category')
#         if category is None:
#             category='unknown'

#         if category not in dict1:
#             dict1[category]=0.0
        
#         dict1[category]+=amount

#     return dict1



# sales_data = [
#     {"category": "electronics", "amount": 120.5},
#     {"category": "clothing", "amount": 45.0},
#     {"amount": 30.0}, # Missing category
#     {"category": "electronics", "amount": "error"}, # Bad amount
#     {"category": "clothing", "amount": 15.5},
#     {"category": None, "amount": 10.0}
# ]

# print(aggregate_sales(sales_data))

# Question 2

# def generate_reports(transactions):
#     dict1={}
#     dict1['unique_items']=[]
#     for item in transactions:
#         sales=item.get('price')
#         piece=item.get('item')

#         if piece not in dict1["unique_items"]:
#             dict1["unique_items"].append(piece)

#         if 'total_revenue' not in dict1:
#             dict1['total_revenue']=sales
#         else:
#             dict1['total_revenue']+=sales

#     return dict1

# orders = [
#     {"item": "Burger", "price": 5.50},
#     {"item": "Fries", "price": 2.00},
#     {"item": "Burger", "price": 5.50},
#     {"item": "Soda", "price": 1.50}
# ]


# print(generate_reports(orders))

# Question 3
# def clean_temperatures(raw_data):
#     list1=[]
#     for item in raw_data:
#         try:
#             amount=float(item)
#         except(ValueError,TypeError):
#             continue

#         list1.append(amount)

#     return list1


# api_response = [32, " 35.5 ", None, "server_error", 40.1, ""]
# print(clean_temperatures(api_response))

# Question 4
# class ShiftManager:
#     def __init__(self):
#         self.active_staff=[]

#     def clock_in(self,employee_name):
#         if employee_name not in self.active_staff:
#             self.active_staff.append(employee_name)

#     def clock_out(self,employee_name):
#         try:
#             self.active_staff.remove(employee_name)
#         except ValueError as e:
#             print(e)

#     def get_current_staff(self):
#         return self.active_staff
    
# manager = ShiftManager()
# manager.clock_in("Ali")
# manager.clock_in("Zain")
# manager.clock_in("Ali") 
# manager.clock_out("Zain")

# print(manager.get_current_staff())

# Question 5
# import numpy as np

# def get_low_stock_items(stock_array, threshold):
#     index=np.where(stock_array<threshold)[0]
#     return index


# inventory = np.array([9, 12, 1, 4, 80, 2])
# alert_threshold = 10
# print(get_low_stock_items(inventory,alert_threshold))

# Question 6
import numpy as np

def celsius_to_fahrenheit(c_array):
    return np.round((c_array*(9/5))+32,decimals=1)

celsius_temps = np.array([0, 1,25, 37.5, 100])

print(celsius_to_fahrenheit(celsius_temps))

