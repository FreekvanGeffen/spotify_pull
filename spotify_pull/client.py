"""Facilities to interact with the `Spotify` API."""

import datetime
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def create_spotipy_client() -> spotipy:
    """Create a Spotipy client.

    Returns
    -------
        Spotipy client

    """
    return spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        )
    )


def get_playlist(sp: spotipy, playlist_id: str) -> dict:
    """Fetch all playlist data.

    Args:
    ----
        sp: Spotipy client
        playlist_id: Spotify playlist ID

    Returns:
    -------
        Spotify playlist object

    """
    return sp.playlist(playlist_id)


def get_playlist_info(playlist: dict) -> dict:
    """Get playlist info from playlist dictionary.

    Args:
    ----
        playlist: Playlist dictionary

    Returns:
    -------
        Playlist info

    """
    playlist_info = {
        "name": playlist["name"],
        "description": playlist["description"],
        "followers": playlist["followers"]["total"],
        "numbers": playlist["tracks"]["total"],
        "url": playlist["external_urls"]["spotify"],
        "date": str(datetime.datetime.now(tz=datetime.timezone.utc).date()),
        "image": playlist["images"][0]["url"],
    }
    return playlist_info


def milliseconds_to_mm_ss(milliseconds: str) -> str:
    """Convert milliseconds to mm:ss."""
    total_seconds = milliseconds / 1000
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)

    # Format the result as mm:ss
    return f"{minutes:02}:{seconds:02}"


def get_track_info(sp: spotipy, playlist: dict) -> list[dict]:
    """Get tracks info from playlist dictionary.

    Args:
    ----
        sp: Spotipy client
        playlist: Playlist dictionary

    Returns:
    -------
        Tracks info

    """
    tracks = list(playlist["tracks"]["items"])
    track_info = []

    # Fetch all tracks in the playlist
    while "tracks" in playlist and playlist["tracks"]["next"]:
        playlist = sp.next(playlist["tracks"])
        if "items" in playlist:
            tracks += list(playlist["items"])

    # Select interesting track details
    for track in tracks:
        track_details = {
            "name": track["track"]["name"],
            "artist": track["track"]["artists"][0]["name"],
            "album": track["track"]["album"]["name"],
            "release_date": track["track"]["album"]["release_date"],
            "duration": milliseconds_to_mm_ss(track["track"]["duration_ms"]),
            "added_by": track["added_by"]["id"],
            "added_at": str(track["added_at"])[:10],
            "url": track["track"]["external_urls"]["spotify"],
            "image": track["track"]["album"]["images"][0]["url"],
        }
        track_info.append(track_details)

    return track_info
