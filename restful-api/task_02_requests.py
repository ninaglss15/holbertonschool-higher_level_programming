#!/usr/bin/pyhton3

import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()

        filtered_posts = []

        for p in posts:
            filtered_posts.append({
            "id": p["id"],
            "title": p["title"],
            "body": p["body"]
            })

        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered_posts)

        print("Le fichier posts.csv a été créé avec succès !")
    else:
        print("Erreur lors de la récupération des posts")
