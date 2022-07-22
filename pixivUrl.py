from asyncio.windows_events import NULL
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

pixiv_url = "https://www.pixiv.net"
# img_main = "https://cdn.discordapp.com/attachments/969967027601149984/999722432413835334/96038637_p0_master1200.jpg"
img_main = "https://cdn.discordapp.com/attachments/969967027601149984/999747488711970876/82772617_p1_master1200.jpg"
URL = "https://www.google.com/searchbyimage?image_url="

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('headless')
# options.add_argument('window-size=1920,1080')


def get_url(img):
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.implicitly_wait(5)

    driver.get(url="https://ascii2d.net/")

    urlin = driver.find_element(By.CSS_SELECTOR, value='#uri-form')
    urlin.send_keys(img)

    urlbtn = driver.find_element(
        By.CSS_SELECTOR, value='body > div > div > form.text-xs-center.m-t-2 > div > div.col-sm-1.col-xs-12 > button')
    urlbtn.click()

    uls = driver.find_elements(
        By.TAG_NAME, value='a')

    urls = []

    for ul in uls:
        href = ul.get_attribute("href")
        if(isinstance(href, str) and href.startswith(pixiv_url)):
            urls.append(href)

    driver.quit()

    if(len(urls) > 0):
        return(urls[0])
    else:
        return(NULL)


def get_id(url):
    return(url[31:])


if __name__ == "__main__":
    print(get_url(img_main))
