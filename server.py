"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

MEANNESS =['not awesome', "not terrific", "unneato"]

@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
            <html>
              <head>
                <title>Hi There!</title>
              </head>
              <body>
                <p>Hi! This is the home page.</p>
                <a href="/hello">This is a link to the hellopage</a>
              </body>
            </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    # return """
    # <!doctype html>
    # <html>
    #   <head>
    #     <title>Hi There!</title>
    #   </head>
    #   <body>
    #     <h1>Hi There!</h1>
    #     <form action="/greet">
    #       What's your name? <input type="text" name="person"><br>
    #       What compliment would you like?
    #       <select name="choose_compliment">
    #       <option value="pretty">Pretty</option>
    #       <option value="awesome">Awesome</option>
    #       <option value="pythonic">Pythonic</option>
    #       </select><br>
    #       <input type="submit" value="Submit">
    #     </form>
    #   </body>
    # </html>
    # """

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person"><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("choose_compliment")
    #compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def insult_person():
    """Insult user"""

    player = request.args.get("person")
    insult = choice(MEANNESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """.format(player=player, insult=insult)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
