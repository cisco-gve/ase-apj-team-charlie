
from tropo import Tropo, Result, Session
from http.server import BaseHTTPRequestHandler, HTTPServer
#import TropoAPI

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if "/continue" in self.path:
            content_len = int(self.headers['content-length'])
            post_body = self.rfile.read(content_len)
            print("IN CONTINUE")
            print(post_body)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            r = Result(post_body.decode('utf-8'))
            
            t = Tropo()
            answer = r.getValue()

            if int(answer) == 1:
                t.say("We are now transferring you to a Charlie Hospital phone operator!   Please wait a moment...")

            elif int(answer) == 2:
                t.say("Please provide your information:  Your name, ID card, hospital department and doctor!!  We will make the appointment for you!")

            else:
                t.say("We see from your phone number you have an appointment with Dr.Green on Friday May 5th at 2:30PM.")

            print("ANSWER " + answer)

            message = t.RenderJson()           
            self.wfile.write(bytes(message, "utf8"))
            return

        else:
            content_len = int(self.headers['content-length'])
            post_body = self.rfile.read(content_len)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            print(post_body)
            s = Session(post_body.decode('utf-8'))
            t = Tropo()
            t.ask(choices="1,2,3", timeout=60, name="digit",
                  say="Welcome to Charlie Hospital!!  Please press one to speak to phone operator;   Press two to make a new appointment; Press three to check your appointment")
            t.on(event="continue",next=("/continue"))
            message = t.RenderJson()
            self.wfile.write(bytes(message, "utf8"))
            return

def run():
    print('starting server...')
    server_address = ('127.0.0.1', 8088)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()

