from flask import *
from flask_sqlalchemy import SQLAlchemy, request
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# branch_name = str(input("Which branch student you want? "))
@app.route("/view_student")
def view_student():
    return render_template("View_Student.html")

@app.route("/extc")
def extc():
    return render_template("extc.html")

@app.route("/it")
def IT():
    return render_template("IT.html")

@app.route("/mech")
def mech():
    return render_template("mech.html")

@app.route("/comps")
def comps():
    return render_template("comps.html")

@app.route("/add_student", methods = ["GET","POST"])
def add_student():
    if request.method == "POST":
        Name = request.form.get("Name")
        Gender = request.form.get("Gender")
        Eng_Year = request.form.get("Eng_Year")
        Branch = request.form.get("Branch")
        Gmail = request.form.get("Gmail")

        with open('ATT.csv', 'a') as readFile:
            fieldnames = ['Name','Gender', 'Eng_Year','Branch', 'Gmail']
            writer = csv.DictWriter(readFile, fieldnames=fieldnames)
            readFile.seek(0, 2)
            if readFile.tell() == 0:
                writer.writeheader()
            writer.writerow({'Name': Name,'Gender':Gender, 'Eng_Year': Eng_Year,'Branch':Branch, 'Gmail': Gmail})

    return render_template("add_student_info.html")

@app.route("/mark_attendance", methods = ["GET","POST"])
def mark_student():
    if request.method == "POST":
        Date = request.form.get("Date")
        Branch = request.form.get("Branch")
        Eng_Year = request.form.get("Eng_Year")
        Roll_No = request.form.get("Roll_No")
        Subjects = request.form.get("Subjects")
        Attendance = request.form.get("Attendance")

        with open('mark.csv', 'a') as readFile:
            fieldnames = ['Date', 'Branch', 'Eng_Year', 'Roll_No', 'Subjects', 'Attendance']
            writer = csv.DictWriter(readFile, fieldnames=fieldnames)
            readFile.seek(0, 2)
            if readFile.tell() == 0:
                writer.writeheader()
            writer.writerow({'Date': Date, 'Branch': Branch, 'Eng_Year': Eng_Year, 'Roll_No': Roll_No, 'Subjects': Subjects, 'Attendance': Attendance})

    return render_template("mark_attendance.html")

@app.route("/analysis")
def Analysis():
    return render_template("analysis.html")

@app.route("/yearwise")
def yearAnalysis():
    return redirect(url_for('static', filename='FY.png'))

@app.route("/monthwise")
def monthAnalysis():
    return redirect(url_for('static', filename='TMSY.png'))

@app.route("/weekwise")
def weekAnalysis():
    return redirect(url_for('static', filename='W1FoY.png'))

@app.route("/subjectwise")
def subAnalysis():
    return redirect(url_for('static', filename='SOM1.png'))



if __name__ == "__main__":
    app.run(debug=True)
