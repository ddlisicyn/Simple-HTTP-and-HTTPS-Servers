import http.server
from io import BytesIO
import mysql.connector


class HttpProcessor(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(page)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        date, currency = kurs_from_db(body.decode('utf-8'))
        response = BytesIO()
        response.write(b'USD on ' + date.encode() + b' = ' + str(currency[0]).encode() + b'\n')
        response.write(b'EUR on ' + date.encode() + b' = ' + str(currency[1]).encode() + b'\n')
        self.wfile.write(response.getvalue())


def kurs_from_db(body):
    if 'calendar' in body:
        date = body.replace('calendar=', '').replace('-', '.')
    else:
        return
        conn = mysql.connector.connect(user="admin", password="qwerty123qwerty123", host="37.139.42.19", port=3306, database="MySQL-8037")
        sql = conn.cursor()
        db_response = sql.execute(
            f"select USD, EUR from Currency where DATE = to_date('{date}', 'YYYY.MM.DD')"
            ).fetchone()
        return date, db_response


page = open("index.html", "rb").read()
server = ('localhost', 80)
HTTPD = http.server.HTTPServer(server, HttpProcessor)
print(f'server START on {server}')
HTTPD.serve_forever()