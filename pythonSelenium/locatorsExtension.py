from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.maximize_window()
driver.find_element_by_css_selector("#username").send_keys("ardak.akish@yahoo.com")
driver.find_element_by_css_selector(".password").send_keys("Akish6886!")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
# //tagname[text() = 'xxx']
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)

#driver.find_element_by_css_selector("#Login").click()
