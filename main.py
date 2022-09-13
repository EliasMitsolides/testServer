import os
# Flask is a nice tool, among many, for sending things to some sort of 'backend' to be processed
from flask import Flask

# HTML, CSS, and JS are nice. All of them together lets you do cool stuff buuuut you can't have
#   a back end with just that.
# Flask will let me communicate this front-end code and send/retrieve to/from a back-end or be the backend.
# Flask can act as the back-end or how we will communicate with it (if we used a bigger tool for a back-end)
# That kind of "front<->back-end communication" help is considered part of the term 'web framework'
from flask import render_template
# I'm gonna try to use this import to render an image (Kiryu!) saved inside this project
app = Flask(__name__)

KIRYU_IMAGE_PATH = os.path.join('static', 'BigKiryu.png')
app.config['BigKiyru'] = KIRYU_IMAGE_PATH
# app.route is what Flask uses to map URLs to functions
@app.route("/")
def hello_world():
    return "<p>Hello, World@@@@@@@@@@@@@!</p>"


@app.route("/byebye")
def bye_world():
    return "<p>bye, World@@@@@@@@@@@@@!</p>"


# you dont have to say get or post by default, get is the default from browsers to server (here)
@app.route("/youshouldntbehere")
def nogo_world():
    return "<p>McExcuse ME!</p>"


# this img element gets a Kiryu from an image saved inside this project's folder
@app.route("/Kiryu")
def kiryu_local_world():
    # "GET /BigKiryu.png HTTP/1.1" 404
    # full_filename = os.path.join(app.config['BigKiyru'])
    # /\/\ this doesnt work as KIRYU_IMAGE_PATH is already the path we need, we would need this if
    #  Big Kiryu.png was in another folder within the static folder
    full_filename = KIRYU_IMAGE_PATH
    # looks in a directory called 'templates' which we gotta make
    return render_template("index.html", kiryu_image=full_filename)
    #return "<img src=\"../BigKiryu.png\" alt=\"Kiryu\">"


# this img element gets a Kiryu from a URL from outside this project, on the web
@app.route("/BigKiryu")
def kiryu_external_world():
    return "<img src=\"https://www.giantbomb.com/a/uploads/scale_small/1/14876/3065027-4993810116-latest\" " \
           "alt=\"thats a big kiryu\">"


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)