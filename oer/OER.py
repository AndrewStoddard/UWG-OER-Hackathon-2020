from web import OERHTTPHandler
from http.server import HTTPServer


def main():
    print("Starting Web server...")
    try:
        HTTPServer(('', 8001), OERHTTPHandler).serve_forever()
    except KeyboardInterrupt:
        print("Exitting...")


if __name__ == '__main__':
    main()
