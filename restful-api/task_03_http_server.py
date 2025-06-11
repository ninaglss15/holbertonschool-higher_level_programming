#!/usr/bin/env python3
"""
RESTful API - Task 3: Develop a simple API using Python with
the http.server module

This script implements a basic HTTP server using Python's
built-in http.server module.
It handles GET requests, serves text and JSON responses,
and implements simple endpoint routing.
"""

import http.server
import json


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET requests to the server.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, MyRequestHandler)

httpd.serve_forever()
