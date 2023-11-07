# Importing the required modules/libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

import random
# Taking input from the user

print("Enter the url of the amazon webpage !")
URL = input()


# List of User Agents

user_agents_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/77.0.1",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/73.0.3856.344",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.23.75 Chrome/89.0.4389.90",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Vivaldi/3.8.2259.42",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/6.1.3.1000",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Avast/98.8.3863.87",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/77.0.1",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/88.0.705.81",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/73.0.3856.344",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.23.75 Chrome/89.0.4389.90",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Vivaldi/3.8.2259.42",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/6.1.3.1000",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Avast/98.8.3863.87",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/77.0.1",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/73.0.3856.344",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.23.75 Chrome/89.0.4389.90",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Vivaldi/3.8.2259.42",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/77.0.1",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Edge/88.0.705.81",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Opera/73.0.3856.344",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.23.75 Chrome/89.0.4389.90",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Vivaldi/3.8.2259.42",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/88.0.1",
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.1.2 Safari/602.4.8',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/601.7.8',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.1.9 Safari/533.21.1'

]
# Function to make request with a specific user agent.

def make_request_with_user_agent(user_agents_list,URL):
    
    user_agent = random.choice(user_agents_list)
    HEADERS = {'User-Agent':user_agent, 'Acccept-Language':'en-US,en;q=0.5'}
    
    webpage = requests.get(URL,headers=HEADERS)
    return webpage
    
success = False

while not success:
    
    webpage_response = make_request_with_user_agent(user_agents_list,URL)
    
    if ( webpage_response.status_code == 200 ):
        print("Data Fetched Successfully !")
        success = True
        
    else:
        continue
        
soup = BeautifulSoup(webpage_response.content,'html.parser')

# Extracting all the product links from webpage

parent_tags = soup.find_all("h2", attrs={'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})

links_list = []
for tags in parent_tags:
    
    sub_parent_tag = tags.find("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    product_link = "https://www.amazon.in" + sub_parent_tag.get('href')
    
    links_list.append(product_link)
amazon_scrapData = {'Product_Name':[],'Price':[],'Rating':[],'Availability':[],'Product_Link':[]}
# Functions to scrap product details

# Function to extract Product Name 

def fetch_productName(product_link_soup):
    
    try:
        # Extracting upper tag of product title
        product_name_uppertag =  product_link_soup.find("h1", attrs={'class':'a-size-large a-spacing-none'})
        
        # Extracting anchor tag of product title
        product_name_tag = product_name_uppertag.find("span", attrs={'class':'a-size-large product-title-word-break'})
        product_name = product_name_tag.text.strip()
    
    except AttributeError:
        product_name = "Not Available"
        
    return product_name
    
# Function to extract Product Price 

def fetch_productPrice(product_link_soup):
    
    try:
        # Extracting upper tag of product price
        product_price_uppertag =  product_link_soup.find("span", attrs={'class':'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'})
        
        product_price_symbol = product_price_uppertag.find("span", attrs={'class':'a-price-symbol'}).text.strip()
        product_price_whole = product_price_uppertag.find("span", attrs={'class':'a-price-whole'}).text.strip()
        product_price = (product_price_symbol + product_price_whole)
    
    except AttributeError:
        product_price = "NIL"
        
    return product_price
    
    
# Function to extract Product Rating

def fetch_productRating(product_link_soup):
    
    try:
        product_rating_uppertag = product_link_soup.find("a", attrs={'class':'a-popover-trigger a-declarative'})
        product_rating_tag =product_rating_uppertag.find("span", attrs={'class':'a-size-base a-color-base'})
        product_rating = product_rating_tag.text.strip() + "⭐️"
    
    except AttributeError:
        product_rating = "NA"
        
    return product_rating

# Function to extract Product Availability

def fetch_productAvailability(product_link_soup):
    
    try:
        # Upper tag of product availability
        product_availability_uppertag = product_link_soup.find("div", attrs={'class':'a-section a-spacing-none a-spacing-top-micro }', 'id':'availability'})
        
        # Product Availability tag
        product_availability_tag = product_availability_uppertag.find("span")
        
        product_availability = product_availability_tag.text.strip()
    
    except AttributeError:
        
        try:
            product_availability_uppertag = product_link_soup.find("div", attrs={'class':'outOfStock'})
            product_availability_tag = product_availability_uppertag.find("span", attrs={'class':'a-color-price a-text-bold'})
            product_availability = product_availability_tag.text.strip()
            
        except AttributeError:
            product_availability = "In Stock"
        
    return product_availability
    
# Fetching Product Details and Storing in a Dictionary

for link in links_list:
    
    user_agent = random.choice(user_agents_list)
    HEADERS = {'User-Agent':user_agent, 'Acccept-Language':'en-US,en;q=0.5'}
    
    new_webpage = requests.get(link, headers=HEADERS)
    
    
    if ( new_webpage.status_code != 200 ):
        
        
        error_message = ("Error " + str(new_webpage.status_code) + " Access Denied")
        
    
        amazon_scrapData['Product_Name'].append(error_message)
        amazon_scrapData['Price'].append(error_message)
        amazon_scrapData['Rating'].append(error_message)
        amazon_scrapData['Availability'].append(error_message)
        amazon_scrapData['Product_Link'].append(link)
        
        continue
        
    product_link_soup = BeautifulSoup(new_webpage.content,'html.parser')
    
    product_name_uppertag =  product_link_soup.find("h1", attrs={'class':'a-size-large a-spacing-none'})
    if (product_name_uppertag is None):
        while (product_name_uppertag==None):
            
            new_webpage = requests.get(link,headers=HEADERS)
            product_link_soup = BeautifulSoup(new_webpage.content,'html.parser')
            product_name_uppertag =  product_link_soup.find("h1", attrs={'class':'a-size-large a-spacing-none'})
    
    amazon_scrapData['Product_Name'].append(fetch_productName(product_link_soup))
    amazon_scrapData['Price'].append(fetch_productPrice(product_link_soup))
    amazon_scrapData['Rating'].append(fetch_productRating(product_link_soup))
    amazon_scrapData['Availability'].append(fetch_productAvailability(product_link_soup))
    amazon_scrapData['Product_Link'].append(link)
        
# Generating a dataframe using pandas library

amazon_df = pd.DataFrame.from_dict(amazon_scrapData)

# Converting the scrap data to a CSV File

amazon_df.to_csv("amazon_scrapData.csv",index=False)
print(amazon_df)