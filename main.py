from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8080


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write("Hello from the braincell".encode("utf-8"))


def main():
    server = HTTPServer((HOST, PORT), RequestHandler)
    print(f"Server is running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
