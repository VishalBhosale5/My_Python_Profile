from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def profile():
    return "<!DOCTYPE html><html lang='en'><head><title>Vishal Bhosales IMAD profile</title> <meta " \
           "charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'></head><body> <div " \
           "class='container text-center full-height'><div class='row content'><div class='col-sm-4 sidenav'> <div " \
           "class='thumbnail'><img src='v.jpg' alt='Lights' style='width:10%' /> </div><h2 align='center'><b>Vishal " \
           "Bhosale</b></h2> <p align='center'>Student,<br>SIT,<br>pune.</p> </div><div class='col-sm-8 " \
           "text-left'><h3>About me</h3><p>I'm a Science geek who loves to learn science and " \
           "technology.</p><hr><h3>Education</h3><p>I'M a Computer Engineering Student in pune " \
           "university.</p><hr><h3>Experience</h3><p>still learning</p><hr><h3>A cool thing I've done " \
           "recently</h3><p>made this profile<p><hr> <a href='https://twitter.com/share' class='twitter-share-button' " \
           "data-size='large' data-text='I just built #myfirstapp with #imad! @HasuraEd. Check it out here - ' " \
           "data-show-count='false'>Tweet</a><script async src='//platform.twitter.com/widgets.js' " \
           "charset='utf-8'></script> <iframe id='fb_share' src='' width='84' height='28' " \
           "style='border:none;overflow:hidden' scrolling='no' frameborder='0' allowTransparency='true'></iframe> " \
           "<script>var current_url = window.location.href;document.getElementById(" \
           "'fb_share').src='https://www.facebook.com/plugins/share_button.php?href='+current_url+'&layout" \
           "=button_count&size=large&mobile_iframe=true&appId&width=84&height='28'; " \
           "</script></div></div></div><footer class='container-fluid text-center footer'>Passion and perseverance " \
           "will takes you the places where no degree can.</footer></body></html> "

if __name__ == "__main__":
    app.run()
