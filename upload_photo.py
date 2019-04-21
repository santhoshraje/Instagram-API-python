#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
from InstagramAPI import InstagramAPI
from random import randint
import os

username = ""
password = ""
photocaption = "Comment Amen if you love God!\n.\n#jesus #love #christian #christianity #amen #christianblogger #christianlife #christianmom #christiangirl #christianliving #christianwoman #faith #grace #truth #choosejoy #Godslove #GodlovesYou #BibleVerse"
InstagramAPI = InstagramAPI(username, password)
InstagramAPI.login()

q = 1
while q:
 i = randint(0, 1000)
 photo_path = '/home/user/Pictures/' + str(i) + '.jpg'

 if os.path.exists(photo_path):
  caption = photocaption
  try:
    InstagramAPI.uploadPhoto(photo_path, caption=caption)
  except RuntimeError:
    print("Corrupted file detected. File has been deleted.")
    os.remove(photo_path)
    continue
  q = 0
  print(photo_path + " has been successfully uploaded.")
  os.remove(photo_path)
 else:
  continue

