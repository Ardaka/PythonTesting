from selenium import webdriver
# browser exposes an executable file
# Through Selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="c:\\geckodriver.exe")
#driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")
#driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")
driver.get("https://rahulshettyacademy.com/") # get method to hit url on browser
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close() # close current window