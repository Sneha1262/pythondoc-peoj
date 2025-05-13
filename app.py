from http.server import BaseHTTPRequestHandler, HTTPServer

def say_hello():
    print("Hello from Dockerized Python!")

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Dockerized Python!")

if __name__ == "__main__":
    say_hello()
    server_address = ('0.0.0.0', 5000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Running on port 5000...")
    httpd.serve_forever()
