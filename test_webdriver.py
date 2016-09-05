from pprint import pprint


def test_create_session(url, session):
    post_data = {'desiredCapabilities': {}}
    response = session.post('{}/session'.format(url), json=post_data)
    response.raise_for_status()
    pprint(response.json())
