"""
Unit tests for Magic Decision Maker application
"""
import pytest
from app import app, RESPONSES, COLORS


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Test that the main page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Magic Decision Maker' in response.data


def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'


def test_decision_endpoint(client):
    """Test the decision API endpoint"""
    response = client.get('/api/decision')
    assert response.status_code == 200
    data = response.get_json()

    # Check that response contains required fields
    assert 'response' in data
    assert 'color' in data

    # Check that response is one of the valid responses
    assert data['response'] in RESPONSES

    # Check that color is one of the valid colors
    assert data['color'] in COLORS


def test_decision_endpoint_randomness(client):
    """Test that the decision endpoint returns different results"""
    responses = set()
    colors = set()

    # Make multiple requests
    for _ in range(20):
        response = client.get('/api/decision')
        data = response.get_json()
        responses.add(data['response'])
        colors.add(data['color'])

    # With 20 requests, we should get at least some variety
    # (there's a tiny chance this could fail with true randomness, but very unlikely)
    assert len(responses) > 1, "Expected some variety in responses"
    assert len(colors) > 1, "Expected some variety in colors"


def test_responses_list():
    """Test that RESPONSES list is properly configured"""
    assert len(RESPONSES) > 0
    assert all(isinstance(r, str) for r in RESPONSES)
    assert all(len(r) > 0 for r in RESPONSES)


def test_colors_list():
    """Test that COLORS list is properly configured"""
    assert len(COLORS) > 0
    assert all(isinstance(c, str) for c in COLORS)
    # Check that colors are in hex format
    assert all(c.startswith('#') for c in COLORS)
    assert all(len(c) == 7 for c in COLORS)


def test_404_error(client):
    """Test that invalid routes return 404"""
    response = client.get('/nonexistent-route')
    assert response.status_code == 404
