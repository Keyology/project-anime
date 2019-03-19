from flask import Flask
from jikanpy import Jikan
app = Flask(__name__)
jikan = Jikan()

@app.route('/')
def home():
    return "<h1>Anime recomendations</h1>"

@app.route('/my-anime-user/<name>')
def my_anime_username(name):
    
    # get profile info, same as above
    my_anime_user = jikan.user(username=name, request='profile')

if __name__ == "__main__":
    app.run()