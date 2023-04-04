from pselenium import webdriver
import time
for i in range(100):
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()
    
    # Navigate to the website
    driver.get("https://github.com/rahulsh3105")
    
    # Wait for the website to load
    time.sleep(1)
    
    # Close the browser
    driver.quit()
