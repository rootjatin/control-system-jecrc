from flask import Flask, jsonify, request
import sympy as sp 
from z3 import *
s = sp.symbols("s")
t = sp.symbols("t", positive=True)
# initialize our Flask application
# initialize our Flask application
# initialize our Flask application
app= Flask(__name__)
@app.route("/message", methods=["POST"])
def message():
    posted_data = request.get_json()
    name = posted_data['equation']
    fff1=eval(name)
    #fff=sp.parsing.sympy_parser.parse_expr(name)
    ttt=sp.inverse_laplace_transform(fff1,s,t).evalf().simplify()
    return jsonify(str(ttt))
#  main thread of execution to start the server


