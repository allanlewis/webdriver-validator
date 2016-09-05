import logging
from pprint import pprint

import click
import requests

logging.basicConfig(level=logging.DEBUG)


@click.command()
@click.option(
    '--host', metavar='HOSTNAME', required=True,
    help='The hostname or IP address of the server to validate')
@click.option(
    '--port', metavar='PORT', type=int, required=True,
    help='The port number on which the WebDriver server is running')
def validate(host, port):
    session = requests.Session()
    session_url = 'http://{}:{}/session'.format(host, port)
    post_data = {'desiredCapabilities': {}}
    response = session.post(session_url, json=post_data)
    response.raise_for_status()
    pprint(response.json())

if __name__ == '__main__':
    validate()
