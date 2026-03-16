from flask import Flask, render_template, request, jsonify, send_from_directory
from logic.calculator_logic import calculate

app = Flask(
    __name__, 
    template_folder='../frontend/html', 
    static_folder='../frontend'
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/styles/<path:filename>")
def serve_styles(filename):
    return send_from_directory('../frontend/styles', filename)

@app.route("/scripts/<path:filename>")
def serve_scripts(filename):
    return send_from_directory('../frontend/scripts', filename)

@app.route("/calculate", methods=["POST"])
def perform_calculation():
    """
    API endpoint that accepts JSON data and returns a JSON result.
    Example input: {"a": 10, "b": 5, "op": "+"}
    Example output: {"result": 15}
    """
    data = request.json
    try:
        a = float(data.get("a", 0))
        b = float(data.get("b", 0))
        op = data.get("op", "+")
        
        # BUSINESS LOGIC is handled by the backend module
        result = calculate(a, op, b)
        
        return jsonify({
            "status": "success",
            "result": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
