import http.server
import socketserver
import os

PORT = 8000
web_dir = os.path.join(os.path.dirname(__file__), '../')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at http://localhost:{PORT}")
print(f"Access VIA at http://localhost:{PORT}/via.html")
httpd.serve_forever()