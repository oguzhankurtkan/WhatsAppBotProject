from selenium import webdriver
import requests

with open ("text.txt", "r", encoding="utf-8") as text:
    textlist = list()
    message = text.read()
    # To make it read each line separately
    textlist = message.split("\n")

print (textlist)