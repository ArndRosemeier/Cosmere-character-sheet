"""
Simple local web server for the Cosmere Character Sheet
This allows the HTML to load external JSON files without CORS issues.

Usage: python run_server.py
Then open your browser to: http://localhost:8000/cosmere-character-sheet.html
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/cosmere-character-sheet.html"
        print(f"[SERVER STARTED]")
        print(f"")
        print(f"  Local Server: http://localhost:{PORT}")
        print(f"  Character Sheet: {url}")
        print(f"")
        print(f"[INFO] External files (cosmere-rules.json) will load properly")
        print(f"[INFO] Press Ctrl+C to stop the server")
        print(f"")
        
        # Open browser automatically
        try:
            webbrowser.open(url)
            print(f"[SUCCESS] Opened browser")
        except:
            print(f"[INFO] Please open your browser manually to: {url}")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n[SERVER STOPPED]")

if __name__ == "__main__":
    main()

