import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up the Spotipy client
scope = "user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Retrieve song currently playing and its id
current_song = sp.currently_playing()
song_id = current_song["item"]["id"]

# Retrieve audio analysis
audio_analysis = sp.audio_analysis(song_id)

# Retreive volume values for each segment
segments = audio_analysis["segments"]
segment_loudness = [segments["volume_start"] for segment in segments]
