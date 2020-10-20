import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def fibonacci():
    a = 0
    b = 1
    limit = 50
    found = 0
    show = "0, "
    while limit > found:
        a, b = b, a + b
        show += f'{a}, ' if found != 49 else f'{a}.'
        found += 1
    return show


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8001))
    app.run(host="0.0.0.0", port=port)
