from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import requests
from PIL import Image
from selenium.webdriver.common.keys import Keys
import requests
import random



obt = Options()
obt.add_experimental_option("debuggerAddress", "localhost:9876")
driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\Music\\chromedriver.exe", chrome_options=obt)

def tiktok():
    driver.switch_to_frame(driver.find_element_by_xpath(
        '//*[@id="main"]/div[2]/div/iframe'))

    i = 0
    while True:
        i += 1
        print("making it again:"+str(i))

        print("making a new video...")
        os.system('python tiktok.py')
        sleep(50)
        element = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div[1]/div/input')

        element.send_keys("C:\\Users\\User\\Documents\\makeedit\\Thoughts! #fyp #fact #theory #interesting.mp4")

        sleep(10)

        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[7]/div[2]/button').click()

        sleep(5)
        try:

            driver.find_element_by_xpath(
                '//*[@id="portal-container"]/div/div/div[1]/div[2]').click()
        except:
            driver.get("https://www.tiktok.com/upload?lang=en")
            sleep(20)
            driver.switch_to_frame(driver.find_element_by_xpath(
                '//*[@id="main"]/div[2]/div/iframe'))
            sleep(10)
tiktok()