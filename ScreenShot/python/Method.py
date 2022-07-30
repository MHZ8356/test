from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import os


def ti(tweet_link):
    data = tweet_link.split('/')
    return data[5]


def csh(tweet_id):
    option = webdriver.ChromeOptions()
    option.headless = True
    option.add_argument('--window-size=1296,1000')
    driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', options=option)
    driver.maximize_window()
    driver.get(f'https://memaili.ir/sc/?id={tweet_id}&theme=ffffff&w=900')
    e = driver.find_element(By.XPATH, '//*[@id="contentbox"]')
    # e = driver.find_element_by_xpath('//*[@id="contentbox"]')
    id = tweet_id.split('?')
    driver.save_screenshot(f"{id[0]}.png")

    img = Image.open(f"{id[0]}.png")
    box = (0, 0, 975, e.size['height'] + 70)
    img2 = img.crop(box)
    img2.save(f"new_{id[0]}.png")

    tweet_image = open(f"new_{id[0]}.png", 'rb')
    driver.quit()
    return tweet_image
    os.remove(f"{id[0]}.png")
    os.remove(f"new_{id[0]}.png")
    return tweet_image
