from selenium import webdriver
from pyquery import PyQuery as pq

def get_page_source():
    browser = webdriver.Chrome('C:\\program_in_PATH\\chromedriver.exe')
    browser.get('http://samr.cfda.gov.cn/WS01/CL1129/')
    #print(browser.page_source)
    page_source = browser.page_source
    browser.close()

    print(type(page_source))

    with open('page_source.html', 'w', encoding='utf-8') as f:
        f.write(page_source)

def get_page_data():
    with open('page_source.html','r', encoding='utf-8') as f:
        str = f.read()
        print(type(str))

    doc = pq(str)
    print(type(doc))

def main():
    get_page_data()

main()