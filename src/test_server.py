import requests
from cowpy import cow
import json


def test_server_sends_200_response():
    """
    Tests for 200 response from server, establishes connection
    """
    response = requests.get('http://127.0.0.1:3000/')
    assert response.status_code == 200


def test_server_sends_cowsay_href():
    """
    Tests for cowsay endpoint
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
    Tests 404 response for invalid endpoint
    """
    response = requests.get('http://127.0.0.1:3000/monkey')
    assert response.status_code == 404
    assert response.text == '404 Not Found'


def test_server_sends_400_response():
    """
    Tests 400 request for invalid formatted response
    """
    response = requests.get('http://127.0.0.1:3000/cow?message=whatup')
    assert response.status_code == 400


def test_server_cow_get_200_msg():
    """
    Checks for 200 response on correctly formatted query
    """
    response = requests.get('http://127.0.0.1:3000/cow?msg=This is so fumb')
    assert response.status_code == 200


def test_server_cow_get_text():
    """
    Tests text of successful query
    """
    response = requests.get('http://127.0.0.1:3000/cow?msg=This is so fumb.')
    assert response.text[:15] == ' ______________'
    assert response.text == cow.Stimpy().milk('This is so fumb.')


def test_server_post_status_code():
    """
    Tests status code of successful post
    """
    response = requests.post('http://127.0.0.1:3000/cow?msg=This is so fumb')
    assert response.status_code == 200


def test_server_post_text():
    """
    Tests text of successful post
    """
    response = requests.post('http://127.0.0.1:3000/cow?msg=This is so fumb')
    content = {'content': cow.Stimpy().milk('This is so fumb')}
    assert response.text[:15] == '{"content": " _'


def test_server_unsuccessful_post_request():
    """
    Tests status code of unsuccessful post
    """
    response = requests.post('http://127.0.0.1:3000/cow msg=This is so fumb')
    assert response.status_code == 404


def test_server_unsuccessful_post_format():
    """
    Tests status code of improperly formatted post
    """
    response = requests.post('http://127.0.0.1:3000/cow?message=This is so fumb')
    assert response.status_code == 400
