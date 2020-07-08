from flask import Flask
app = Flask(__name__)

@app.route("/")
def sayHello():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def greetName(name):
    return "Hi " + name + "!"

@app.route("/repeat/<int:times>/<phrase>")
def repeatPhrase(times, phrase):
    show = ""
    for i in range(times):
        show += phrase + "\n"
    return show

@app.errorhandler(404)
def showErrorPage(e):
    return "Sorry! No response. Try Again"

if __name__ == "__main__":
    app.run(debug=True)