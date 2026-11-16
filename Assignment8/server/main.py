from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Computing Lab 8</title>
        <style>
            body {
                font-family: Arial;
                background: #eef2ff;
                text-align: center;
                padding: 80px;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 12px;
                max-width: 600px;
                margin: auto;
            }
            h1 { color: #2563eb; }
        </style>
    </head>
    <body>
        <div class="container">
          <h1>Cloud Computing Lab 8</h1>
          <h2>Application Version 1</h2>
          <p>Successfully deployed using Microsoft Azure.</p>
          <p>This application demonstrates PaaS.</p>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
