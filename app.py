from flask import Flask
from jikanpy import Jikan
from flask import jsonify
app = Flask(__name__)
jikan = Jikan()

@app.route('/')
def home():
    return "<h1>Anime recomendations</h1>"

@app.route('/my-anime-user', methods=["GET"])
def my_anime_username():
    
    # get profile info, same as above
    my_anime_user = jikan.user(username="king_key", request='profile')
    response = jsonify(my_anime_user)
    return response

if __name__ == "__main__":
    app.run()