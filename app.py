from flask import Flask, render_template
import os

app = Flask(__name__)
counter_file = "counter.txt"

@app.route("/")
def home():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            f.write("0")
    with open(counter_file, "r+") as f:
        count = int(f.read()) + 1
        f.seek(0)
        f.write(str(count))
    return render_template("index.html", counter=count)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
