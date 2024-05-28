from client import (
    create_spotipy_client,
    get_playlist,
    get_playlist_info,
    get_track_info,
)
from utils import get_playlist_history, write_data_files

playlist_id = "2MzJ9ZBgzHHhm6PNE1G9rg"

sp = create_spotipy_client()
playlist = get_playlist(sp, playlist_id)
tracks = get_track_info(sp, playlist)
playlist_stats = get_playlist_info(playlist)
playlist_history = get_playlist_history("data_folder/playlist.ndjson")

playlist_history.append(playlist_stats)
playlist_history = list({d["date"]: d for d in playlist_history}.values())

# Specify the file path for the NDJSON file
ndjson_file_paths = ["playlist.ndjson", "tracks.ndjson"]
objects = [playlist_history, tracks]

# Write the dictionary to the NDJSON file
for p, o in zip(ndjson_file_paths, objects):
    write_data_files(p, o)
