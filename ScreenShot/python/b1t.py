from selenium import webdriver


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
option = webdriver.ChromeOptions()
option.headless = False
option.add_argument(f'user-agent={user_agent}')
option.add_argument('--ignore-certificate-errors')
option.add_argument('--allow-running-insecure-content')
option.add_argument('--disable-extensions')
option.add_argument('--start-maximized')
option.add_argument('--disable-gpu')
option.add_argument('--disable-dev-shm-usage')
option.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', options=option)
driver.get('https://twitter.com/i/flow/login')
