import json
from flask import Flask, render_template

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
    # Lire les données du fichier JSON
    with open("items.json", "r") as file:
        data = json.load(file)  # Charge le JSON en dictionnaire
        items_list = data.get("items", [])  # Récupère la liste d'items ou une liste vide

    return render_template('items.html', items=items_list)  # Passe la liste au template

if __name__ == '__main__':
    app.run(debug=True, port=5000)