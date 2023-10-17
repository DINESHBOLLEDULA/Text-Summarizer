from flask import Flask, render_template, request
from preprocess import preprocess_text
from model import generate_summary
from scrape import scrape_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text-summarization', methods=["POST"])
def output():

    if request.method == "POST":
        option=request.form.get('options')
        if option=='url':
            inputurl=request.form['urlinput']
            inputtext=scrape_text(str(inputurl))
        elif option=='document':
            inputfile=request.form["fileinput"]
            print(inputfile)
        else:
            inputtext = request.form["inputtext_"]
            print(inputtext)

        original_text=preprocess_text(inputtext)
        summary=generate_summary(original_text)
    return render_template("output.html", data = {"input": original_text,"summary":summary})

if __name__ == '__main__': # It Allows You to Execute Code When the File Runs as a Script
    app.run(debug=True)

