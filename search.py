from colorama import Fore,Back,Style
from selenium import webdriver
import time
topic_search=input(Fore.RED+ "Enter the topic do you need to search: ")
topic_search=topic_search.replace(' ',"+")
browser=webdriver.Chrome("chromedriver.exe")
for i in range (1):
    #time.sleep(10)
    elements=browser.get("https://www.google.com/search?q="+topic_search +"&start" +str(i))
    input("press any key to exit")
    

