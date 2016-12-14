import sys
import os
import subprocess
import spotipy
import pprint
import spotipy.util as util
import secret
# import app
# a = app.App()
# username = a.username = 

username = "1271115372"
scope = 'user-top-read user-library-read playlist-modify-private playlist-modify playlist-modify-public playlist-read-private user-read-email user-read-private user-read-birthdate'
token = util.prompt_for_user_token(username, scope, secret.SPOTIPY_CLIENT_ID, secret.SPOTIPY_CLIENT_SECRET, secret.SPOTIPY_REDIRECT_URI)

def user_playlists():
	dict = {}
	if token:
	    sp = spotipy.Spotify(auth=token)
	    playlist = sp.user_playlists(username, limit=50, offset=0)
	    main_list = playlist['items']
	    for item in main_list:
	    	dict[item['name']]= item['id']
	return dict

def playlist_track_list(playlist_id):
	track_id_list = []
	if token:
	    sp = spotipy.Spotify(auth=token)
	    results = sp.user_playlist_tracks(username, playlist_id)
	    tracks_list = results['items']
	    for item in tracks_list:
	    	track_id_list.append(item['track']['id'])
	return track_id_list
	print track_id_list

def track_bpm(track_id, run_type):
	list = []
	track_as_list = []
	track_as_list.append(track_id)
	# print track_as_list
	if token:
	    sp = spotipy.Spotify(auth=token)
	    audio_features = sp.audio_features(track_as_list)
	    if run_type[1] == 1:
	    	for features in audio_features:
	    		bpm = features['tempo']
	    		print bpm
	    		if bpm > 200:
	    			return track_id
	    			print track_id
	    		else:
	    			None
	    elif run_type[1] == 2:
	    	for features in audio_features:
	    		bpm = features['tempo']
	    		# print bpm
	    		if 80 < bpm > 100:
	    			return track_id
	    			print track_id
	    		else:
	    			None
	    elif run_type[1] == 3:
	    	for features in audio_features:
	    		bpm = features['tempo']
	    		# print bpm
	    		if 80 < bpm > 100:
	    			return track_id
	    			print track_id
	    		else:
	    			None
	    elif run_type[1] == 4:
	    	for features in audio_features:
	    		bpm = features['tempo']
	    		# print bpm
	    		if 80 < bpm > 100:
	    			return track_id
	    			print track_id
	    		else:
	    			None	    				  	
	  	else: 
	  		None
def create_playlist(playlist_name):
	if token:
	    sp = spotipy.Spotify(auth=token)
	    sp.trace = False
	    playlists = sp.user_playlist_create(username, playlist_name)
	    playlist_parse = playlists[u'uri'].split(":")
	    playlist_id = playlist_parse[4]
	    print """
	Great! A new playlist, "%s" has been added to your Spotify account!
	""" % (playlist_name)
	    return playlist_id

	else:
	    print("Can't get token for", username)
	    return None

def playlist_tracks(username, playlist_id):
	if token:
	    sp = spotipy.Spotify(auth=token)
	    results = sp.user_playlist_tracks(username, playlist_id)
	    print results


def playlist_add(playlist_id, track_ids):
	if token:
		sp = spotipy.Spotify(auth=token)
    	sp.trace = False
    	results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
# else:
#     print("Can't get token for", username)







 