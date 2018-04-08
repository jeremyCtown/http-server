import requests
from cowpy import cow
import json as json


def test_server_sends_200_response():
    """
    Tests is server sends 200 response
    """
    response = requests.get('http://127.0.0.1:3000/')
    assert response.status_code == 200


def test_server_sends_cowsay_href():
    """
    tests if cowsay endpoint sends correct text
    """
    response = requests.get('http://127.0.0.1:3000/')
    assert response.text == """
            <!DOCTYPE html>
<html>
<head>
    <title> cowsay </title>
</head>
<body>
    <header>
        <nav>
        <ul>
            <li><a href="/cowsay">cowsay</a></li>
        </ul>
        </nav>
    <header>
    <main>
        <!-- project description -->
    </main>
</body>
</html>
"""


def test_server_sends_404_response():
    """
    tests that 404 response works for no endpoint
    """
    response = requests.get('http://127.0.0.1:3000/monkey')
    assert response.status_code == 404
    assert response.text == '404 Not Found'


def test_server_sends_400_response():
    """
    Tests if query improperly formatted
    """
    response = requests.get('http://127.0.0.1:3000/cow?msg=')
    assert response.status_code == 400


def test_server_cow_get_200_msg():
    """
    Tests proper query sends 200 response
    """
    response = requests.get('http://127.0.0.1:3000/cow?msg="This is so fumb"')
    assert response.status_code == 200


def test_server_cow_get_text():
    """
    Tests query sends correct text
    """
    response = requests.get('http://127.0.0.1:3000/cow?msg=This is so fumb')
    assert response.text[:15] == ' ______________'
    assert 'This is so fumb' in response.text


def test_server_post_status_code():
    """
    Tests post sends correct status code
    """
    response = requests.post('http://127.0.0.1:3000/cow', json={'msg': 'is this thing on?'})
    assert response.status_code == 200


def test_server_post_text():
    """
    Tests post response is correct
    """
    response = requests.post('http://127.0.0.1:3000/cow', json={'msg': 'This is so fumb'})
    content = {'content': cow.Stimpy().milk('"This is so fumb"')}
    assert response.text[:15] == '{"content": " _'
    assert response.text == json.dumps(content)
