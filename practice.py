
import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util
SPOTIPY_CLIENT_ID = "e8ad653d5f55408da763a67be6cae1f4"
SPOTIPY_CLIENT_SECRET = "7455adaa6f634130985ba2e0bdde11c8"
SPOTIPY_REDIRECT_URI = "https://www.spotify.com/us/account/overview/"
username = "1271115372"
playlist_name = "Test Playlist"
scope = 'user-top-read user-library-read playlist-modify-private playlist-modify playlist-modify-public playlist-read-private user-read-email user-read-private user-read-birthdate'
token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
track_ids = []




# if token:
#     sp = spotipy.Spotify(auth=token)
#     sp.trace = False
#     ranges = ['short_term', 'medium_term', 'long_term']
#     for range in ranges:
#         print "range:", range
#         results = sp.current_user_top_tracks(time_range=range, limit=50)
#         print results


# if token:
#     sp = spotipy.Spotify(auth=token)
#     sp.trace = False
#     results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)


# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     i = 0
#     results_list = results['items']
#     while i < 20:
#     	track_ids.append(results_list[i]['track']['uri'].split(":")[2]) 
#     	i = i + 1
#     print track_ids
  
    # track_ids= results['items'][0]['track']['uri']

# def playlist_tracks(playlist_id):
	# if token:
	#     sp = spotipy.Spotify(auth=token)
	#     results = sp.user_playlist_tracks(username, playlist_id)
# 	    tracks_list = results['items']
# 	    for item in tracks_list:
# 	    	print item['track']['id']

def track_bpm(track_id, run_type):
	list = []
	if token:
	    sp = spotipy.Spotify(auth=token)
	    song_list = sp.audio_features(track_id)
	    if run_type[1] == 1:
	    	for item in song_list:

	    		if 5.0 < item['tempo']:
	    			track_id.append
	    			print list[0]
	    		else:
	    			None
	   #  elif run_type[1] == 2:
	   #  	for item in song_list:
	   #  		if 160 < item['tempo'] <= 170:
	   #  			list.append(track_id)
	   #  		else:
	   #  			None
	   #  elif run_type[1] == 3:
	   #  	for item in song_list:
	   #  		if 150 < item['tempo'] <= 160:
	   #  			list.append(track_id)
	   #  		else:
	   #  			None
	   #  elif run_type[1] == 4:
	   #  	for item in song_list:
	   #  		if 120 < item['tempo'] <=150:
	   #  			list.append(track_id)
	   #  		else:
	   #  			None
	  	else: 
	  		return list
	else:
	    print("Can't get token for", username)
	    
track_bpm(['7x4JKksWaTbumTlo5iu63M'], ["fast mix", 1, '0h82R74CZnRxz6TCQ6JFbo'])


# def user_playlist_names():
# 	if token:
# 	    sp = spotipy.Spotify(auth=token)
# 	    playlists = sp.user_playlists(username, limit=50, offset=0)
# 	    i = 0
# 	    while i < 20:
# 	  		print playlists['items'][i]['name']
# 	  		i = i + 1
# 	else:
# 	    print("Can't get token for", username)

# def user_playlists_ids():
# 	if token:
# 	    sp = spotipy.Spotify(auth=token)
# 	    playlists = sp.user_playlists(username, limit=50, offset=0)
# 	    i = 0
# 	    while i < 20:
# 	  		print playlists['items'][i]['id']
# 	  		i = i + 1
# 	else:
# 	    print("Can't get token for", username)	

# def user_playlists():
# 	dict = {}
# 	if token:
# 	    sp = spotipy.Spotify(auth=token)
# 	    playlist = sp.user_playlists(username, limit=50, offset=0)
# 	    i = 0
# 	    while i < 20:
# 	  		# print playlist['items'][i]['name']
# 	  		dict[playlist['items'][i]['name']] = playlist['items'][i]['id']
# 			i = i + 1
# 	return dict
# 	else:
# 	    print("Can't get token for", username)











