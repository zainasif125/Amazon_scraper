from playwright.sync_api import Playwright, sync_playwright, expect
import time
from bs4 import BeautifulSoup
import json
from product import get_products
from data_saver import save_data


class amazon_scraper():
    def run(self,search_list):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            for item in search_list:
                all_items=[]
                for i in range(1,20):
                    if i==1:  
                        page.goto(f"https://www.amazon.com/s?k={item}",timeout=600000, wait_until='domcontentloaded')
                    else:
                        page.goto(f"https://www.amazon.com/s?k={item}&page={i}",timeout=600000, wait_until='domcontentloaded')
                    for j in range(10):
                        print("Scrolling down ",j)
                        page.mouse.wheel(0, 540)
                        time.sleep(0.5)
                    html=page.content()
                    products=get_products(html)
                    all_items.extend(products)
                save_data(item,all_items)
            context.close()
            browser.close()

