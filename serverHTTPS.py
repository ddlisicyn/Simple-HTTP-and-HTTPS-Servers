#!/usr/bin/env python3
import os
import ssl
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer
import socket

IP = '127.0.0.1'
script_dir = os.path.dirname(os.path.realpath(__file__))
keypath = os.path.join(script_dir, 'server.key')
certpath = os.path.join(script_dir, 'server.crt')
def test(HandlerClass=SimpleHTTPRequestHandler, 
      ServerClass=HTTPServer, protocol="HTTP/2.0", port=8443, bind=IP):
    server_address=(bind, port)
    HandlerClass.protocol_version = protocol
    with ServerClass(server_address, HandlerClass) as httpd:
        httpd.socket = ssl.wrap_socket(
            httpd.socket, keyfile=keypath, certfile=certpath, server_side=True)
        sa = httpd.socket.getsockname()
        serve_message = "Serving HTTP on {host} port {port} (https://{host}:{port}/)..."
        print(serve_message.format(host=sa[0], port=sa[1]))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting")
            sys.exit(0)
if __name__=='__main__':
    test()