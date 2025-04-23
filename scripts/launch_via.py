import os
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer

class ViaHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.join(os.getcwd(), 'via'), **kwargs)

def start_via():
    # Preprocess images
    subprocess.run(['python', 'scripts/preprocess.py'])
    
    # Launch server
    server = HTTPServer(('', 8000), ViaHandler)
    print("VIA accessible at: http://localhost:8000/html/_via_image_annotator.html")
    server.serve_forever()

if __name__ == '__main__':
    start_via()