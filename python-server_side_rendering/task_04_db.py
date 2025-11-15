#!/usr/bin/python3
"""Flask application for product display from JSON, CSV and SQLite files."""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    """Home page route."""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page route."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Items page route."""
    with open('items.json', 'r') as f:
        data = json.load(f)
        items_list = data.get('items', [])
    return render_template('items.html', items=items_list)


def read_json_data():
    """
    Read product data from JSON file.

    Returns:
        list: List of product dictionaries
    """
    with open('products.json', 'r') as json_file:
        return json.load(json_file)


def read_csv_data():
    """
    Read product data from CSV file.

    Returns:
        list: List of product dictionaries
    """
    products = []
    with open('products.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sql_data():
    """
    Read product data from SQLite database.

    Returns:
        list: List of product dictionaries
    """
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        
        conn.close()
    except sqlite3.Error as e:
        raise Exception(f"Database error: {e}")
    
    return products


@app.route('/products')
def products():
    """
    Display products from JSON, CSV or SQL source.

    Query parameters:
        source (str): Data source ('json', 'csv', or 'sql')
        id (int, optional): Product ID to filter

    Returns:
        Rendered template with products or error message
    """
    source = request.args.get('source')
    product_id = request.args.get('id')
    products_list = []
    error = None

    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Read data from appropriate source
    try:
        if source == 'json':
            products_list = read_json_data()
        elif source == 'csv':
            products_list = read_csv_data()
        elif source == 'sql':
            products_list = read_sql_data()
    except FileNotFoundError:
        error = f"{source.upper()} file not found"
        return render_template('product_display.html', error=error)
    except Exception as e:
        error = str(e)
        return render_template('product_display.html', error=error)

    # Filter by product ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            products_list = [p for p in products_list if p['id'] == product_id]
            if not products_list:
                error = "Product not found"
                return render_template('product_display.html', error=error)
        except ValueError:
            error = "Invalid product ID"
            return render_template('product_display.html', error=error)

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)