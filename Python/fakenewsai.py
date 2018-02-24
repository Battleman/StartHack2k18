from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time

def fakeNewsAI(domain):
    def correct_url(url): 
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        return url

    def crawl_url(domain, url="www.fakenewsai.com"):
        display = Display(visible=1, size=(1024, 768))
        display.start()

        url = correct_url(url)
        browser = webdriver.Firefox()
        browser.get(url)

        inputUrl = browser.find_element_by_id("url")
        inputUrl.clear()
        inputUrl.send_keys(domain)
        inputUrl.send_keys(Keys.RETURN)
        time.sleep(2)
        if(str(1) in browser.find_element_by_id("real").get_attribute("style")):
            retvalue= "Probably not fake"
        elif(str(1) in browser.find_element_by_id("fake").get_attribute("style")):
            retvalue="Probably fake"
        elif(str(1) in browser.find_element_by_id("error").get_attribute("style")):
            retvalue="Error"
        browser.quit()
        return retvalue
    return crawl_url(domain)
