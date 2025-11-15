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

    if source == 'json':
        try:
            with open('products.json', 'r') as json_file:
                products_list = json.load(json_file)
        except FileNotFoundError:
            return render_template('product_display.html',
                                   error="JSON file not found")
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                products_list = []
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products_list.append(row)
        except FileNotFoundError:
            return render_template('product_display.html',
                                   error="CSV file not found")
    else:
        return render_template('product_display.html',
                               error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [
                p for p in products_list
                if p['id'] == product_id
            ]
            if not filtered_products:
                return render_template('product_display.html',
                                       error="Product not found")
            products_list = filtered_products
        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid product ID")

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
