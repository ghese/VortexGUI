from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        script_dir = os.path.dirname(__file__)

        if self.path == '/':
            self.path = '/index.html'
        try:
            if self.path.endswith(".html"):
                abs_file_path = os.path.join(script_dir, self.path[1:])
                file_to_open = open(abs_file_path).read()
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))

            if self.path.endswith(".css"):
                abs_file_path = os.path.join(script_dir, self.path[1:])
                file_to_open = open(abs_file_path).read()
                self.send_response(200)
                self.send_header('Content-type','text/css')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))

            if self.path.endswith(".js"):
                abs_file_path = os.path.join(script_dir, self.path[1:])
                file_to_open = open(abs_file_path).read()
                self.send_response(200)
                self.send_header('Content-type','application/javascript')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))

            if self.path.endswith(".jpg"):
                abs_file_path = os.path.join(script_dir, self.path[1:])
                file_to_open = open(abs_file_path, 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','image/jpg')
                self.end_headers()
                self.wfile.write(file_to_open)

            if self.path.endswith(".png"):
                abs_file_path = os.path.join(script_dir, self.path[1:])
                file_to_open = open(abs_file_path, 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','image/png')
                self.end_headers()
                self.wfile.write(file_to_open)

            if self.path.endswith(".eot"):
                abs_file_path = os.path.join(script_dir, self.path[1:])
                file_to_open = open(abs_file_path, 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','application/vnd.ms-fontobject')
                self.end_headers()
                self.wfile.write(file_to_open)

            if self.path.endswith(".ttf"):
                abs_file_path = os.path.join(script_dir, self.path[1:])
                file_to_open = open(abs_file_path, 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','application/font-sfnt')
                self.end_headers()
                self.wfile.write(file_to_open)

            if self.path.endswith(".woff"):
                abs_file_path = os.path.join(script_dir, self.path[1:])
                file_to_open = open(abs_file_path, 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','font/woff')
                self.end_headers()
                self.wfile.write(file_to_open)

            if self.path.endswith(".woff2"):
                abs_file_path = os.path.join(script_dir, self.path[1:])
                file_to_open = open(abs_file_path, 'rb').read()
                self.send_response(200)
                self.send_header('Content-type','font/woff2')
                self.end_headers()
                self.wfile.write(file_to_open)

            #Do Actions
            if self.path.endswith("launch1.do"):
                file_to_open = "Launched the control-system"
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))
                print("Do roslaunch vortex manta.launch")
            if self.path.endswith("launch2.do"):
                file_to_open = "Enabled Xbox controller"
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))
                print("Do roslaunch joystick_interface joystick_interface.lauch")
            if self.path.endswith("launch3.do"):
                file_to_open = "Thrusters Armed"
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))
                print("Do roslaunch pub /mcu_arm std/msgs/String \"data: 'arm'\"")
            if self.path.endswith("launch4.do"):
                file_to_open = "Thrusters Disarmed"
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))
                print("Do roslaunch pub /mcu_arm std/msgs/String \"data: 'kev'\"")
        except:
            file_to_open = "File not found:" + self.path
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        #end

httpd = HTTPServer(('localhost', 80), Serv) #Change IP and port as needed.
httpd.serve_forever()