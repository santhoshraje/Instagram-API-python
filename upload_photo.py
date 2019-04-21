#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
from InstagramAPI import InstagramAPI
from random import randint
import os
import telegram

# username for the account
username = " "
# password for the account
password = " "
# caption for the photo
photo_caption = " "
# if the user wants photo to be deleted after upload (removes possibility of double posting)
remove_after_upload = False
# condition that is used to continue the loop
continue_loop = 1
# full path to folder containing photos to be uploaded
directory_path = " "
# id for the telegram bot that you want to use
chat_bot = telegram.Bot(token=' ')
# id of the telegram account you want to send the message to
chat_id = 0
# if the user wants telegram log messages
telegram_logging = False

# function to count the number of photos remaining in the directory
def count_photos(path):
  count = 0
  for root,subdir,listfilename in os.walk(path):
    for filename in listfilename:
        count += 1
  return count

# login to instagram
InstagramAPI = InstagramAPI(username, password)
InstagramAPI.login()

# main program loop
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
  # if user wants telegram message sent after each post
  if telegram_logging:
    count = count_photos(directory_path)
    chat_bot.send_message(chat_id=chat_id, text= " ")
 # if photo upload is not successful
 else:
  continue
