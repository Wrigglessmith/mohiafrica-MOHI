from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to MOHI Africa</h1><p>This is your live website hosted on Render!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
