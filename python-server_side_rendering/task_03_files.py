#!/usr/bin/python3
"""
Flask application to display products from JSON or CSV with optional filtering by id.
"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products_list = []

    if source == 'json':
        try:
            with open('products.json') as f:
                products_list = json.load(f)
        except FileNotFoundError:
            return render_template('product_display.html', error="JSON file not found")
        except json.JSONDecodeError:
            return render_template('product_display.html', error="Invalid JSON file")
    elif source == 'csv':
        try:
            with open('products.csv') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products_list.append(row)
        except FileNotFoundError:
            return render_template('product_display.html', error="CSV file not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid CSV format")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            products_list = [p for p in products_list if p['id'] == product_id]
            if not products_list:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
