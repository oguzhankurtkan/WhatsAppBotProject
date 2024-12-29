from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


with open ("text.txt", "r", encoding="utf-8") as text:
    textlist = list()
    message = text.read()
    # To make it read each line separately
    textlist = message.split("\n")

def start():
    flag = False
    # Using Chrome and 4 seconds wait
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    # Redirect to the URL with get function
    driver.get('https://web.whatsapp.com/')
    input('If you have scanned the QR code, press the enter key.')
    message_area = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')


    # Online status check and click the message are
    while True:
        message_area.click()
        # Retrieving WhatsApp online status information
        wa_source = driver.page_source
        soup = bs(wa_source, 'lxml')
        search = soup.find_all('div', {'class': ['_2Gdma', '_2amHe']})
        try:
            online = search[0].span.text
            print(online)
            if (online in ['online', 'çevrimiçi']) and flag == False:
                print ('online test')
                msgToSend = textlist[random.randint(0, len(textlist)-1)]
                message_area.send_keys(msgToSend)
                message_area.send_keys(Keys.ENTER)
                # Main point: Not spam.
                flag = True
            elif online not in ['online', 'çevrimiçi']:
                print('Offline!')
                flag = False
        except:
            print('Offline!')
            flag = False

        time.sleep(5)



start()