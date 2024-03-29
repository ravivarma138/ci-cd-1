"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/page1">GITHUB</a>' in response.data
    assert b'<a class="nav-link" href="/page2">DOCKER</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Python-Flask</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI-CD</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data


def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About Page" in response.data


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/github")
    assert response.status_code == 200
    assert b"Page 1" in response.data


def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/dockerproj")
    assert response.status_code == 200
    assert b"Page 2" in response.data


def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/python-flask")
    assert response.status_code == 200
    assert b"Page 3" in response.data


def test_request_page4(client):
    """This makes the index page""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"Page 4" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
