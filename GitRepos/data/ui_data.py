from selenium.webdriver.common.by import By

##### UI data ######

url = "https://github.com/django"
browser = "chrome"
chrome_binary = "chromedriver.exe"
firefox_binary = "geckodriver.exe"

#######################		LOCATOR DATA	#######################
#Git Home Page
locator_XPATH = By.XPATH
all_repos = '//div[@class="org-repos repo-list"]//child::ul/li'
wait = 2