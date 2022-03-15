from py_proxy.handler import DefaultHandler
from tornado.ioloop import IOLoop
from tornado.web import Application


def main():
    app = Application(
        handlers=[
            (r'.*', DefaultHandler)
        ]
    )
    app.listen(8080)
    IOLoop.current().start()
