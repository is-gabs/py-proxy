import mock
import pytest

from py_proxy import main
from py_proxy.handler import DefaultHandler


@pytest.fixture
def mock_application():
    with mock.patch(
        'py_proxy.Application'
    ) as mocked_class:
        yield mocked_class


@pytest.fixture
def mock_ioloop():
    with mock.patch(
        'py_proxy.IOLoop'
    ) as mocked_class:
        yield mocked_class


def test_should_call_tornado_application(
    mock_application,
    mock_ioloop
):
    main()
    mock_application.assert_called_once_with(
        handlers=[(r'.*', DefaultHandler)]
    )


def test_should_call_app_listen_with_port(
    mock_application,
    mock_ioloop
):
    main()
    mock_application().listen.assert_called_once_with(8080)


def test_should_call_ioloop_current(
    mock_application,
    mock_ioloop
):
    main()
    mock_ioloop.current.assert_called_once()


def test_should_call_ioloop_current_start(
    mock_application,
    mock_ioloop
):
    main()
    mock_ioloop.current().start.assert_called_once()
