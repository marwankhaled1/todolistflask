from flask import Flask


app=Flask(__name__)

@app.route('/main')
def index():
    return 'Hello, World'

@app.route('/hello')
def hello():
    return 'Hello, Maroo'


if __name__ == "__main__" :
    app.run(debug=True)
