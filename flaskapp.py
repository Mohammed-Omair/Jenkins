from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f'Mohammed Omair Mohiuddin 1002165593'

if __name__ == '__main__':
    app.run(debug=True)
