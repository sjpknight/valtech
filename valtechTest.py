##############################
# Author = Simon Knight
# Valtech Website Test Script
# Execute using Python3
##############################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.set_window_size(1380,800)

#Question 1
driver.get("https://www.valtech.com")
newsSection = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[3]/div[1]/header/h2')
assert "LATEST NEWS" in newsSection.text

# Question 2
aboutPageLink = driver.find_element_by_xpath('//*[@id="navigationMenuWrapper"]/div/ul/li[1]/a/span')
aboutPageLink.click()
title = driver.find_element_by_tag_name('h1')
assert "About" in title.text

servicesPageLink = driver.find_element_by_xpath('//*[@id="navigationMenuWrapper"]/div/ul/li[3]/a/span')
servicesPageLink.click()
title = driver.find_element_by_tag_name('h1')
assert "Services" in title.text

workPageLink = driver.find_element_by_xpath('//*[@id="navigationMenuWrapper"]/div/ul/li[2]/a/span')
workPageLink.click()
title = driver.find_element_by_tag_name('h1')
assert "Work" in title.text

# Question 3
contactUsArea = driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/p[2]')
offices = contactUsArea.text
# number of offices = length of text string less initial "you'll find us in" text
numOffices = len(offices.split())-4
print(numOffices)
