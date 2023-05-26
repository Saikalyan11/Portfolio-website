from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def firstpage():
    return render_template('Index.html')


@app.route('/Works')
def nextpage():
    return render_template('Work.html')


if __name__ == '__main__':
    app.run(debug=True)
