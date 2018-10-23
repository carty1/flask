from flask import Flask


app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Welcome to your homepage!'

@app.route('/about')
def about():
    return 'This is a basic Flask made website'

@app.route('/htmlexample')
def htmlExample():
    return '<h1> Look at this header</h1> <p>HTML is great!</p>'


if __name__ == "__main__":
    app.run(debug=True)































