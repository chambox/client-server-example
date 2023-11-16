# A simple HTTP server
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from the server!")


httpd = HTTPServer(("0.0.0.0", 8000), SimpleHandler)
print("Server started on port 8000...")
httpd.serve_forever()
