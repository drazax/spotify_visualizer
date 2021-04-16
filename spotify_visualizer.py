#!/usr/bin/python3

import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

if __name__ == '__main__':
    spotify_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

