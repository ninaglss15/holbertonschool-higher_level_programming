#!/usr/bin/python3
"""Simple API using http.server"""

import json
import http.server


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            response = {"status": "OK"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode())

        else:
            error = {"error": "Endpoint not found"}
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(error).encode())


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleAPIHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("🚀 Server running on http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
