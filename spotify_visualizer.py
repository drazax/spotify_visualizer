#!/usr/bin/python3

import argparse
import os
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

def debug(aMessage):
    print(aMessage)

def loadConfig(aConfigFile):
    with open(aConfigFile, 'r') as read_from:
        for line in read_from:
            key, value = line.split(maxsplit=1)
            os.environ[key] = value.rstrip()

def addArguments(aArgumentParser):
    aArgumentParser.add_argument('-c', '--config', nargs='?', default='config.cfg', help='Specifies a new config file')

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    addArguments(argument_parser)
    arguments = argument_parser.parse_args()
    loadConfig(arguments.config)

    spotify_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

