from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# flask --app server.py run --debug
#copy paste that to launch the server in debug mode

# @app.route("/index.html")
# def index():
#     return render_template("index.html")

# @app.route("/works.html")
# def works():
#     return render_template("works.html")

# @app.route("/work.html")
# def work():
#     return render_template("work.html")

# @app.route("/about.html")
# def about():
#     return render_template("about.html")

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

#Dynamic routing below, hard-coded routing above

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'Email: {email}\nSubject: {subject}\nMessage: \n{message}\n\n')

def write_to_csv(data):
    with open('database.csv', mode='a', newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return "Something went wrong. Try again later."
