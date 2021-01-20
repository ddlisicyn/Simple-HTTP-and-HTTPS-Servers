Для корректной работы необходимо установить на систему OpenSSL.
Затем в каталоге /bin сгенерировать ключ и сертификат командами:
openssl genrsa -out server.key 4096
openssl req -new -x509 -days 365 -key server.key -out server.crt