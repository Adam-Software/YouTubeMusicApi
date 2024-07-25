from Melody_CLI import Player
import time
import os
import pygame

pygame.init()
pygame.mixer.init()

player = Player()
searchQuery = "female vocale drum and base"

def Search(searchQuery):
    youtubeSearchResults, videoIDS = player.searchSong(searchQuery)
    desiredVideo = int(6)
    audioFile = player.downloadSong(videoIDS[desiredVideo])
    return audioFile

if __name__ == "__main__":
    print("Search:", searchQuery)
    audioFile = Search(searchQuery)
    print("PlaySong:", audioFile)
    player.playSong(audioFile)
    time.sleep(5)
    "Set volume from 0.0 to 1.0"
    player.setvolumeSong(0.1)
    time.sleep(3)
    "Add volume from 0.0 to 1.0"
    player.addvolumeSong(0.9)
    time.sleep(2)
    #player.stopSong(audioFile)
