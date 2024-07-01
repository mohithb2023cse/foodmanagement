from datetime import date

class FoodItem:
    def _init_(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date

class FoodWasteManagementSystem:
    def _init_(self):
        self.food_items = []

    def add_food_item(self, food_item):
        self.food_items.append(food_item)

    def remove_expired_items(self):
        today = date.today()
        expired_items = [item for item in self.food_items if item.expiry_date < today]
        self.food_items = [item for item in self.food_items if item.expiry_date >= today]
        return expired_items

    def display_items(self):
        if not self.food_items:
            print("No food items in the system.")
        else:
            print("Food items in the system:")
            for i, item in enumerate(self.food_items, 1):
                print(f"{i}. Name: {item.name}, Expiry Date: {item.expiry_date}")

    def display_expired_items(self):
        expired_items = self.remove_expired_items()
        if not expired_items:
            print("No expired items in the system.")
        else:
            print("Expired items removed from the system:")
            for i, item in enumerate(expired_items, 1):
                print(f"{i}. Name: {item.name}, Expiry Date: {item.expiry_date}")

# Sample usage
if _name_ == "_main_":
    food_system = FoodWasteManagementSystem()
    while True:
        print("\nFood Waste Management System Menu:")
        print("1. Add food item")
        print("2. Display all food items")
        print("3. Remove expired items")
        print("4. Display expired items")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the food item: ")
            expiry_date = input("Enter the expiry date (YYYY-MM-DD) of the food item: ")
            expiry_date = date.fromisoformat(expiry_date)
            food_system.add_food_item(FoodItem(name, expiry_date))
            print("Food item added successfully.")
        elif choice == "2":
            food_system.display_items()
        elif choice == "3":
            food_system.remove_expired_items()
            print("Expired items removed successfully.")
        elif choice == "4":
            food_system.display_expired_items()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")
