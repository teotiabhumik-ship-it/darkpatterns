"""
Simple HTTP Server for Dark Pattern Test Sites
Serves all test sites on port 5000 with CORS enabled.
Run: python server.py
"""

import http.server
import socketserver
import os
import sys

PORT = 5000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def translate_path(self, path):
        if path.startswith('/darkpatterns'):
            path = path[len('/darkpatterns'):]
            if not path or path == '/':
                path = '/index.html'
        return super().translate_path(path)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("=" * 60)
        print(f"Dark Pattern Test Sites running at: http://localhost:{PORT}")
        print("=" * 60)
        print(f"- Portal:               http://localhost:{PORT}/index.html")
        print(f"- Azure Grand Hotel:    http://localhost:{PORT}/hotel-booking/index.html")
        print(f"- FitPulse Club:        http://localhost:{PORT}/subscription-service/index.html")
        print(f"- ConcertPass Tickets:  http://localhost:{PORT}/ticket-hub/index.html")
        print("=" * 60)
        print("Press Ctrl+C to stop the server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == '__main__':
    main()
