from selenium import webdriver
import os

driver_path = os.getcwd() + "/python/geckodriver"
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(executable_path=driver_path, options=options)
driver.maximize_window()
driver.get(f'https://zartweety.ir/shot/?id={tweet_id}&theme=ffffff')
e = driver.find_element_by_xpath('//*[@id="contentbox"]')
driver.save_full_page_screenshot(f"{tweet_id}.png")

img = Image.open(f"{tweet_id}.png")
box = (0, 0, 1120, e.size['height'] + 70)
img2 = img.crop(box)
img2.save(f"new_{tweet_id}.png")

tweet_image = open(f"new_{tweet_id}.png", 'rb')
driver.quit()
os.remove(f"{tweet_id}.png")
os.remove(f"new_{tweet_id}.png")
return tweet_image
