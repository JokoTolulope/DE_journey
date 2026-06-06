''' import csv

with open("ng_ecommerce_orders.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row) '''

import csv

completed_orders = []

with open("ng_ecommerce_orders.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["order_status"] == "completed":
            completed_orders.append(row)

print(f"Total completed orders: {len(completed_orders)}")
print("---")
for order in completed_orders[:5]:
    print(f"  {order['order_id']} | {order['customer_name']} | {order['city']} | {order['total_amount_ngn']}") 
    
# find orders marked completed but missing a delivery date
#data quality check

suspicious_orders = [
    row for row in completed_orders
    if row["delivery_date"] == ""
]

print(f"\n completed orders missing a delivery date: {len(suspicious_orders)}")
for order in suspicious_orders:
    print(f"  {order['order_id']} | {order['customer_name']} | Status: {order['order_status']} | Delivery: '{order['delivery_date']}'")

#Summary by city, which city has the most completed orders
city_counts = {}
for order in completed_orders:
    city = order["city"]
    city_counts[city] = city_counts.get(city, 0) + 1

#sort by count descending
top_cities = sorted(city_counts.items(), key = lambda x: x[1], reverse = True)

print("\n  Completed orders by city:")
for city, count in top_cities:
    print(f"  {city}: {count} orders")
    
#Total revenue from completed orders
total_revenue = sum(int(order["total_amount_ngn"]) for order in completed_orders)
print(f"\n  Total revenue from completed orders:  {total_revenue:,}")