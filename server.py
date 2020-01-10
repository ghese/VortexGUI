from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            if self.path.endswith(".html"):
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))

            if self.path.endswith(".css"):
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
                self.send_header('Content-type','text/css')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))

            if self.path.endswith(".js"):
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
                self.send_header('Content-type','application/javascript')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))

            if self.path.endswith(".jpg"):
                file_to_open = open(self.path[1:], 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','image/jpg')
                self.end_headers()
                self.wfile.write(file_to_open)

            if self.path.endswith(".png"):
                file_to_open = open(self.path[1:], 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','image/png')
                self.end_headers()
                self.wfile.write(file_to_open)

            if self.path.endswith(".eot"):
                file_to_open = open(self.path[1:], 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','application/vnd.ms-fontobject')
                self.end_headers()
                self.wfile.write(file_to_open)

            if self.path.endswith(".ttf"):
                file_to_open = open(self.path[1:], 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','application/font-sfnt')
                self.end_headers()
                self.wfile.write(file_to_open)

            if self.path.endswith(".woff"):
                file_to_open = open(self.path[1:], 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','font/woff')
                self.end_headers()
                self.wfile.write(file_to_open)

            if self.path.endswith(".woff2"):
                file_to_open = open(self.path[1:], 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','font/woff2')
                self.end_headers()
                self.wfile.write(file_to_open)
        except:
            file_to_open = "File not found"
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        #self.end_headers()
        #self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()