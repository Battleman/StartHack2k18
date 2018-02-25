from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time

def fakeNewsAI(domain, ff=True):
    if(ff):
        driver = webdriver.Firefox()
        display = Display(visible=0, size=(1024, 768))
        display.start()
    else:
        driver=webdriver.Chrome('D:\\epfl\\Lauzhack\\StartHack2k18\\Python\\chromedriver.exe')

    page = driver.get('http://www.fakenewsai.com/');
    inpu = driver.find_element_by_tag_name('input')
    inpu.clear()
    inpu.send_keys(url)
    driver.find_element_by_class_name('button').click()

    time.sleep(5)
    for resM in driver.find_elements_by_class_name('results') :
        if resM.get_attribute('style') == 'opacity: 1;' :
            return resM.text
    return "CRITICAL ERROR"
