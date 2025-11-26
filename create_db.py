
import sqlite3
conn = sqlite3.connect("food_delivery.sqlite")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT)""")

# Restaurants table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS Restaurants (
    restaurant_id INTEGER PRIMARY KEY,
    name TEXT,
    cuisine TEXT,
    phone TEXT)""")

# Delivery Partners table
cursor.execute("""
CREATE TABLE IF NOT EXISTS DeliveryPartners (
    partner_id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT)""")

# Orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    restaurant_id INTEGER,
    partner_id INTEGER,
    status TEXT,
    order_time TEXT,
    delivery_time TEXT,
    cancellation_policy TEXT,
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(restaurant_id) REFERENCES Restaurants(restaurant_id),
    FOREIGN KEY(partner_id) REFERENCES DeliveryPartners(partner_id))""")

# smaple data

# Users
cursor.execute("INSERT OR IGNORE INTO Users VALUES (1, 'Abhi', 'abhie@domain.com')")

# Restaurants
cursor.execute("INSERT OR IGNORE INTO Restaurants VALUES (1, 'Tikka House', 'Indian', '9999999999')")

# Delivery Partners
cursor.execute("INSERT OR IGNORE INTO DeliveryPartners VALUES (1, 'Praggu', '8888888888')")

# Orders
cursor.execute("""INSERT OR IGNORE INTO Orders 
VALUES (1, 1, 1, 1, 'On the way', '2025-11-26 12:00', '2025-11-26 12:45', 'Can cancel within 10 minutes')""")

# Commit and close
conn.commit()
conn.close()

print("Database created successfully with sample data.")
