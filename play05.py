from selenium import webdriver
from pyquery import PyQuery as pq
import csv


def get_page_source(page):
    browser = webdriver.Chrome('C:\\program_in_PATH\\chromedriver.exe')

    if page < 1:
        print('Invalid page number')
        return 0
    urllet = 'http://samr.cfda.gov.cn/WS01/CL1129/'
    if page == 1:
        url = 'http://samr.cfda.gov.cn/WS01/CL1129/index.html'
    else:
        url = urllet + 'index_' + str(page-1) + '.html'
        print('Now crawling:', url)
    browser.get(url)
    # print(browser.page_source)
    page_source = browser.page_source
    browser.close()

    with open('page_swap.html', 'w', encoding='utf-8') as f:
        f.write(page_source)

    return 0

def get_page_data():
    with open('page_swap.html','r', encoding='utf-8') as f:
        str = f.read()

    doc = pq(str)

    columns = doc('.ListColumnClass15').items()
    swaps = []
    for column in columns:
        swaplet = {}
        swaplet['date']=column('.listtddate15').text()
        swaplet['url']=('http://samr.cfda.gov.cn/WS01'+column('[href]').attr('href')[2:])
        swaplet['title']=column('[href]').text()
        swaps.append(swaplet)

    csv_header = ['date', 'url', 'title']
    with open('csv_swap.csv','a+', encoding='utf-8') as f:
        writer = csv.DictWriter(f, csv_header)
        # writer.writeheader()
        for row in swaps:
            writer.writerow(row)

    return 0

def get_page_range(start, end):
    if start >= end:
        print('Start page number should be smaller than end')
        return 0
    for i in range(start, end+1):
        print(i)
        get_page_source(i)
        get_page_data()
    return 0


def main():
    # get_page_source(2)
    get_page_range(1, 89)


main()
