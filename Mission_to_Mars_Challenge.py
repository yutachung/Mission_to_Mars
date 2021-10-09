#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


hemisphere_image_urls = []

list_of_links = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',
                'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
                'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',
                'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']
for link in list_of_links:
    browser.visit(link)
    html = browser.html
    bs = soup(html, 'html.parser')
    img_url_rel = bs.find('img', class_='wide-image').get('src')
    img_url = f'https://astrogeology.usgs.gov{img_url_rel}'
    title = bs.find('h2', class_='title').get_text()
    hemisphere_image_urls.append({"title":title, "img_url":img_url})


# In[4]:


hemisphere_image_urls


# In[5]:


browser.quit()

