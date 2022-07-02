from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/backend', methods=['POST'])
def backend():
    text = request.form['texts']
    return text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8010)
