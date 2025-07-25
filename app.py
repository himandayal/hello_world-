from flask import Flask, render_template, request

app = Flask(__name__)

DEFAULT_MATRIX = [
    ("E1 Climate Change", 4, 3),
    ("E2 Pollution", 3, 3),
    ("E3 Water & Marine Resources", 2, 2),
    ("E4 Biodiversity & Ecosystems", 3, 3),
    ("E5 Resource Use & Circular Economy", 4, 3),
    ("S1 Own Workforce", 3, 2),
    ("S2 Workers in the Value Chain", 4, 3),
    ("S3 Affected Communities", 3, 3),
    ("S4 Consumers and End Users", 2, 2),
    ("G1 Governance, Business Conduct", 4, 4),
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        company = {
            "name": request.form.get("name"),
            "industry": request.form.get("industry"),
            "country": request.form.get("country"),
            "scope": request.form.get("scope"),
            "stakeholders": request.form.get("stakeholders"),
            "impacts": request.form.get("impacts"),
        }
        return render_template("report.html", company=company, matrix=DEFAULT_MATRIX)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
