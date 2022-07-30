
from selenium import webdriver
from PIL import Image
from webdriver_manager.firefox import GeckoDriverManager


tweet_id = 1527256533096079361
#tweet_id = 1536672142108069889
driver_path = "/home/me/projects/PHP/ScreenShot/python/geckodriver"
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
#driver = webdriver.Firefox(executable_path=driver_path, options=options)
driver = webdriver.Firefox(
    executable_path=GeckoDriverManager().install(), options=options)
driver.maximize_window()
driver.get(f'https://zartweety.ir/shot/?id={tweet_id}&theme=ffffff')
e = driver.find_element_by_xpath('//*[@id="contentbox"]')
driver.save_full_page_screenshot(f"{tweet_id}.png")

img = Image.open(f"{tweet_id}.png")
box = (0, 0, 1120, e.size['height'] + 70)
img2 = img.crop(box)
img2.save(f"new_{tweet_id}.png")

driver.quit()
