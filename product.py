from bs4 import BeautifulSoup

def get_image(product):
    try:
        image=product.find("img",{"src":True})['src']
        return image
    except:
        return
def get_title(product):
    try:
        title=product.find("div",{"data-cy":"title-recipe"})
        title=title.find('span',{"class":"a-size-medium a-color-base a-text-normal"}).text
        return title
    except:
        return
def get_price(product):
    try:
        price=product.find("div",{"data-cy":"price-recipe"})
        price=price.find('span',{"class":"a-price-whole"}).text
        return price
    except:
        return
def get_rating(product):
    try:
        rating=product.find("span",{"class":"a-icon-alt"}).text
        return rating
    except:
        return
def get_reviews(product):
    try:
        reviews=product.find("span",{"class":"a-size-base"}).text
        return reviews
    except:
        return
def get_link(product):
    try:
        link="https://www.amazon.com"+product.find('a',{'href':True})['href']
        return link
    except:
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
            "image":image,
            "title":title,
            "price":price,
            "rating":rating,
            "reviews":reviews,
            "link":link
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