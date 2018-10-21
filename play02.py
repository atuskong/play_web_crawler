from selenium import webdriver
from pyquery import PyQuery as pq
import csv

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

    doc = pq(str)
    # print(doc('.ListColumnClass15 .listtddate15').text())

    columns = doc('.ListColumnClass15').items()
    swaps = []
    for column in columns:
        swaplet = {}
        # print(column('.listtddate15').text())
        swaplet['date']=column('.listtddate15').text()
        # print(column('[href]').attr('href'))
        swaplet['appendix']=column('[href]').attr('href')
        # print(column('[href]').text())
        swaplet['title']=column('[href]').text()
        swaps.append(swaplet)
    # print(swaps)

    csv_header = ['date', 'appendix', 'title']
    with open('csv_file.csv','w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, csv_header)
        writer.writeheader()
        for row in swaps:
            writer.writerow(row)

def main():
    get_page_data()

main()