from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def indexpage():
    return render_template('Index.html')


@app.route('/Services')
def services():
    return render_template('Services.html')


@app.route('/Collaborate')
def collaborate():
    return render_template('Collaborate.html')


if __name__ == '__main__':
    app.run(debug=True)
