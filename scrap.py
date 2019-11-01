
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_results(search_term):
	url ="https://www.startpage.com";
	browser = webdriver.Firefox()
	browser.get(url)
	search_box = browser.find_element_by_id("query")
	search_box.send_keys(search_term)
	search_box.submit()
	try:
		links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")  
		element = WebDriverWait(browser, 10).until(
		EC.presence_of_element_located((By.ID, "myDynamicElement")))
	except:
		links = browser.find_elements_by_xpath("//h3//a")
	# finally:
	# 	browser.quit() 
	results = []
	for link in links:
		href = link.get_attribute("href")
		print(href)
		results.append(href)
	browser.close()
	return results    

get_results("Machine Learning")
