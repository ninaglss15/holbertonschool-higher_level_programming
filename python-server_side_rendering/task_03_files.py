#!/usr/bin/python3
"""Flask application for product display from JSON and CSV files."""

from flask import Flask, render_template, request
import json
import csv

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


@app.route('/products')
def products():
    """
    Display products from JSON or CSV source.

    Query parameters:
        source (str): Data source ('json' or 'csv')
        id (int, optional): Product ID to filter

    Returns:
        Rendered template with products or error message
    """
    source = request.args.get('source')
    product_id = request.args.get('id')
    products_list = []
    error = None

    # Validate source parameter
    if source not in ['json', 'csv']:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Read data from JSON file
    if source == 'json':
        try:
            with open('products.json', 'r') as json_file:
                products_list = json.load(json_file)
        except FileNotFoundError:
            error = "JSON file not found"
            return render_template('product_display.html', error=error)

    # Read data from CSV file
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products_list.append(row)
        except FileNotFoundError:
            error = "CSV file not found"
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