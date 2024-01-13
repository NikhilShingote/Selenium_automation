from datetime import datetime
import pandas as pd

class Hotelmanagement:
    def __init__(self):
        self.orders = pd.DataFrame(columns=["Item name", "Quantity", "Type", "DateTime", "Time of purchase"])

    def add_order(self):
        itemname = input("Enter the itemname: ")
        itemType = input("Enter the ItemType: ")
        Quantity = int(input("Enter the Quantity: "))
        order_Date = datetime.now().strftime("%Y-%m-%d")
        order_time = datetime.now().time()

        self.orders.loc[len(self.orders.index)] = [itemname, Quantity, itemType, order_Date, order_time]

    def view_orders(self):
        if self.orders.empty:
            print("No orders to display")
        else:
            print(self.orders)

    def update_order(self):
        order_id = int(input("Enter the Order Id: "))

        if order_id >= len(self.orders):
            print("Orders not found: ")
        else:
            print("Updating Order Id: ", order_id)
            self.orders.at[order_id, "Item name"] = input("Enter the item name to change")
            self.orders.at[order_id, "Quantity"] = int(input("Enter the item name to change"))
            print("Order Updated successfully")

    def save_to_excel(self):
        self.orders.to_excel("Bakery_orders_practice.xlsx")
        print("Orders saved to Excel sheet")

Order_system = Hotelmanagement()

while True:
    print("\n1. Add Order\n2. View Orders\n3. Update Order\n4. Save to Excel\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        Order_system.add_order()
    elif choice == '2':
        Order_system.view_orders()
    elif choice == '3':
        Order_system.update_order()
    elif choice == '4':
        Order_system.save_to_excel()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")