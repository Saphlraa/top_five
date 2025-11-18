from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simple in-memory storage for submissions
submissions = []
numrequests = 0
UI_dark_mode = False

@app.route("/", methods=["GET", "POST"])
def home():
    global submissions
    global numrequests
    if request.method == "POST":
        # Get the category and top five items from the form
        category = request.form.get("category", "").strip()
        items = [
            request.form.get(f"item{i}", "").strip() for i in range(1, 6)
        ]
        # Validate that all inputs are filled
        if category and all(items):
            submissions.append({"category": category, "five": items})
        return redirect("/")
    numrequests = numrequests + 1
    return render_template("index.html", submissions=submissions)

@app.route("/settings", methods=["GET", "POST"])
def settings():
    global UI_dark_mode
    global numrequests
    if request.method == "POST":
        UI_dark_mode = not UI_dark_mode
        return redirect("/settings")
    numrequests = numrequests + 1
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)

