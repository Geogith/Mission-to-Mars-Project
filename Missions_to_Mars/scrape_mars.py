# Import dependencies

from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time



def scrape():
    url = f'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)
    time.sleep(3)
    html_string = browser.html

    soup = BeautifulSoup(html_string, 'html.parser')

    news_titles = soup.find_all("div", class_='content_title')[1].get_text()
    news_para = soup.find("div", class_='article_teaser_body').get_text()


    browser2 = Browser('chrome', **executable_path, headless=True)       
    url = f"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser2.visit(url)
    time.sleep(3)

    mars = browser2.find_by_id('full_image')
    mars.click()
    time.sleep(2)

    mars_page = browser2.html
    mars_image_page = BeautifulSoup(mars_page, 'html.parser')
    image_of_mars = mars_image_page.find(class_='fancybox-image').get('src')

    featured_image_url = 'https://www.jpl.nasa.gov'+image_of_mars

    url = 'https://space-facts.com/mars/'
    facts_table = pd.read_html(url)[0]
    facts_table_html = facts_table.to_html()

    browser3 = Browser('chrome', **executable_path, headless=True)
    url = f'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser3.visit(url)
    time.sleep(2)

    # browser2.find_by_css('a.product-item h3')[0].click()
    # mars_links = browser3.find_by_css('a.product-item h3')
    # len(mars_links)
    hemisphere_image_urls = []
    for i in range(4):
        mars_links = browser3.find_by_css('a.product-item h3')
        link = mars_links[i]
        title = link.html
        link.click()
        html = browser3.html
        soup = BeautifulSoup(html)
        div = soup.find('div', class_='downloads')
        url = div.find_all('a')[1]['href']
        print(title, url)
        hemisphere_image_urls.append({'title': title, 'img_url':url})
        browser3.back()

    mars_data = {
        'news': {'title': news_titles, 'paragraph': news_para}, 
        'featured_image_url': featured_image_url, 
        'facts_table': facts_table_html, 
        'hemisphere_image_urls': hemisphere_image_urls
    }

    return mars_data



if __name__=='__main__': 
    print(scrape())
