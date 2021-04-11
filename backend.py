from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/WebPage.html/', methods=['post', 'get'])
def WebPage():
    message = ''
    if request.method == 'POST':
        Name = request.form.get('Name')
        LastName = request.form.get('LastName')
        SearchNews = request.form.get('Enter your Name')

        message = "You have searched for "+SearchNews
        if SearchNews == '' :
            return (render_template('base.html',message = "Nothing"))

        return(render_template('WebPage.html', message = message))

if __name__ == "__main__":
    app.run(debug=True)