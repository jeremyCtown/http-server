from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from cowpy import cow

ren = cow.Ren()
ren_msg = ren.milk('400 Error!?! You steenkin eeeediot')
# print(ren_msg)
stimpy = cow.Stimpy()
errr = cow.Cheese()
errr_msg = errr.milk('I am Errr.. You can query this site using /cow?msg="text" as an endpoint ')
post_dict = {'content': None}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"""
            <!DOCTYPE html>
<html>
<head>
    <title> cowsay </title>
</head>
<body>
    <header>
        <nav>
        <ul>
            <li><a href="/cowsay">cowsay</a></li>
        </ul>
        </nav>
    <header>
    <main>
        <!-- project description -->
    </main>
</body>
</html>
""")
            return
        elif parsed_path.path == '/cowsay':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(errr_msg.encode('utf8'))
        elif parsed_path.path == '/cow':
            try:
                msg = json.loads(parsed_qs['msg'][0])
                
            except (KeyError, json.decoder.JSONDecoderError):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(ren_msg.encode('utf8'))
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(stimpy.milk(msg).encode('utf8'))
            return

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/cow':
            try:
                msg = parsed_qs['msg'][0]
                msg_json = stimpy.milk(msg)
                post_dict['content'] = msg_json
                
            except (KeyError, json.decoder.JSONDecodeError):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(ren_msg.encode('utf8'))
                return
     
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(post_dict).encode('utf8'))
            return
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    
def create_server():
    return HTTPServer(('127.0.0.1', 3000), SimpleHTTPRequestHandler)


def run_forever():
    server = create_server()

    try:
        print('Starting server on port 3000')
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
