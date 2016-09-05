import pytest
import requests


def pytest_addoption(parser):
    parser.addoption('--host')
    parser.addoption('--port', type=int)


@pytest.fixture(scope='session')
def url(request):
    host = request.config.getoption('host')
    port = request.config.getoption('port')
    return 'http://{}:{}'.format(host, port)


@pytest.fixture
def session():
    return requests.Session()
