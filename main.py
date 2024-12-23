from selenium import webdriver
import requests

with open ("text.txt", "r", encoding="utf-8") as text:
    textlist = list()
    message = text.read()
    # To make it read each line separately
    textlist = message.split("\n")

def start():
    # Using Chrome and 4 seconds wait
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    # Redirect to the URL with get function
    driver.get('https://web.whatsapp.com/')
    input('If you have scanned the QR code, press the enter key.')
    message_are = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    # Online status check and click the message are
    while True:
        message_area.click()

start()