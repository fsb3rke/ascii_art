from os import system
import json

sett_file = open("sett.json", "r").read()
sett_json = json.loads(sett_file)

imagesrc = sett_json["photo"]
grayscaleimagesrc = sett_json["grayscale_photo_OUTPUT"]
asciiimagesrc = sett_json["ascii_photo_OUTPUT"]

firstReqCommand = sett_json["ConvertSett"]["firstReq"]
secondReqCommand = sett_json["ConvertSett"]["secondReq"]


system(f"{firstReqCommand} {imagesrc} {grayscaleimagesrc}") # firstReq
system(f"{secondReqCommand} {grayscaleimagesrc} {asciiimagesrc}")