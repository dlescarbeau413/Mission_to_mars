#import splinter and beautiful soup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome',** executable_path,headless=False)


# In[2]:


url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[3]:


html=browser.html
news_soup = soup(html,'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[4]:


slide_elem.find('div', class_='content_title')


# In[5]:


news_title= slide_elem.find('div', class_='content_title').get_text()
news_title


# In[6]:


news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ###Featured Images 
# 

# In[7]:


url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[8]:


#fnind and click the full button image

full_image_elem =browser.find_by_tag('button')[1]
full_image_elem.click()


# In[9]:


# Parse the resulting html with soup
html =browser.html
img_soup = soup(html, 'html.parser')


# In[10]:


# Find the relative image url
img_url_rel =img_soup.find('img', class_= 'fancybox-image').get('src')
img_url_rel


# In[11]:


img_url =f'https://spaceimages-mars.com/{img_url_rel}'
img_url



import pandas as pd



df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns =['description','Mars','Earth']
df.set_index('description',inplace=True)
df




df.to_html()



browser.quit()


# # Challenge Deliverable 1

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere
for img in range(4):
    browser.links.find_by_partial_text('Hemisphere')[img].click()
    
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    title = img_soup.find('h2',class_ ='title').text
    img_url = img_soup.find('li').a.get('href')
    
    hemispheres = {}
    hemispheres['title'] = title
    hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
    
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()
    
browser.quit()
    

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls





