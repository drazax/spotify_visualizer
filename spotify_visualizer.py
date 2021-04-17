#!/usr/bin/python3

import argparse
import os
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

def debug(*aMessage):
    for message in aMessage:
        print(message)

def loadConfig(aConfigFile):
    with open(aConfigFile, 'r') as read_from:
        for line in read_from:
            environment_variable_key, environment_variable_value = line.split(maxsplit=1)
            os.environ[environment_variable_key] = environment_variable_value.rstrip()

def addArguments(aArgumentParser):
    aArgumentParser.add_argument('-c', '--config', nargs='?', default='config.cfg', help='Specifies a new config file')

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    addArguments(argument_parser)
    arguments = argument_parser.parse_args()
    loadConfig(arguments.config)

    spotify_client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-read-private'), client_credentials_manager=SpotifyClientCredentials())
    playlists = spotify_client.user_playlists(os.environ['SPOTIPY_USER'], limit=20)
    debug(playlists)
