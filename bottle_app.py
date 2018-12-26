
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug,static_file

def htmlify(head,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                %s
            </head>
            <body>
            %s
            </body>
        </html>

    """ % (head,text)
    return page

def index():
    head = """ <meta charset="UTF-8">
                <link rel="stylesheet" href="./static/style1.css"/>
                <img class="center" src="./static/logo.png" alt="logo" widht="500px" height="450px">
                <link rel="shortcut icon" href="./static/logo.png" type="img/x-icon">
                <title>Tarantino</title>"""
    text = """<p class="q"><i>Television Actor, Producer, Film Actor, Director, Screenwriter, Actor (1963–)</i></p>
                <br>
                <div class="topnav">
                <a class="active" href="index.html">Home</a>
                <a href="about.html">About</a>
                <a href="films.html">Films</a>
                </div>
                <img src="./static/tarantino1.jpg" title="Quentin Tarantino" alt="Tarantino" width="auto" height="auto"> """
    return htmlify(head,text)

def static_file_callback(filename):
	return static_file(filename ,root='./')


route('/', 'GET', index)
route('/static/<filename>' , 'GET' , static_file_callback)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
