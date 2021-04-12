from flask import Flask, render_template, request
# from flask import request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("base.html")

@app.route('/', methods =["GET", "POST"])
def login():
    if request.method == "POST":
        Name = request.form['fname']
        # LastName = request.form.get('lname')
        SearchNews = request.form.get('News')

        message = "{} have searched for ".format(Name) + SearchNews
        # if SearchNews == '':
        #     return (render_template('base.html',message = "Nothing"))
        return message
    return render_template("base.html")

if __name__ == "__main__":
    app.run()