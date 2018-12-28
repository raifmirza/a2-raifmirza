
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug,static_file,request
from hashlib import sha256

def create_hash(password):  # Hashing function is adopted from: https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

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
                <a href="/comment">Comment</a>
                </div>
                <img src="./static/tarantino1.jpg" title="Quentin Tarantino" alt="Tarantino" width="auto" height="auto"> """
    return htmlify(head,text)

def about():
    head = """ <meta charset="UTF-8">
        <link rel="stylesheet" href="./static/style2.css"/>
        <img class="center" src="./static/logo.png" alt="logo" widht="500px" height="450px">
        <link rel="shortcut icon" href="./static/logo.png" type="img/x-icon">
        <title>Tarantino</title>"""
    text = """<p class="q"><i>Television Actor, Producer, Film Actor, Director, Screenwriter, Actor (1963–)</i></p>
                <br>
                <div class="topnav">
                <a href="/">Home</a>
                <a class="active"href="/about">About</a>
                <a href="/films">Films</a>
                <a href="/comment">Comment</a>
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

def films():
    head = """ <meta charset="UTF-8">
<link rel="stylesheet" href="./static/style3.css"/>
  <img class="center" src="./static/logo.png" alt="logo" widht="500px" height="450px">
  <link rel="shortcut icon" href="./static/logo.png" type="img/x-icon">

<title>Tarantino</title>"""
    text ="""<button onclick="topFunction()" id="myBtn" title="Go to top">Top</button>

<p class="q"><i>Television Actor, Producer, Film Actor, Director, Screenwriter, Actor (1963–)</i></p>
<br>
<div class="topnav">
  <a href="/">Home</a>
  <a href="/about">About</a>
  <a class="active" href="/films">Films</a>
  <a href="/comment">Comment</a>
</div>
<script>
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
</script>
<h2>Some of Him Top Films as a Director</h2>
<table align="center">
  <tr>
    <td rowspan="3"><img src="./static/reservoir.jpg" title="Reservoir Dogs(1992)" alt="film poster" width="300px" height="350px"></td>
    <td><img src="./static/imdb_icon.png"  title="IMDB" alt="imdb icon" width="30px" height="30px"> 8.3</td>
  </tr>

  <tr>
  <td><img src="./static/rotten.png"  title="Rotten Tomatoes" alt="rotten tomatoes icon" width="30px" height="30px">%91</td>
  </tr>
  <tr>
    <td><a href="https://www.imdb.com/title/tt0105236/?ref_=nm_flmg_wr_25"><strong>About:</strong></a>After a simple jewelry heist goes terribly wrong, the surviving criminals begin to suspect that one of them is a police informant. </td>
  </tr>
</table>
<table align="center">
  <tr>
    <td rowspan="3"><img src="./static/pulp.jpg" title="Pulp Fiction(1994)" alt="film poster" width="300px" height="350px"></td>
    <td><img src="./static/imdb_icon.png"  title="IMDB" alt="imdb icon" width="30px" height="30px">8.9</td>
  </tr>
  <tr>
  <td><img src="./static/rotten.png"  title="Rotten Tomatoes" alt="rotten tomatoes icon" width="30px" height="30px">%94</td>
  </tr>
  <tr>
    <td><a href="https://www.imdb.com/title/tt0110912/?ref_=nm_flmg_wr_23"><strong>About:</strong></a>The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.  </td>
  </tr>
</table>
<table align="center">
  <tr>
    <td rowspan="3"><img src="./static/kill1.jpg" title="Kill Bill Vol. 1(2003)" alt="film poster" width="300px" height="350px"></td>
    <td><img src="./static/imdb_icon.png"  title="IMDB" alt="imdb icon" width="30px" height="30px">8.1</td>
  </tr>
  <tr>
  <td><img src="./static/rotten.png"  title="Rotten Tomatoes" alt="rotten tomatoes icon" width="30px" height="30px">%85</td>
  </tr>
  <tr>
    <td><a href="https://www.imdb.com/title/tt0266697/?ref_=nm_flmg_wr_15"><strong>About:</strong></a>After awakening from a four-year coma, a former assassin wreaks vengeance on the team of assassins who betrayed her. </td>
  </tr>
</table>
<table align="center">
  <tr>
    <td rowspan="3"><img src="./static/kill2.jpg" title="Kill Bill Vol. 2(2004)" alt="film poster" width="300px" height="350px"></td>
    <td><img src="./static/imdb_icon.png"  title="IMDB" alt="imdb icon" width="30px" height="30px">8.0</td>
  </tr>
  <tr>
  <td><img src="./static/rotten.png"  title="Rotten Tomatoes" alt="rotten tomatoes icon" width="30px" height="30px">%84</td>
  </tr>
  <tr>
    <td><a href="https://www.imdb.com/title/tt0378194/?ref_=nm_flmg_wr_14"><strong>About:</strong></a>The Bride continues her quest of vengeance against her former boss and lover Bill, the reclusive bouncer Budd, and the treacherous, one-eyed Elle.  </td>
  </tr>
</table>
<table align="center">
  <tr>
    <td rowspan="3"><img src="./static/ing.jpg" title="Inglourious Basterds (2009)" alt="film poster" width="300px" height="350px"></td>
    <td><img src="./static/imdb_icon.png"  title="IMDB" alt="imdb icon" width="30px" height="30px">8.3</td>
  </tr>
  <tr>
  <td><img src="./static/rotten.png"  title="Rotten Tomatoes" alt="rotten tomatoes icon" width="30px" height="30px">%88</td>
  </tr>
  <tr>
    <td><a href="https://www.imdb.com/title/tt0361748/?ref_=nm_flmg_dr_6"><strong>About:</strong></a>In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner's vengeful plans for the same. </td>
  </tr>
</table>
<table align="center">
  <tr>
    <td rowspan="3"><img src="./static/django.jpg" title="Django Unchained (2012)" alt="film poster" width="300px" height="350px"></td>
    <td><img src="./static/imdb_icon.png"  title="IMDB" alt="imdb icon" width="30px" height="30px">8.4</td>
  </tr>
  <tr>
  <td><img src="./static/rotten.png"  title="Rotten Tomatoes" alt="rotten tomatoes icon" width="30px" height="30px">%86</td>
  </tr>
  <tr>
    <td><a href="https://www.imdb.com/title/tt1853728/?ref_=nm_flmg_wr_7"><strong>About:</strong></a>With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner. </td>
  </tr>
</table>
<table align="center">
  <tr>
    <td rowspan="3"><img src="./static/hate.jpg" title="The Hateful Eight (2015)" alt="film poster" width="300px" height="350px"></td>
    <td><img src="./static/imdb_icon.png"  title="IMDB" alt="imdb icon" width="30px" height="30px">7.8</td>
  </tr>
  <tr>
  <td><img src="./static/rotten.png"  title="Rotten Tomatoes" alt="rotten tomatoes icon" width="30px" height="30px">%74</td>
  </tr>
  <tr>
    <td><a href="https://www.imdb.com/title/tt3460252/?ref_=nm_flmg_wr_5"><strong>About:</strong></a>In the dead of a Wyoming winter, a bounty hunter and his prisoner find shelter in a cabin currently inhabited by a collection of nefarious characters. </td>
  </tr>
</table>
<p>Reference from <a href="https://www.rottentomatoes.com/">Rotten Tomatoes</a> and <a href="https://www.imdb.com/?ref_=nv_home">Imdb</a></p>"""
    return htmlify(head,text)


def html(text, text2):
    comment_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
<link rel="stylesheet" href="./static/style4.css"/>
<img class="center" src="./static/logo.png" alt="logo" widht="500px" height="450px">
<link rel="shortcut icon" href="./static/logo.png" type="img/x-icon">
<title>Tarantino</title>
</head>
<body>
  <p class="q"><i>Television Actor, Producer, Film Actor, Director, Screenwriter, Actor (1963–)</i></p>
              <br>
              <div class="topnav">
              <a href="/">Home</a>
              <a href="/about">About</a>
              <a href="/films">Films</a>
              <a class="active" href="/comment">Comment</a>
              </div>
  <div>
    %s
    <form class="form" method="post" action="/comment">
      <label for="name">Name: </label>
      <br>
      <input type="text" rows="8" id="name" name="name" placeholder="Name and Surname">
      <br>
      <label for="key">Key: </label>
      <br>
      <input type="password" rows="8" id="key" name="pass" placeholder="Password">
      <br>
      <label for="message">Your message: </label>
      <br>
      <textarea name="message" id="message" rows="8" cols="54" placeholder="Add Comment"></textarea>
      <br>
      <input type="radio" name="grade" value="good" checked> Good
      <input type="radio" name="grade" value="neutral"> Neutral
      <input type="radio" name="grade" value="bad"> Bad<br><br>
      <input type="submit" name="submit" value="Submit">
      <input type="reset"><br>

    </form>
    <form class="form" method="GET" action="/comment2">
    <input type="submit" name="delete" value="Delete" onclick="hello">
    </form>
  </div>
    <div  style="display: inline-block; width: 400px">
    <p style='font-size: 30px; padding-bottom: 10px'>Previous Comments:</p>
    %s
    </div>
</body>
</html>
    ''' % (text2,text)
    return comment_page




debug(mode=True)
user_text = ""
list_for_smth = []
hash1 = "d883b52bdc5bcf4ad89a34da2a6b74c2765610f406a564ce8080868fd4befeb8"

def get_comments(list):
    global user_text
    global hash
    try:
        request.POST["name"]
        user_name = request.POST["name"]
        try:
            request.POST["message"]
            user_comment = request.POST["message"]
            if(user_comment != ""):
                request.POST["grade"]
                check = request.POST["grade"]
                if check == "good":
                    say = "GOOD"
                if check == "neutral":
                    say = "Neutral"
                if check == "bad":
                    say = "Bad"
                try:
                    request.POST["pass"]
                    pw = request.POST["pass"]
                    newHash = create_hash(pw)
                    if(newHash == hash1):

                        list.append("<p style='font-size: 25px; font-weight: 5; padding-bottom: 7px'>"+user_name+": "+user_comment+"   "+say+"</p>")
                        user_text = "<p style='font-size: 30px; font-weight: 5'>Your comment has been added</p>"
                    else:
                        user_text = "<p style='font-size: 30px; font-weight: 5'>Wrong password, try again!</p>"
                except:
                    print("Something go wrong")
            else:
                user_text = "<p style='font-size: 30px; font-weight: 5'>You should give a comment first.</p>"
        except:
            print("Something go wrong")
    except:
        print("Something go wrong")

def com_message():
    global list_for_smth
    global user_text
    get_comments(list_for_smth)
    thello = ""
    for i in list_for_smth:
        thello += i
    return html(thello, user_text)

def delete():
    global list_for_smth
    global user_text
    get_comments(list_for_smth)
    thello = ""
    if len(list_for_smth) == 0:
        user_text = """
                    <br>
                    <div class="alert">
                    <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                    <strong>There is nothing to delete!</strong>
                    </div>"""
    else:
        list_for_smth.pop()
        user_text = "<p style='font-size: 30px; font-weight: 5'>Your comment has been deleted!</p>"
        for i in list_for_smth:
            thello += i
    return html(thello,user_text)



def static_file_callback(filename):
	return static_file(filename ,root='./')



route('/', 'GET', index)
route('/about','GET',about)
route('/films','GET',films)
route('/comment', 'GET', com_message)
route('/comment', 'POST', com_message)
route('/comment2', 'GET', delete)
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
