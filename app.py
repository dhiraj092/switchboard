from flask import Flask, request, jsonify, render_template
from query_data import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/query", methods=["POST"])
def query():
    user_query = request.json.get("query", "").strip()
    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        response = generate_response(user_query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
