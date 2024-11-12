from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDZvOWd2ZGJlc3JiY2lvcGhlcHZ6ZXIwcHByeWlhc3F2OHFiNTQ5dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Cij37iSqbvzEpLgZmN/giphy.webp" width=300>'

correct_guess = random.randint(0, 9)
print(correct_guess)

@app.route("/<int:number>")
def guess(number):
    if number == correct_guess:
        return '<h1 style="background-color: green; color: white">You found me!</h1>' \
                '<img src="https://media0.giphy.com/media/kiBcwEXegBTACmVOnE/giphy.webp?cid=790b76116leyw01aa3w6g4it50pv236n8428o1cfkgpepemv&ep=v1_gifs_search&rid=giphy.webp&ct=g" width="300"/>'

    elif  number < correct_guess:
        return '<h1 style="background-color: red; color: white">You guessed too low!</h1>' \
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTFrdTZtZ3lyZXd5dGRiZWYxaXBmZnBweXJtZ2w1eTdqcHFpbTJ6MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/11Xc3nOtJcb8Aw/giphy.webp" width=300/>'
    else:
        return '<h1 style="background-color: purple; color:white">You guessed too high!</h1>' \
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWEwZXhrOW43cXRta252bDRsbTF3MmNvZDNnbWtnZjd6cm4wNDhqZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zu8DrkFiuz8JO/200.webp" width=300/>'



if __name__ == '__main__':
    app.run(debug=True)

