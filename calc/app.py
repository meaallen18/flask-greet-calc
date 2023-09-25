from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = add(a,b)
    return f"The sum of {a} and {b} is {result}"

@app.route('/sub')
def subtraction():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return f"The difference of {a} and {b} is {result}"

@app.route('/mult')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return f"The product of {a} and {b} is {result}"

@app.route('/div')
def division():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return f"The quotient of {a} and {b} is {result}"

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def calculate(operator):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[operator](a,b)

    return str(result)

   

