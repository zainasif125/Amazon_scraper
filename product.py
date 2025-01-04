from bs4 import BeautifulSoup
from datetime import datetime
def get_image(product):
    try:
        image=product.find("img",{"src":True})['src']
        return image
    except Exception as e:
        print("Error in getting image :",e)
        return
def get_title(product):
    try:
        title=product.find("div",{"data-cy":"title-recipe"})
        return title.text
    except Exception as e:
        print("Error in getting title :",e)
        return
def get_price(product):
    try:
        price=product.find("div",{"data-cy":"price-recipe"})
        price=price.find('span',{"class":"a-price-whole"}).text
        return price
    except Exception as e:
        print("Error in getting price :",e)
        return
def get_rating(product):
    try:
        rating=product.find("span",{"class":"a-icon-alt"}).text
        return rating
    except Exception as e:
        print("Error in getting ratings :",e)
        return
def get_reviews(product):
    try:
        reviews=product.find("span",{"class":"a-size-base"}).text
        return reviews
    except Exception as e:
        print("Error in getting reviews :",e)
        return
def get_link(product):
    try:
        link="https://www.amazon.com"+product.find('a',{'href':True})['href']
        return link
    except Exception as e:
        print("Error in getting link :",e)
        return
        
def get_details(product):
    try:
        image=get_image(product)
        title=get_title(product)
        price=get_price(product)
        rating=get_rating(product)
        reviews=get_reviews(product)
        link=get_link(product)
        return {
            "title":title,
            "price":price,
            "rating":rating,
            "reviews":reviews,
            "image":image,
            "link":link,
            "time_scraped": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        print(e)
        return
def get_products(html):
    soup=BeautifulSoup(html,"html.parser")
    products=soup.find_all("div",{"data-index":True,"data-asin":True})
    print("Number of products ",len(products))
    all_data=[]
    for product in products:
        if product is not None:
            data=get_details(product)
            if data is not None:
                print(data)
                if data['title'] is not None:
                    all_data.append(data)
                print("---------------"*5)
    return all_data