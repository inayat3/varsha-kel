# Demonstration ONLY — insecure pattern for learning
from flask import Flask, request

app = Flask(__name__)

@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    
    # ❌ Vulnerable Pattern: unsanitized user input inside HTML
    return f"<h1>Hello {name}</h1>"

if __name__ == "__main__":
    app.run(debug=False)
