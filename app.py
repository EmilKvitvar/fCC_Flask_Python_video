from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Stavanger, Norge',
        'salary': 'NOK. 20,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bergen, Norge',
        'salary': 'NOK. 25,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'KR. 22,000'
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'Oslo, Norge',
        'salary': 'KR. 30,000'
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html",
                           jobs=JOBS,
                           company_name="Markiga")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
