import functions
import app
a = app.App()

def add_tracks():
	print """
	You can add tracks from any one of your existing playlists. The tracks that best fit your run mix will be added automatically. Here is a list of your current playlists: 
	
	"""
	# functions.user.playlists returns a dictionary of all playlists. Key is playlist name, and value is playlist id.
	a.all_user_playlists = functions.user_playlists()
	for key in a.all_user_playlists:
		if key != a.run_type:
			print key
		else:
			None


	playlist_source_request = raw_input("""
	Please type the playlist name to add tracks from that playlist:  """)
	
	if playlist_source_request in a.all_user_playlists:
		print """
	OK, '%s'. Tracks from the '%s' playlist that best fit your run are being added to your run mix. Please wait...""" % (playlist_source_request, playlist_source_request)

		a.playlist_source_id = a.all_user_playlists[playlist_source_request]
# a.tracks_to_playlist_All returns a list of all playlist tracks
		a.tracks_to_playlist_All = functions.playlist_track_list(a.playlist_source_id)
	# print a.tracks_to_playlist_All
# This loop returns a list of all tracks that have the users requested run type BPM:
		a.tracks_to_playlist_BPM = create_BPM_list(a.tracks_to_playlist_All)

		if a.tracks_to_playlist_BPM:
			functions.playlist_add(a.playlist_destination, a.tracks_to_playlist_BPM)
			print """
	Songs from the '%s' playlist that match your run criteria have been added to your new run playlist!""" % (playlist_source_request)
			return add_more_tracks()
		else:
			response = raw_input("""
	There are no songs in this playlist that fit your requested run criteria. Type 'y' to select another playlist, 'exit' to exit or any other key to return to main menu.   """)
			if response.lower() == 'y':
				return add_tracks()
			elif response.lower() == 'exit':
				return exit()
			else:
				return main()

	else: 
		print """
	%s is not an exiting user playlist.""" % playlist_source_request
		return add_tracks()

def add_more_tracks():
	return_add_tracks = raw_input("""
	Would you like to add tracks from another playlist? If Yes type 'y'. If you would like to return to the main menu, type 'm'. To exit, type 'exit':   """)

	if return_add_tracks.lower() == "y":
		return add_tracks()
	elif return_add_tracks.lower() == "m":
		return main()
	elif return_add_tracks.lower() =="exit":
		return exit()
	else:
		print """
	'%s' is not a valid request""" % return_add_tracks
		return add_more_tracks()
	

def create_playlist():
	run_type = []
	run_distance = raw_input("""
	Please type a number (1-4) that best coorelates with the distance of your run.

	1: Less than 1 mile 
	2: 5K (3.2 miles)
	3: Half marathon (13 miles) 
	4: Marathon (26 miles)

   	""")
   	playlist_name = ""
	if run_distance == "1":
		run_type = ["Short Distance Mix", 1]
	elif run_distance == "2":
		run_type = ["5k Mix", 2]
	elif run_distance == "3":
		run_type = ["Half Marathon Mix", 3]
	elif run_distance == "4":
		run_type = ["Marathon Mix", 4]	
	
	if run_type: 
		playlist_name = run_type[0]
		playlist_id = functions.create_playlist(playlist_name)
		run_type.append(playlist_id)
		return run_type
	else:
		print """
	"%s" is not a valid option.""" % (run_distance)
		return create_playlist()

def create_BPM_list(tracks_list):
	list =[]
	for songs in tracks_list:
		filtered_bpm_item = functions.track_bpm(songs, a.run_type)
		if filtered_bpm_item != None:
			list.append(filtered_bpm_item)
	return list		

def exit():
	print """

	Thanks for playing. Enjoy your new run mix!
	"""

def main():
	
	# if a.username:
	print """
	Welcome to the runner's Spotify playlist creater!"""

	
	a.run_type = create_playlist()
	a.playlist_destination = a.run_type[2]

	add_tracks()
	# else:
	# 	a.username = raw_input = """
	# Please enter your Spotify User ID or "device username". You can find this by logging into your Spotify account, going to the Account section, and clicking 'Set device password'."""
	# 	return main()
	
		 
main()





	