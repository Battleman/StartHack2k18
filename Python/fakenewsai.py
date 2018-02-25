from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time

def fakeNewsAI(domain, ff=True):
    if(ff):
        display = Display(visible=0, size=(1024, 768))
        display.start()
        driver = webdriver.Firefox()
    else:
        driver=webdriver.Chrome('D:\\epfl\\Lauzhack\\StartHack2k18\\Python\\chromedriver.exe')

    page = driver.get('http://www.fakenewsai.com/');
    inpu = driver.find_element_by_tag_name('input')
    inpu.clear()
    domain = toDomain(domain)
    inpu.send_keys(domain)
    driver.find_element_by_class_name('button').click()

    time.sleep(5)
    retVal = "CRITICAL ERROR"
    for resM in driver.find_elements_by_class_name('results') :
        if resM.get_attribute('style') == 'opacity: 1;' :
            retVal = resM.text
    driver.quit()
    return retVal


def toDomain (url) :
	if ('http' in url) :
		return url.split('/')[2]
	else :
		return url.split('/')[0]
	