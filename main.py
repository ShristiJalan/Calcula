from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/operation_result/', methods=['POST'])
def operation_result():
    return (render_template, 'index.html')