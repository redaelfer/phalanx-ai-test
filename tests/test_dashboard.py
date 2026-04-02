"""Tests for the Phalanx AI Dashboard — dark mode toggle feature."""

import pytest

from app import app as flask_app


@pytest.fixture
def client():
    """Create a Flask test client."""
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as c:
        yield c


class TestDashboardRoute:
    """GET / should return the dashboard page."""

    def test_status_200(self, client):
        resp = client.get("/")
        assert resp.status_code == 200

    def test_contains_dashboard_heading(self, client):
        html = client.get("/").data.decode()
        assert "<h1>Dashboard</h1>" in html

    def test_contains_nav(self, client):
        html = client.get("/").data.decode()
        assert "Phalanx AI" in html


class TestDarkModeToggle:
    """The dashboard must include a working dark-mode toggle."""

    def test_toggle_button_present(self, client):
        html = client.get("/").data.decode()
        assert 'id="dark-mode-toggle"' in html

    def test_toggle_has_aria_label(self, client):
        html = client.get("/").data.decode()
        assert 'aria-label="Toggle dark mode"' in html

    def test_data_theme_attribute(self, client):
        html = client.get("/").data.decode()
        assert 'data-theme="light"' in html

    def test_sun_icon_present(self, client):
        html = client.get("/").data.decode()
        assert "☀️" in html

    def test_moon_icon_present(self, client):
        html = client.get("/").data.decode()
        assert "🌙" in html

    def test_darkmode_js_linked(self, client):
        html = client.get("/").data.decode()
        assert "darkmode.js" in html

    def test_stylesheet_linked(self, client):
        html = client.get("/").data.decode()
        assert "style.css" in html


class TestStaticAssets:
    """Static CSS and JS files should be served."""

    def test_css_serves(self, client):
        resp = client.get("/static/css/style.css")
        assert resp.status_code == 200
        assert b"data-theme" in resp.data

    def test_js_serves(self, client):
        resp = client.get("/static/js/darkmode.js")
        assert resp.status_code == 200
        assert b"dark-mode-toggle" in resp.data
