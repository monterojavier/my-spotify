from flask import Flask
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

app = Flask(__name__)
CORS(app)

scope = 'user-top-read'
range = 'long_term'

# Spotify oauth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_ID,
                                               client_secret=config.client_SECRET,
                                               redirect_uri="http://localhost:3000/",
                                               scope=scope))

# Top Artist Long Term API Route
@app.route('/top_artist')
def top_artist():
  top5 = []
  results = sp.current_user_top_artists(time_range=range, limit=5)

  for idx, item in enumerate(results['items']):
    artist_info = {"name": item["name"],
                   "image":item["images"][2],
                   "url":item["external_urls"]["spotify"]
                   }
    top5.append(artist_info)

  return {"top5": top5}


if __name__ == "__main__":
  app.run(debug=True)
