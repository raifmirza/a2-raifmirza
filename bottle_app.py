
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
                <a class="active" href="/">Home</a>
                <a href="/about">About</a>
                <a href="/films">Films</a>
                </div>
                <img src="./static/tarantino1.jpg" title="Quentin Tarantino" alt="Tarantino" width="auto" height="auto"> """
    return htmlify(head,text)

def about():
    head = """ <meta charset="UTF-8">
        <link rel="stylesheet" href="./static/style2.css"/>
        <img class="center" src="./static/logo.png" alt="logo" widht="500px" height="450px">
        <link rel="shortcut icon" href="./static/slogo.png" type="img/x-icon">
        <title>Tarantino</title>"""
    text = """<p class="q"><i>Television Actor, Producer, Film Actor, Director, Screenwriter, Actor (1963–)</i></p>
                <br>
                <div class="topnav">
                <a href="/">Home</a>
                <a class="active"href="/about">About</a>
                <a href="/films">Films</a>
                </div>
                <img src="./static/tarantino2.jpg" title="Tarantino" alt="Tarantino" style="float:right;width:700px;height:410px;">
                <h2>Synopsis</h2>
                <p>Born in Tennessee in 1963, Quentin Tarantino moved to California at age 4. His love of movies led to a job in a video store,
                during which time he wrote the scripts for True Romance and Natural Born Killers. Tarantino's directorial debut came
                with 1992's Reservoir Dogs, but he received widespread critical and commercial acclaim with Pulp Fiction (1994),
                for which he won an Academy Award for best screenplay. Subsequent features included Jackie Brown (1997),
                Kill Bill: Vol. 1 (2003) and Vol. 2 (2004) and Grindhouse (2007). Tarantino earned several award nominations
                for Inglourious Basterds (2009) and Django Unchained (2012), the latter garnering him a second Oscar win for best screenplay.
                </p>

                <br>
                <h2>Early Life</h2>
                <p>Quentin Tarantino was born on March 27, 1963, in Knoxville, Tennessee. He is the only child of Connie McHugh, who is part Cherokee
                and part Irish, and actor Tony Tarantino, who left the family before Quentin was born.
                Moving to California at the age of 4, Tarantino developed his love for movies at an early age. One of his earliest memories is of his
                grandmother taking him to see a John Wayne movie. Tarantino also loved storytelling, but he showed his creativity in unusual ways.
                "He wrote me sad Mother's Day stories. He'd always kill me and tell me how bad he felt about it," Connie once told Entertainment Weekly.
                "It was enough to bring a tear to a mother's eye."
                Tarantino loathed school, choosing to spend his time watching movies or reading comics rather than studying. The only subject that
                appealed to him was history. "History was cool and I did well there, because it was kind of like the movies," he told Entertainment Weekly.
                After dropping out of high school, Tarantino worked as an usher at a adult film theater for a time. He also took acting classes. Tarantino
                eventually landed a job at Video Archives in Manhattan Beach, California. There he worked with Roger Avary, who shared his passion for film.
                The two even worked on some script ideas together.
                </p>
                <br>
                <img src="./static/a.jpeg" title="Tarantino" alt="Tarantino" style="float:right;width:700px;height:410px;">

                <h2>Early Films</h2>
                <p>During his time at Video Archives, Tarantino worked on several screenplays, including True Romance and Natural Born Killers. He also landed
                a guest spot on the popular sitcom The Golden Girls, playing an Elvis impersonator. In 1990, Tarantino left Video Archives to work for Cinetel,
                a production company. Through one of the producers there, he was able to get his script for True Romance in the hands of director Tony Scott.
                 Scott liked Tarantino's script, and bought the rights to it.
                 Working with producer Lawrence Bender, Tarantino was able to secure funding for his directorial debut, Reservoir Dogs (1992), for which he
                 had also written the screenplay. Actor Harvey Keitel was impressed when he read the script, saying "I haven't seen characters like these in years."
                  He signed on as an actor and a producer for the project. Other cast members included Michael Madsen, Tim Roth, Chris Penn, Steve Buscemi and Tarantino himself.
                  In 1992, audiences at the Sundance Film Festival were entranced by Reservoir Dogs, Tarantino's ultraviolent crime caper gone wrong. He drew inspiration
                  for the project from such classic heist films as Rififi and City on Fire. The independent film helped make Tarantino one of the most talked-about figures in
                  Hollywood. While not a big hit in the United States, it became a popular title on video and did well overseas.
                </p>
                <p>Reference from <a href="https://www.biography.com/people/quentin-tarantino-9502086">https://www.biography.com/people/quentin-tarantino-9502086</a></p>
                <h2>Films directed by Quentin Tarantino</h2>
                <ul>
                <li>Death Proof
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                  <li>Actor</li>
                </ul>
                </li>

                <li>Django Unchained

                <ul>
                  <img src="./static/tarantino3.jpg" title="Pulp Fiction" alt="pulp fiction scene" style="float:right;width:700px;height:410px;">
                  <li>Director</li>
                  <li>Screenwriter</li>
                  <li>Actor</li>
                </ul>
                </li>

                <li>Four Rooms
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                  <li>Actor</li>
                </ul>
                </li>
                <li>Grindhouse
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                  <li>Actor</li>
                </ul>
                </li>
                <li>The Hateful Eight
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                  <li>Actor</li>
                </ul>
                </li>
                <li>Inglourious Basterds
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                  <li>Actor</li>
                </ul>
                </li>
                <li>Jackie Brown
                <ul>
                  <li>Director</li>

                  <li>Screenwriter</li>
                  <img src="./static/tarantino4.png" title="Pulp Fiction" alt="gimp" style="float:right;width:700px;height:410px;">
                  <li>Actor</li>

                </ul>
                </li>
                <li>Kill Bill: Volume 1
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                </ul>
                </li>
                <li>Kill Bill: Volume 2
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                  <li>Actor</li>
                </ul>
                </li>
                <li>My Best Friend's Birthday
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                  <li>Actor</li>
                </ul>
                </li>
                <li>Once Upon a Time in Hollywood
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                </ul>
                </li>
                <li>Pulp Fiction
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                  <li>Actor</li>
                </ul>
                </li>
                <li>Reservoir Dogs
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                  <li>Actor</li>
                </ul>
                </li>
                <li>Sin City
                <ul>
                  <li>Director</li>
                  <li>Screenwriter</li>
                </ul>
                </li>
                </ul>
                <p>Reference from <a href="https://en.wikipedia.org/wiki/Category:Films_directed_by_Quentin_Tarantino">https://en.wikipedia.org/wiki/Category:Films_directed_by_Quentin_Tarantino</a></p> """
    return htmlify(head,text)

def static_file_callback(filename):
	return static_file(filename ,root='./')


route('/', 'GET', index)
route('/about','GET',about)
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
