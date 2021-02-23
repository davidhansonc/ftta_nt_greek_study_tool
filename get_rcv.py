import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os


def scrape_verses(link):
    r = requests.get(link)
    assert r.status_code == 200

    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    verses = soup.find_all('p', 'verse')
    for verse in verses:
        with open('rcv.txt', 'a') as rcv:
            rcv.write(verse.text + '\n')
    return


def get_child_links(url, driver, selector):
    driver.get(url)
    links = []
    for a in driver.find_elements_by_css_selector(selector):
        links.append(a.get_attribute('href'))
    
    for link in links:
        driver.get(link)

    return links



if __name__ == '__main__':
    url = "https://text.recoveryversion.bible/RcV.htm"

    driver = webdriver.Chrome()
    driver.maximize_window()

    book_links = get_child_links(url, driver, 'p.nt-links > a')

    all_chapters = []
    for link in book_links:
        chapter_links = get_child_links(link, driver, '.chapter-links > a')
        if chapter_links == []:
            chapter_links = [link]
        all_chapters.extend(chapter_links)

    driver.quit()
    
    if os.path.exists('rcv.txt'):
        os.remove('rcv.txt')
    for link in all_chapters:
        scrape_verses(link)