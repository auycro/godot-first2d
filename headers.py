import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler, test

DIRECTORY = "bin"

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Opener-Policy','same-origin')
        self.send_header('Cross-Origin-Embedder-Policy','require-corp')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    #document_root_dir = os.path.expanduser('~/document_root')
    os.chdir("./bin")
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8080)
