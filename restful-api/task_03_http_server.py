#!/usr/bin/env python3
"""
RESTful API - Task 3: Basic HTTP Server with JSON responses using http.server

This script sets up a simple HTTP server on port 8000,
handles GET requests on specific endpoints,
and returns text or JSON responses accordingly.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET requests for specific endpoints:
        - "/" returns a welcome text message
        - "/data" returns a JSON dataset
        - "/status" returns a simple status message in JSON
        - other paths return 404 Not Found
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            status = {
                "status": "OK"
            }
            json_status = json.dumps(status)
            self.wfile.write(json_status.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            message = "Endpoint not found"
            self.wfile.write(message.encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    port = 8000
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting http.server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
