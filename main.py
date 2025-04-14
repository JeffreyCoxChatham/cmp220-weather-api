from http.server import  HTTPServer
from WeatherDataRequestHandler import WeatherDataRequestHandler

def run(server_class=HTTPServer, handler_class=WeatherDataRequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()