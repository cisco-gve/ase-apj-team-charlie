
from tropo import Tropo, Result, Session
from http.server import BaseHTTPRequestHandler, HTTPServer
#import TropoAPI

class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        s = Session(post_body.decode('utf-8'))
        
        t = Tropo()
        t.call(to="+8618801428848", network = "SMS")
        t.say(['Hi,Patient', 'Time to take aspilin!'])
        message = t.RenderJson()

        self.wfile.write(bytes(message, "utf8"))
        return

def run():
    print('starting server...')
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
