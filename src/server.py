from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from cowpy import cow

ren_msg = cow.Ren().milk('400 Error!?! You steenkin eeeediot')
stimpy = cow.Stimpy()
errr_msg = cow.Cheese().milk('I am Errr.. You can query this site using /cow?msg=text as an endpoint ')


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        """
        handles GET requests
        """
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
        elif parsed_path.path == '/cowsay':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(errr_msg.encode('utf8'))
        elif parsed_path.path == '/cow':
            try:
                msg = parsed_qs['msg'][0]
                
            except (KeyError, json.decoder.JSONDecodeError):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(ren_msg.encode('utf8'))
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(stimpy.milk(msg).encode('utf8'))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        """
        handles POST requests
        """
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/cow':
            try:
                content_length = int(self.headers['Content-Length'])
                body = json.loads(self.rfile.read(content_length).decode('utf8'))
                
            except (KeyError, json.decoder.JSONDecodeError):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(ren_msg.encode('utf8'))
                return
     
            self.send_response(200)
            self.send_headers('Content-Type', 'application/json')
            self.end_headers()
            msg_json = stimpy.milk(body['msg'])
            self.wfile.write(json.dumps({'content': msg_json}).encode('utf8'))

        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

 
def create_server():
    """
    creates server instance
    """
    return HTTPServer(('127.0.0.1', 3000), SimpleHTTPRequestHandler)


def run_forever():
    """
    keeps server from shutting down after request complete
    """
    server = create_server()

    try:
        print('Starting server on port 3000')
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
