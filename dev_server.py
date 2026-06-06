import http.server
import socketserver
import os

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # If the requested path has no extension and is not a directory, try adding .html
        if self.path != '/' and not os.path.exists(self.translate_path(self.path)):
            if os.path.exists(self.translate_path(self.path) + '.html'):
                self.path += '.html'
            elif self.path.endswith('/index'):
                self.path = self.path.replace('/index', '/index.html')
        
        # If they just request /index without .html
        if self.path == '/index':
            self.path = '/index.html'

        return super().do_GET()

# Ensure we can reuse the port immediately
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT} with .html auto-resolution")
    httpd.serve_forever()
