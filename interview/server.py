'''
Generated by Claude, just testing how this type of stuff works.
'''

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# In-memory key-value store
storage = {}

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        
        if parsed_url.path == '/set':
            # Handle set request
            params = parse_qs(parsed_url.query)
            for key, value in params.items():
                storage[key] = value[0]
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Key-value pair stored')
        elif parsed_url.path == '/get':
            # Handle get request
            params = parse_qs(parsed_url.query)
            if 'key' in params:
                key = params['key'][0]
                if key in storage:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(storage[key].encode())
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b'Key not found')
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Missing key parameter')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Page not found')

def run_server():
    server_address = ('localhost', 4000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server on http://localhost:4000/')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()