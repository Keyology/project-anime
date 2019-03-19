from flask import Flask
from jikanpy import Jikan
from flask import jsonify
from flask import request
app = Flask(__name__)
jikan = Jikan()

@app.route('/')
def home():
    return "<h1>Anime recomendations</h1>"

@app.route('/my-anime-user', methods=["GET", "POST"])
def my_anime_username():
    print("route has been hit")
    # get profile info, same as above
    name_param = request.args.get('name')
    print("This is name params", name_param)
    name_param = str(name_param)
    my_anime_user = jikan.user(username=name_param, request='profile')
    response = jsonify(my_anime_user)
    print("This is the response",response)
    return response

if __name__ == "__main__":
    app.run(debug=True, port=8000)