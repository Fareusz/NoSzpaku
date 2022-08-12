from dotenv import load_dotenv
import os
import requests
import sys
import json
import spotipy
import webbrowser
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

username = input('Podaj nazwe uzytkownika: ')
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)
devices = spotifyObject.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
deviceID = devices['devices'][0]['id']

while True:
    track = spotifyObject.current_user_playing_track()
    print(json.dumps(track, sort_keys=True, indent=4))
    print()
    artists = track['item']['artists']
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']
    print(artists)
    if artist !="":
        print("Currently playing " + artist + " - " + track)
    for x in artists:
        if 'Szpaku' == artists[0]['name']:
            print('ta słuchamy szpaka jak co')
            trackSelectionList = ['spotify:track:7JprB3m3eZ7nVMsyBkitJ9']
            spotifyObject.start_playback(deviceID, None,
                                             trackSelectionList)
    user = spotifyObject.current_user()
    displayName = user['display_name']
    follower = user['followers']['total']
    time.sleep(5)