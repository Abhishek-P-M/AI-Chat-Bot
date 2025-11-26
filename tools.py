import sqlite3

DB_FILE = "food_delivery.sqlite"

def get_order_status(user_id):
    """Return the current status of a user's order."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM Orders WHERE user_id=?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else "No active orders found."

def get_delivery_time(user_id):
    """Return the delivery time of a user's order."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT delivery_time FROM Orders WHERE user_id=?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else "No active orders found."

def get_cancellation_policy(user_id):
    """Return the cancellation policy of a user's order."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT cancellation_policy FROM Orders WHERE user_id=?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else "No active orders found."

def get_delivery_partner_info(user_id):
    """Return the delivery partner name and phone number for a user's order."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DeliveryPartners.name, DeliveryPartners.phone
        FROM Orders
        JOIN DeliveryPartners ON Orders.partner_id = DeliveryPartners.partner_id
        WHERE Orders.user_id=? """, (user_id,))
    row = cursor.fetchone()
    conn.close()
    return f"{row[0]}, Phone: {row[1]}" if row else "No active orders found."

def get_restaurant_info(order_id):
    """Return the restaurant name, cuisine, and phone for a given order."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Restaurants.name, Restaurants.cuisine, Restaurants.phone
        FROM Orders
        JOIN Restaurants ON Orders.restaurant_id = Restaurants.restaurant_id
        WHERE Orders.order_id=?""", (order_id,))
    row = cursor.fetchone()
    conn.close()
    return f"{row[0]}, Cuisine: {row[1]}, Phone: {row[2]}" if row else "Order not found."
