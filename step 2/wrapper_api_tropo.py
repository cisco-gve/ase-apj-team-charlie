from tropo import Tropo, Result, Session
from http.server import BaseHTTPRequestHandler, HTTPServer


#Tropo Say()
#Answering incoming calls
class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len)

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        s = Session(post_body.decode('utf-8'))
        t = Tropo()
        t.say(['Hello world!', 'This is a test'])
        message = t.RenderJson()

        # Send message back to client
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


#Tropo Ask() and Call Transfer() Function
#Following example is asking for digit and figure out the digit you chose and transfer the call

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
            print("ANSWER " + answer)
            t.say("You chose "+ answer)
            t.transfer("+14075550100")
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
            t.ask(choices="0,1,2,3,4,5,6,7,8,9", timeout=60, name="digit", say="Pick a number from 0 to 9")
            t.on(event="continue",next=("/continue"))
            message = t.RenderJson()
            self.wfile.write(bytes(message, "utf8"))
            return

        
#Create Python Web Server to interact with Tropo WebAPI request      
def run():
    print('starting server...')
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

