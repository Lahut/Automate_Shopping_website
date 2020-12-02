from selenium import webdriver
from dotenv import load_dotenv
import os 
load_dotenv()

PATH = os.getenv("EXECUTABLE_PATH")
SHOPPING_WEBSITE = os.getenv("SHOPPING_WEB")
driver = webdriver.Chrome(PATH)
#your code inside this indent
driver.get(SHOPPING_WEBSITE)





#driver.quit()