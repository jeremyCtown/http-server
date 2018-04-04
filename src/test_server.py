import requests
from cowpy import cow
import json


def test_server_sends_200_response():
    response = requests.get('http://127.0.0.1:3000/')
    assert response.status_code == 200


def test_server_sends_cowsay_href():
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
    response = requests.get('http://127.0.0.1:3000/monkey')
    assert response.status_code == 404
    assert response.text == '404 Not Found'


def test_server_sends_400_response():
    response = requests.get('http://127.0.0.1:3000/cow?msg=whatup')
    assert response.status_code == 400


def test_server_cow_get_200_msg():
    response = requests.get('http://127.0.0.1:3000/cow?msg="This is so fumb"')
    assert response.status_code == 200


def test_server_cow_get_text():
    response = requests.get('http://127.0.0.1:3000/cow?msg="This is so fumb"')
    assert response.text[:15] == ' ______________'
    assert response.text == cow.Stimpy().milk('This is so fumb')


def test_server_post_status_code():
    response = requests.post('http://127.0.0.1:3000/cow?msg="This is so fumb"')
    assert response.status_code == 200


def test_server_post_text():
    response = requests.post
    ('http://127.0.0.1:3000/cow?msg="This is so fumb"')
    content = {'content': cow.Stimpy().milk('This is so fumb')}
    assert response.text[:15] == '{"content": " _'
    assert response.text == json.dumps(content)


