from quotes import quotes
from flask import Flask, render_template, Response
from random import randint
app = Flask(__name__)


def get_quote(template):
    quote = quotes[randint(0, 10000) % len(quotes)]
    split_quote = quote.split(" - ")
    split_attribution = split_quote[1].split(",")
    return render_template(template, person=split_attribution[0], quote=split_quote[0], attribution=", ".join(split_quote[1:]))


@app.route('/', methods=['GET'])
def show_quote_pretty():
    return get_quote("quotable.j2")


@app.route('/', methods=['POST'])
def show_quote():
    return Response(get_quote("quotable_json.j2"), mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
