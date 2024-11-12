from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello World! Hell yeah</h1>' \
            '<p>This is a paragraph. </p>' \
            '<img src="https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*" width=200/>'


@app.route("/bye")
@make_bold
def say_bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name}. You are {number} years old"


if __name__ == "__main__":
    app.run(port=8000, debug=True)