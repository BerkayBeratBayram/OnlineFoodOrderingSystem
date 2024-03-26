import pymysql
from tkinter import *


db = pymysql.connect(
    host='127.0.0.1',
    user='basar',
    password='basar123',
    db='restaurant_db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = db.cursor()


root = Tk()
root.title("Online Food Ordering")


menu_frame = Frame(root)
menu_frame.pack(padx=20, pady=20)

def get_user_input_user():
    user_id = int(entries_user["UserID"].get())
    first_name = entries_user["FirstName"].get()
    last_name = entries_user["LastName"].get()
    email = entries_user["Email"].get()
    phone_number = entries_user["PhoneNumber"].get()
    address = entries_user["Address"].get()
    return user_id, first_name, last_name, email, phone_number, address

def get_user_input_restaurant():
    restaurant_id = int(entries_restaurant["RestaurantID"].get())
    restaurant_name = entries_restaurant["RestaurantName"].get()
    cuisine_type = entries_restaurant["CuisineType"].get()
    restaurant_address = entries_restaurant["RestaurantAddress"].get()
    contact_number = entries_restaurant["ContactNumber"].get()
    return restaurant_id, restaurant_name, cuisine_type, restaurant_address, contact_number

def get_user_input_menu():
    item_id = int(entries_menu["ItemID"].get())
    restaurant_id = int(entries_menu["RestaurantID"].get())
    item_name = entries_menu["ItemName"].get()
    price = float(entries_menu["Price"].get())
    description = entries_menu["Description"].get()
    return item_id, restaurant_id, item_name, price, description


def add_user():
    try:
        user_id, first_name, last_name, email, phone_number, address = get_user_input_user()


        cursor.execute("SELECT * FROM User WHERE UserID = %s", (user_id,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("You can not create with existing UserID, try with a different UserID.")
        else:
            cursor.execute("INSERT INTO User (UserID, FirstName, LastName, Email, PhoneNumber, Address) VALUES (%s, %s, %s, %s, %s, %s)",
                           (user_id, first_name, last_name, email, phone_number, address))
            db.commit()
            print("User added successfully.")

    except Exception as e:
        print(f"Error: {e}")


def update_user():
    try:
        user_id, first_name, last_name, email, phone_number, address = get_user_input_user()
        cursor.execute("UPDATE User SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s, Address=%s WHERE UserID=%s",
                       (first_name, last_name, email, phone_number, address, user_id))
        db.commit()
        print("User updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def delete_user():
    try:
        user_id = int(entries_user["UserID"].get())
        cursor.execute("DELETE FROM User WHERE UserID=%s", (user_id,))
        db.commit()
        print("User deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")


def add_restaurant():
    try:
        restaurant_id, restaurant_name, cuisine_type, restaurant_address, contact_number = get_user_input_restaurant()


        cursor.execute("SELECT * FROM Restaurant WHERE RestaurantID = %s", (restaurant_id,))
        existing_restaurant = cursor.fetchone()

        if existing_restaurant:
            print("You can not create with an existing RestaurantID, try with a different RestaurantID.")
        else:
            cursor.execute("INSERT INTO Restaurant (RestaurantID, RestaurantName, CuisineType, RestaurantAddress, ContactNumber) VALUES (%s, %s, %s, %s, %s)",
                           (restaurant_id, restaurant_name, cuisine_type, restaurant_address, contact_number))
            db.commit()
            print("Restaurant added successfully.")
    except Exception as e:
        print(f"Error: {e}")


def update_restaurant():
    try:
        restaurant_id, restaurant_name, cuisine_type, restaurant_address, contact_number = get_user_input_restaurant()
        cursor.execute("UPDATE Restaurant SET RestaurantName=%s, CuisineType=%s, RestaurantAddress=%s, ContactNumber=%s WHERE RestaurantID=%s",
                       (restaurant_name, cuisine_type, restaurant_address, contact_number, restaurant_id))
        db.commit()
        print("Restaurant updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def delete_restaurant():
    try:
        restaurant_id = int(entries_restaurant["RestaurantID"].get())
        cursor.execute("DELETE FROM Restaurant WHERE RestaurantID=%s", (restaurant_id,))
        db.commit()
        print("Restaurant deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")


def add_menu():
    try:
        item_id, restaurant_id, item_name, price, description = get_user_input_menu()


        cursor.execute("SELECT * FROM Menu WHERE ItemID = %s", (item_id,))
        existing_menu_item = cursor.fetchone()

        if existing_menu_item:
            print("You can not create with an existing ItemID, try with a different ItemID.")
        else:
            cursor.execute("INSERT INTO Menu (ItemID, RestaurantID, ItemName, Price, Description) VALUES (%s, %s, %s, %s, %s)",
                           (item_id, restaurant_id, item_name, price, description))
            db.commit()
            print("Menu item added successfully.")
    except Exception as e:
        print(f"Error: {e}")


def update_menu():
    try:
        item_id, restaurant_id, item_name, price, description = get_user_input_menu()
        cursor.execute("UPDATE Menu SET RestaurantID=%s, ItemName=%s, Price=%s, Description=%s WHERE ItemID=%s",
                       (restaurant_id, item_name, price, description, item_id))
        db.commit()
        print("Menu item updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def delete_menu():
    try:
        item_id = int(entries_menu["ItemID"].get())
        cursor.execute("DELETE FROM Menu WHERE ItemID=%s", (item_id,))
        db.commit()
        print("Menu item deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")


labels_user = ["UserID", "FirstName", "LastName", "Email", "PhoneNumber", "Address"]
entries_user = {}

for i, label in enumerate(labels_user):
    entry_label = Label(menu_frame, text=f"Enter {label}:")
    entry_label.grid(row=i, column=0, padx=5, pady=5)

    entry = Entry(menu_frame)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries_user[label] = entry


add_user_button = Button(menu_frame, text="Add User", command=add_user)
add_user_button.grid(row=len(labels_user), column=0, pady=10, sticky="ew")

update_user_button = Button(menu_frame, text="Update User", command=update_user)
update_user_button.grid(row=len(labels_user), column=1, pady=10, sticky="ew")

delete_user_button = Button(menu_frame, text="Delete User", command=delete_user)
delete_user_button.grid(row=len(labels_user), column=2, pady=10, sticky="ew")


labels_restaurant = ["RestaurantID", "RestaurantName", "CuisineType", "RestaurantAddress", "ContactNumber"]
entries_restaurant = {}

for i, label in enumerate(labels_restaurant):
    entry_label = Label(menu_frame, text=f"Enter {label}:")
    entry_label.grid(row=i + len(labels_user) + 4, column=0, padx=5, pady=5)

    entry = Entry(menu_frame)
    entry.grid(row=i + len(labels_user) + 4, column=1, padx=5, pady=5)
    entries_restaurant[label] = entry


add_restaurant_button = Button(menu_frame, text="Add Restaurant", command=add_restaurant)
add_restaurant_button.grid(row=len(labels_restaurant) + len(labels_user) + 4, column=0, pady=10, sticky="ew")


update_restaurant_button = Button(menu_frame, text="Update Restaurant", command=update_restaurant)
update_restaurant_button.grid(row=len(labels_restaurant) + len(labels_user) + 4, column=1, pady=10, sticky="ew")

delete_restaurant_button = Button(menu_frame, text="Delete Restaurant", command=delete_restaurant)
delete_restaurant_button.grid(row=len(labels_restaurant) + len(labels_user) + 4, column=2, pady=10, sticky="ew")


labels_menu = ["ItemID", "RestaurantID", "ItemName", "Price", "Description"]
entries_menu = {}

for i, label in enumerate(labels_menu):
    entry_label = Label(menu_frame, text=f"Enter {label}:")
    entry_label.grid(row=i + len(labels_restaurant) + len(labels_user) + 8, column=0, padx=5, pady=5)

    entry = Entry(menu_frame)
    entry.grid(row=i + len(labels_restaurant) + len(labels_user) + 8, column=1, padx=5, pady=5)
    entries_menu[label] = entry


add_menu_button = Button(menu_frame, text="Add Menu", command=add_menu)
add_menu_button.grid(row=len(labels_menu) + len(labels_restaurant) + len(labels_user) + 8, column=0, pady=10, sticky="ew")


update_menu_button = Button(menu_frame, text="Update Menu", command=update_menu)
update_menu_button.grid(row=len(labels_menu) + len(labels_restaurant) + len(labels_user) + 8, column=1, pady=10, sticky="ew")


delete_menu_button = Button(menu_frame, text="Delete Menu", command=delete_menu)
delete_menu_button.grid(row=len(labels_menu) + len(labels_restaurant) + len(labels_user) + 8, column=2, pady=10, sticky="ew")


user_id_label = Label(root, text="User ID:")
user_id_label.pack()

user_id_entry = Entry(root)
user_id_entry.pack()

cursor.execute("SELECT * FROM Menu")
menu_items = cursor.fetchall()

menu_label = Label(root, text="Menu:")
menu_label.pack()

for item in menu_items:
    label = Label(root, text=f"{item['ItemID']}. {item['ItemName']} - {item['Price']} TL")
    label.pack()


item_id_label = Label(root, text="Enter the ID of the product you want to order:")
item_id_label.pack()

item_id_entry = Entry(root)
item_id_entry.pack()

quantity_label = Label(root, text="Enter how many you want:")
quantity_label.pack()

quantity_entry = Entry(root)
quantity_entry.pack()


def place_order():
    try:
        user_id = int(user_id_entry.get())

        cursor.execute("SELECT * FROM User WHERE UserID = %s", (user_id,))
        user = cursor.fetchone()

        if user:
            print(f"User: {user['FirstName']} {user['LastName']}")


            item_id = int(item_id_entry.get())
            quantity = int(quantity_entry.get())


            cursor.execute("SELECT * FROM Menu WHERE ItemID = %s", (item_id,))
            menu_item = cursor.fetchone()

            if menu_item:

                cursor.execute("INSERT INTO Orders (UserID, OrderDate, TotalAmount, Status) VALUES (%s, NOW(), (SELECT SUM(menu.Price * %s) FROM Menu menu WHERE menu.ItemID = %s), 'Pending')", (user_id, quantity, item_id))

                order_id = cursor.lastrowid
                cursor.execute("INSERT INTO OrderItem (OrderID, ItemID, Quantity) VALUES (%s, %s, %s)", (order_id, item_id, quantity))
                db.commit()
                print("Your order has been created successfully.")
            else:
                print("No such product was found in the menu.")
        else:
            print("User not found.")

    except ValueError:
        print("Invalid user ID, please enter a number.")


place_order_button = Button(root, text="Order", command=place_order)
place_order_button.pack()



root.mainloop()


cursor.close()
db.close()
