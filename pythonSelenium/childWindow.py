from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element_by_link_text("Click Here").click()
childwindow = driver.window_handles[1]

#("parentid", "childid")
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
driver.close()