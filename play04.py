from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument('disable-gpu')

driver = webdriver.Chrome(chrome_options=options)

driver.command_executor()