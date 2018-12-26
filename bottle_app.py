
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
    return htmlify("My lovely website",
                   "This is going to be an awesome website, when it is finished.")

route('/', 'GET', index)

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
