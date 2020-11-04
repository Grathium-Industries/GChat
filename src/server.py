import http.server
import socketserver
import urllib
from urllib.parse import urlparse
from urllib.parse import parse_qs
import glob

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sending an '200 OK' response
        self.send_response(200)

        # Setting the header
        self.send_header("Content-type", "text/html")

        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()

        html = rf("src/headers.html")
        html += displayVR(toRender)

        # HTML closing
        html += rf("src/footer.html")

        # webpage imports
        html += "<style>" + rf("src/style.css") + "</style>"
        html += "<script>" + rf("src/script.js") + "</script>"

        # Writing the HTML contents with UTF-8
        self.wfile.write(bytes(html, "utf8"))
        return

def rf(filename):
    return open(filename, "r").read()

exec(rf("src/display.py"))

# arg 1 is server port
def startServer(PORT):
    # Create an object of the above class
    handler_object = MyHttpRequestHandler

    my_server = socketserver.TCPServer(("", PORT), handler_object)

    # Star the server
    print("Started VR Server on :", PORT)
    my_server.serve_forever()


# entry point
print("File to Render:")
toRender = str(input())

startServer(8080)