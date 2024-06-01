"""Generic helpers."""

import json
import pathlib


def get_playlist_history(path: str) -> list[dict]:
    """Get playlist info history from NDJSON file.

    Args:
    ----
        path: Path to the NDJSON file

    Returns:
    -------
        Playlist info history

    """
    playlist_info_history = []
    if pathlib.Path(path).exists():
        with pathlib.Path(path).open() as f:
            for line in f:
                playlist_info = json.loads(line)
                playlist_info_history.append(playlist_info)
    return playlist_info_history


def write_data_files(path: str, data: dict) -> None:
    """Write data to NDJSON file.

    Args:
    ----
        path: Path to the NDJSON file
        data: Object to write

    """
    if not pathlib.Path("data_folder/").exists():
        pathlib.Path("data_folder/").mkdir(parents=True, exist_ok=True)
    with pathlib.Path("data_folder/" + path).open("w") as f:
        for entry in data:
            json_line = json.dumps(entry)
            f.write(json_line + "\n")
