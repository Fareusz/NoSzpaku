from dotenv import load_dotenv
import os
import requests
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import time


load_dotenv()

CLIENT_ID = os.getenv('ENV_CLIENT_ID')
CLIENT_SECRET = os.getenv('ENV_CLIENT_SECRET')
AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'authorization_code',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'response_type': 'code',
    'redirect_uri': '127.0.0.1'
})

username = input('Please enter your username: ')
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)
devices = spotifyObject.devices()
print('You successfully signed in with spotify.')
deviceID = devices['devices'][0]['name']
print('Script is working on device: ' + deviceID)

while True:
    track = spotifyObject.current_user_playing_track()
    if track is None:
        print('You are not listening to anything')
        time.sleep(2)
        continue
    artists = track['item']['artists']

    artist = track['item']['artists'][0]['name']
    track = track['item']['name']
    if artist !="":
        print("Currently playing " + artist + " - " + track)
    for x in range(len(artists)):
        if artists[x]['name'] == 'Szpaku':
            spotifyObject.next_track()
    time.sleep(1)