"""Phalanx AI Dashboard — Flask application with dark mode toggle."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():
    """Render the main dashboard page."""
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
