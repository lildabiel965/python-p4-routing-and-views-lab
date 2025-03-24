import io
import sys

from server.app import app
import pytest

@pytest.fixture
def client():
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Python Operations with Flask Routing and Views' in response.data

def test_print_string_route(client):
    """Test the print string route."""
    test_string = "Hello, World!"
    response = client.get(f'/print/{test_string}')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_count_route(client):
    """Test the count route."""
    response = client.get('/count/5')
    assert response.status_code == 200
    assert b'0<br>1<br>2<br>3<br>4<br>5' in response.data

def test_math_route(client):
    """Test the math route for addition."""
    response = client.get('/math/3/+/2')  # Fixed the URL by removing the space
    assert response.status_code == 200
    assert b'5' in response.data

def test_math_subtract(client):
    """Test the math route for subtraction."""
    response = client.get('/math/5/-/3')
    assert response.status_code == 200
    assert b'2' in response.data

def test_math_multiply(client):
    """Test the math route for multiplication."""
    response = client.get('/math/4/*/2')
    assert response.status_code == 200
    assert b'8' in response.data

def test_math_divide(client):
    """Test the math route for division."""
    response = client.get('/math/8/div/2')
    assert response.status_code == 200
    assert b'4.0' in response.data

def test_math_modulo(client):
    """Test the math route for modulo."""
    response = client.get('/math/5/%/2')
    assert response.status_code == 200
    assert b'1' in response.data

def test_math_invalid(client):
    """Test the math route for invalid operation."""
    response = client.get('/math/5/invalid/2')
    assert response.status_code == 200
    assert b'Invalid operation' in response.data
