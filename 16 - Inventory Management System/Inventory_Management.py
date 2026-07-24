class Inventory:

    def __init__(self):
        self.items = {}

    def add_item(self):

        name = input("Enter Item Name: ").strip().title()

        if name in self.items:
            print("Item already exists.")
            return

        try:
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price (₹): "))

            self.items[name] = {
                "quantity": quantity,
                "price": price
            }

            print("Item added successfully.")

        except ValueError:
            print("Invalid input.")

    def view_items(self):

        if not self.items:
            print("\nInventory is empty.")
            return

        print("\n========== INVENTORY ==========")

        for name, details in self.items.items():

            print(f"\nItem     : {name}")
            print(f"Quantity : {details['quantity']}")
            print(f"Price    : ₹{details['price']:.2f}")

    def update_item(self):

        name = input("Enter Item Name: ").strip().title()

        if name not in self.items:
            print("Item not found.")
            return

        try:
            quantity = int(input("Enter New Quantity: "))
            price = float(input("Enter New Price (₹): "))

            self.items[name]["quantity"] = quantity
            self.items[name]["price"] = price

            print("Item updated successfully.")

        except ValueError:
            print("Invalid input.")

    def delete_item(self):

        name = input("Enter Item Name: ").strip().title()

        if name in self.items:
            del self.items[name]
            print("Item deleted successfully.")
        else:
            print("Item not found.")

    def total_value(self):

        total = 0

        for item in self.items.values():
            total += item["quantity"] * item["price"]

        print(f"\nTotal Inventory Value: ₹{total:.2f}")


inventory = Inventory()

while True:

    print("\n" + "=" * 45)
    print("      INVENTORY MANAGEMENT")
    print("=" * 45)

    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Total Inventory Value")
    print("0. Exit")

    try:

        choice = int(input("\nSelect Option: "))

        if choice == 1:
            inventory.add_item()

        elif choice == 2:
            inventory.view_items()

        elif choice == 3:
            inventory.update_item()

        elif choice == 4:
            inventory.delete_item()

        elif choice == 5:
            inventory.total_value()

        elif choice == 0:
            print("\nGoodbye!")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")