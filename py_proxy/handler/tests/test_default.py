from tornado.web import RequestHandler
from py_proxy.handler import DefaultHandler


def test_should_be_sub_class_tornado_request_handler():
    assert issubclass(DefaultHandler, RequestHandler)
