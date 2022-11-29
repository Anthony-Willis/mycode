#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app= Flask(__name__)


limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per day", "2 per hour"]
)

@app.route("/slow")
@limiter.limit("1 per day")
def slow():
    return "Get out and go find some fresh POWDER.Go hit the slopes now because you won't see this message again today."

powdata= [{
    "name": "Lindsey Vonn",
    "skills": [
        "Skiing",
        "Wicked Jumps",
        "super human strength & agility"
              ]
             }]

@app.route("/")
def index():
    # jsonify returns legal JSON
    return jsonify(powdata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

