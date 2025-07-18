import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    """Lit les données du fichier JSON et retourne une liste de dictionnaires."""
    with open("products.json", "r") as file:
        return json.load(file)

def read_csv():
    """Lit les données du fichier CSV et retourne une liste de dictionnaires."""
    products = []
    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

def read_sql():
    """Lit les données de la base SQLite et retourne une liste de dictionnaires."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]

@app.route('/products')
def display_products():
    """Affiche la liste des produits en fonction du format spécifié (JSON, CSV, SQL)."""
    source = request.args.get("source")  # Récupère le paramètre source (json, csv, sql)
    product_id = request.args.get("id", type=int)  # Récupère l'ID (optionnel)

    # Lire les données selon la source demandée
    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    elif source == "sql":
        products = read_sql()
    else:
        return render_template("product_display.html", error="Wrong source")

    # Filtrer les produits si un ID est fourni
    if product_id:
        products = [p for p in products if p["id"] == product_id]
        if not products:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)