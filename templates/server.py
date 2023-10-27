import http.server
import socketserver
import json
import csv

# Read data from the CSV file
data = []
with open('/home/bilal-zaman/Self_Learning/project/Watch_Data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append({
            'lat': float(row['Latitude']),
            'lon': float(row['Longitude'])
        })

# Define a request handler that serves the data
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get_data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            super().do_GET()

# Create an HTTP server with the custom request handler
with socketserver.TCPServer(('', 8000), RequestHandler) as httpd:
    print('Serving on port 8000...')
    httpd.serve_forever()
