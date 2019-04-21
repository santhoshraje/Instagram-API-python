#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
from InstagramAPI import InstagramAPI
from random import randint
import os
import telegram

username = " "
password = " "
photo_caption = " "
remove_after_upload = False
continue_loop = 1
directory_path = " "
# id for the telegram bot that you want to use
chat_bot = telegram.Bot(token=' ')
# id of the telegram account you want to send the message to
chat_id = 0

#login to instagram
InstagramAPI = InstagramAPI(username, password)
InstagramAPI.login()

while continue_loop:
 # generate a random integer from 0 to 1000
 i = randint(0, 1000)
 # directory_path is full of photos that are named from 0 to 1000
 photo_path = directory_path + str(i) + '.jpg'
 # if the path exists
 if os.path.exists(photo_path):
  # upload the photo
  try:
    InstagramAPI.uploadPhoto(photo_path, caption = photo_caption)
  # check for corrupted files
  except RuntimeError:
    print("Corrupted file detected. File has been deleted.")
    # delete the corrupted file
    os.remove(photo_path)
    continue
  # break out of the loop
  continue_loop = 0
  # print success message
  print(photo_path + " has been successfully uploaded.")
  # if user wants the photo to be deleted after uploading
  if remove_after_upload:
    os.remove(photo_path)
 # if photo upload is not successful
 else:
  continue

