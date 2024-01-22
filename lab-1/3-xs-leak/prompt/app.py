from flask import Flask, render_template, request, make_response

import string, random

app = Flask(__name__)

@app.route('/')
def index():
    payload = request.args.get('payload') or ''

    # Level 0
    # roll = random.randint(1, 6)

    # Level 1
    roll = random.randint(0, 256)

    # Level 2
    # roll = "".join(random.choices(string.ascii_letters, k=3))

    # Level 3
    # roll = "".join(random.choices(string.ascii_letters + string.digits, k=3))

    res = make_response(render_template('index.html', payload=payload, roll=roll))
    res.headers['Content-Security-Policy'] = "script-src 'none';"

    return res, 200