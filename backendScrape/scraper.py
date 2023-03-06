from playwright.sync_api import sync_playwright, ViewportSize
import re
import unicodedata
from bs4 import BeautifulSoup
from copy import deepcopy
import time

def menu_scrape():
    url = 'https://foodpro.ucr.edu/foodpro/longmenu.asp?sName=University+of+California%2C+Riverside+Dining+Services&locationNum=03&locationName=Glasgow&naFlag=&WeeksMenus=This+Week%27s+Menus&dtdate=03%2F05%2F2023&mealName=Lunch'
    # halls_html = ['text=College Nine/John R. Lewis Dining Hall', 'text=Cowell/Stevenson Dining Hall', 'text=Crown/Merrill Dining Hall', 'text=Porter/Kresge Dining Hall']

    # halls_name = ['Nine', 'Cowell', 'Merrill', 'Porter']
    # meals = ["Breakfast", "Lunch", "Dinner", "Late Night"]
    # food_cat = {"*Breakfast*": [], "*Soups*": [], "*Entrees*": [], "*Grill*": [], "*Pizza*": [], "*Clean Plate*": [], "*Bakery*": [], "*Open Bars*": [], "*DH Baked*": [], "*Plant Based Station*": [], "*Miscellaneous*": [], "*Brunch*": []}

    # Create nested dictionary
    # meal_times = {}
    # for i in meals:
    #     meal_times.update({i: deepcopy(food_cat)})

    # hall_menus = {}
    # for i in halls_name:
    #     hall_menus.update({i: deepcopy(meal_times)}) 

    # Go through every dining hall college and update hall_menus dictionary
    # for j in range(len(halls_name)):

    with sync_playwright() as p:
        browser = p.chromium.launch()  
        page = browser.new_page()
        page.set_viewport_size(ViewportSize(width = 1080*2, height=1920*2))
        page.goto(url)
        # page.locator(halls_html[j]).click()
        
        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')
        browser.close()

        #menuTable = soup.find('div', {'class': 'longmenucoldispname'})     #'table',  {'bordercolor': 'gray'})    # Finds meal table
        list_of_food = []                                       #{'class': 'longmenucoldispname'}
        for row in soup.find_all('div', {'class': ['longmenucoldispname', 'longmenucolmenucat']}):
            # column = row.find_all('div', {'class': 'longmenucoldispname'})
            # print(column)                           # For each item in the meal table, strip empty text
            text = row.text.strip()                                # and save the menu item
            text = re.sub(r"[\n][\W]+[^\w]", "\n", text)
            list_of_food.append(text)
            
        # Format List
      

        

        # Remove "nutrition calculator" from meals list
        # n_calc_caount = meals_list.count('Nutrition Calculator')
        # for i in range(n_calc_caount):
        #     meals_list.remove('Nutrition Calculator')

        # Updates hall_menu dictionary
        # for i in meals_list:
        #     if i in meal_times.keys():                              # If Breakfast, Lunch, Dinner, or Late Night
        #         meal_time = i                                       # Set current meal time
        #         continue
        #     elif "--" in i:                                         # If at a meal category
        #         meal_cat = i.strip("- ")                            # Clean string
        #         meal_cat = '*' + meal_cat + '*'     
        #         continue
        #     else:                                                   # Append meals to dictionary
        #         hall_menus[halls_name[j]][meal_time][meal_cat].append(i)
            
    for i in list_of_food:
        print(i)                   # Update database


menu_scrape()