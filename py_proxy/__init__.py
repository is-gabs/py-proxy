from tornado.ioloop import IOLoop
from tornado.web import Application


def main():
    app = Application()
    app.listen(8080)
    IOLoop.current().start()
