<<<<<<< HEAD
import pprint
import sys

import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import simplejson as json
def play():
    r = requests.put('https://api.spotify.com/v1/me/player/play', headers={'Authorization': temp})
def next_song():
    r = requests.post('https://api.spotify.com/v1/me/player/next', headers={'Authorization': temp})
    r = requests.put('https://api.spotify.com/v1/me/player/play', headers={'Authorization': temp})
    print(r.status_code)
def pause():
    r = requests.put('https://api.spotify.com/v1/me/player/pause', headers={'Authorization': temp})
def prev_song():
    r = requests.post('https://api.spotify.com/v1/me/player/next', headers={'Authorization': temp})
    r = requests.put('https://api.spotify.com/v1/me/player/play', headers={'Authorization': temp})
def play_song(name):
    sp = spotipy.Spotify()
    search_result = sp.search(name)
    artist_list = search_result['tracks']['items']
    album = 'album'
    track = artist_list[0]['uri']
    #r = requests.get()
    data = json.dumps(
        {
            'uris': [track]
        }
    )
    r = requests.put('https://api.spotify.com/v1/me/player/play', data=data, headers={'Authorization': temp})

if __name__ == '__main__':
    username = "toomuchsaucehackcu"
    authorization = {'Authorization': 'Basic 5fd9106f4c744e8a80248d2ab3d59a27:5ffe3b9afc7449c48f670c37feb37102'}
    client_id = '5fd9106f4c744e8a80248d2ab3d59a27'
    client_secret = '5ffe3b9afc7449c48f670c37feb37102'
    params = {'client_id': client_id, 'response_type':'code','redirect_uri':'http://localhost:8888/callback', 'scope': 'streaming','show_dialog':True}

    token = util.prompt_for_user_token(username, scope='streaming', client_id='5fd9106f4c744e8a80248d2ab3d59a27',
                                       client_secret='5ffe3b9afc7449c48f670c37feb37102',
                                       redirect_uri='http://localhost:8888/callback')

    temp = 'Bearer ' + token
    choice = input('What would you like to do: ')
    while choice != 'exit':
        if choice == 'play':
            play()
        elif choice == 'next':
            next_song()
        elif choice == 'pause':
            pause()
        elif 'play song' in choice:
            song_choice = choice.replace('play', '').replace('song', '').strip()
            #print(song_choice)
            play_song(song_choice)
        choice = input('What would you like to do: ')
=======
import pprint
import sys

import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import simplejson as json

scope = 'streaming user-read-playback-state user-modify-playback-state'
def play():
    r = requests.put('https://api.spotify.com/v1/me/player/play', headers={'Authorization': temp})
def next_song():
    r = requests.post('https://api.spotify.com/v1/me/player/next', headers={'Authorization': temp})
    r = requests.put('https://api.spotify.com/v1/me/player/play', headers={'Authorization': temp})
def pause():
    r = requests.put('https://api.spotify.com/v1/me/player/pause', headers={'Authorization': temp})
def prev_song():
    r = requests.post('https://api.spotify.com/v1/me/player/next', headers={'Authorization': temp})
    r = requests.put('https://api.spotify.com/v1/me/player/play', headers={'Authorization': temp})
def play_song(name):
    sp = spotipy.Spotify()
    search_result = sp.search(name)
    artist_list = search_result['tracks']['items']
    album = 'album'
    track = artist_list[0]['uri']
    #r = requests.get()
    data = json.dumps(
        {
            'uris': [track]
        }
    )
    r = requests.put('https://api.spotify.com/v1/me/player/play', data=data, headers={'Authorization': temp})
def control_volume(direction, value=1):
    r = requests.get('https://api.spotify.com/v1/me/player', headers={'Authorization': temp})
    device_info = r.json()
    volume = device_info['device']['volume_percent']
    print('cur vol: ', volume)
    if direction == 'down':
        value = int(value) * -1
    volume = int(volume) + int(value)
    print('new vol: ', volume)
    data=json.dumps({'volume': int(volume)})
    print('data: ', data)
    r = requests.put('https://api.spotify.com/v1/me/player/volume', params={'volume_percent': volume}, headers={'Authorization': temp})
    r = requests.put('https://api.spotify.com/v1/me/player/play', headers={'Authorization': temp})
    print(r.content)
def change_device(new_device):
    r = requests.get('https://api.spotify.com/v1/me/player/devices', headers={'Authorization': temp})
    devices = r.json()['devices']
    device_to_be =''
    for device in devices:
        print(device['name'])
        if new_device.lower() in device['name'].lower():
            device_to_be = device['id']
    data = {'device_ids':[device_to_be],'play':True}
    r = requests.put('https://api.spotify.com/v1/me/player', data=data, headers={'Authorization': temp})
    r = requests.put('https://api.spotify.com/v1/me/player/play', headers={'Authorization': temp})
if __name__ == '__main__':
    username = "toomuchsaucehackcu"
    authorization = {'Authorization': 'Basic 5fd9106f4c744e8a80248d2ab3d59a27:5ffe3b9afc7449c48f670c37feb37102'}
    client_id = '5fd9106f4c744e8a80248d2ab3d59a27'
    client_secret = '5ffe3b9afc7449c48f670c37feb37102'
    params = {'client_id': client_id, 'response_type':'code','redirect_uri':'http://localhost:8888/callback', 'scope': scope,'show_dialog':True}

    token = util.prompt_for_user_token(username, scope=scope, client_id='5fd9106f4c744e8a80248d2ab3d59a27',
                                       client_secret='5ffe3b9afc7449c48f670c37feb37102',
                                       redirect_uri='http://localhost:8888/callback')

    temp = 'Bearer ' + token
    choice = input('What would you like to do: ')
    while choice != 'exit':
        if choice == 'play':
            play()
        elif choice == 'next':
            next_song()
        elif choice == 'pause':
            pause()
        elif 'play song' in choice:
            song_choice = choice.replace('play', '').replace('song', '').strip()
            #print(song_choice)
            play_song(song_choice)
        elif 'volume' in choice:
            choice = choice.replace('volume', '')
            choice.strip()
            choice = choice.split()
            direction = choice[0]
            value = choice[1]
            control_volume(direction, value)
        elif 'change device to' in choice:
            choice = choice.replace('change', '').replace('device', '').replace('to', '')
            choice.strip()
            change_device(choice)

        choice = input('What would you like to do: ')
>>>>>>> 8eac599ec105f1088d53c0aa68f5490cc9311a84
