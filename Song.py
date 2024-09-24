import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('watr-fluid-10149.mp3')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    stop_playback = int(
      input("Press 2 anytime to pause playback and go back to the menu: "))
    if stop_playback == 2 :
      pause()
      return
    else:
        continue
      

while True:
  os.system('clear')

  print("🎵 MyPOD Music Player")

  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  userInput = input()
  if userInput == "1":
    play()
  elif userInput == "2":
    break
  else:
    continue