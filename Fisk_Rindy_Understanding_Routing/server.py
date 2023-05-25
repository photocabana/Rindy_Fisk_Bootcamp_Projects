from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"


# @app.route('/repeat/<int:num>/<string:word>')
# def repeat_word(num, word):
#     return f"{word * num}"


@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''
    
    for i in range(0,num):
        output += f"<p>{word}</p>"
        
    return output


@app.route("/<null>")
def fail_route(null):
        
    return "Sorry! No response. Try again."


if __name__=="__main__":
    app.run(debug=True)

