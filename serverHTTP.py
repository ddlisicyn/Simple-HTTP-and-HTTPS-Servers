#!/usr/bin/env python3
import http.server
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
        return IP
IP = get_ip()
page1 = open ("index.html", "rb")
f1 = page1.read()
class HttpProcessor(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('content-type','text/html')
    self.end_headers()
    self.wfile.write(f1)
#CGIHTTPRequestHandler
#BaseHTTPRequestHandler
handler = HttpProcessor
server = (IP,80)
HTTPD = http.server.HTTPServer(server, handler)
print (f'server START on {server}')
HTTPD.serve_forever()
