from selenium import webdriver
validateText = "Option3"
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
#driver.find_element_by_css_selector("#name").send_keys("Option3")
#driver.find_element_by_id("alertbtn").click()
#alert = driver.switch_to.alert
#alertText = alert.text
#assert validateText in alertText
#print(alert.text)
#alert.accept()


driver.find_element_by_css_selector("#name").send_keys("Option3")
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.dismiss()