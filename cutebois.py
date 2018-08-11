from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Artists')
def artists():
    return render_template("artists.html")


@app.route('/Youngface')
def youngface():
    return render_template("Youngface.html")


@app.route('/Shop')
def shop():
    return render_template("shop.html")


@app.route('/Contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
