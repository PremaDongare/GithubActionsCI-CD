from flask import Flask, request, jsonify
from src.math_operations import add, sub, mul  # import mul

app = Flask(__name__)

@app.route("/", methods=["GET"])
def calculate():
    """
    Example: 
    https://your-app-url/?op=add&a=5&b=3
    https://your-app-url/?op=sub&a=10&b=4
    https://your-app-url/?op=mul&a=6&b=7
    """
    op = request.args.get("op")
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    if op == "add":
        result = add(a, b)
    elif op == "sub":
        result = sub(a, b)
    elif op == "mul":  # handle multiplication
        result = mul(a, b)
    else:
        return jsonify({"error": "Invalid operation. Use 'add', 'sub', or 'mul'."}), 400

    return jsonify({
        "operation": op,
        "a": a,
        "b": b,
        "result": result
    })
