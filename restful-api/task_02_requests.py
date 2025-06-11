#!/usr/bin/env python3
"""
RESTful API - Task 2: Consuming and processing data from an API using Python

This module defines functions to fetch data
from a RESTful API using the `requests` library,
process the JSON response, display post titles,
and save structured data to a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print their titles.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts_list = response.json()
        for post_item in posts_list:
            print(post_item["title"])
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save
    id, title, and body to a CSV file.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts_list = response.json()
        structured_posts = [
            {
                "id": post_item["id"],
                "title": post_item["title"],
                "body": post_item["body"],
            }
            for post_item in posts_list
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
            csv_fieldnames = ["id", "title", "body"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=csv_fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(structured_posts)
    else:
        print("Failed to fetch posts")
