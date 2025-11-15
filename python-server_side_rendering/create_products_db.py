#!/usr/bin/env python3
"""
Script to create the SQLite database products.db
with a table Products containing demo product data.
"""

import sqlite3


def create_database():
    # Connect to (or create) the database file
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create the Products table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Clear existing data to avoid duplicates
    cursor.execute("DELETE FROM Products")

    # Insert demo data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()