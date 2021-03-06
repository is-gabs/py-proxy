from tornado.ioloop import IOLoop
from tornado.web import Application

from proxy.handler import DefaultHandler


def main():
    app = Application(
        handlers=[
            (r'.*', DefaultHandler)
        ]
    )
    app.listen(8080)
    IOLoop.current().start()
