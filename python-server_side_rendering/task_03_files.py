#!/usr/bin/env python3
"""
Displaying Data from JSON or CSV Files in Flask
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/products')
def products():

    source = request.args.get("source", "").lower()
    products = []
    error = None

    # --- LECTURE DES FICHIERS ---
    try:
        if source == "json":
            with open("products.json", "r", encoding="utf-8") as f:
                products = json.load(f)

        elif source == "csv":
            with open("products.csv", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                products = []
                for row in reader:
                    products.append({
                        "id": int(row["id"]),
                        "name": row["name"],
                        "category": row["category"],
                        "price": float(row["price"])
                    })

        else:
            error = "Wrong source"

    except Exception as e:
        error = "Erreur lors du chargement des données : {}".format(e)

    # --- FILTRAGE PAR ID ---
    product_id = request.args.get("id")

    if product_id and not error:
        try:
            product_id = int(product_id)

            found = None
            for product in products:
                if int(product["id"]) == product_id:
                    found = product
                    break

            if found:
                products = [found]
            else:
                error = "Product not found"
                products = []

        except ValueError:
            error = "Invalid ID format. Must be a number."
            products = []

    return render_template(
        "product_display.html",
        products=products,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
