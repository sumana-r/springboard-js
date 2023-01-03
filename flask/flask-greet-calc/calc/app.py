from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_route():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    sum = str(operations.add(a,b))
    
    return f" <p>The sum of two numbers is: {sum}</p>"

@app.route('/sub', methods=['GET'])
def sub_route():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    diff = str(operations.sub(a,b))
    
    return f" <p>The difference is: {diff}</p>"

@app.route('/mult', methods=['GET'])
def mult_route():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    prod = str(operations.mult(a,b))
    
    return f" <p>The product is: {prod}</p>"

@app.route('/div', methods=['GET'])
def div_route():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    div = str(operations.div(a,b))
    
    return f" <p>The product is: {div}</p>"
    
arithm_op = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div,
}
@app.route("/math/<arithmetic>")
def math(arithmetic):
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    math = str(arithm_op[arithmetic](a,b))
    return math 