from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import json


path = './contacts/contacts.json'

PATH = '/Users/nikitamoussa/Documents/kwork/businessa/chrome/chromedriver'

def process_telegram_contact_to_emoji():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            contact_name = [obj["username"] for obj in data]
            print(contact_name)
        # Получаем значения поля "username" для каждого объекта
        # Выводим значения на экран
        for username in contact_name:
            print(username)
            if not ' 2в' in username:
                find_contact = driver.find_element(
                    By.ID, "telegram-search-input")
                time.sleep(5)
                find_contact.send_keys(username)
                time.sleep(5)
                find_contact.send_keys(Keys.ENTER)
                time.sleep(5)
                name_input = driver.find_element(
                    By.CLASS_NAME, "Button smaller translucent round")
                name_input.click()
                time.sleep(5)
                client_name = driver.find_element(
                    By.CLASS_NAME, "Button smaller translucent round")
                client_name.click()
                time.sleep(5)
                driver.find_element(
                    By.CLASS_NAME, "icon icon-add-user").click()
                time.sleep(5)
                change_user_info_icon = driver.find_element(
                    By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div[1]/div/div/section/button")
                change_user_info_icon.click()
                time.sleep(5)
                change_username = driver.find_element(
                    By.CLASS_NAME, "form-control")
                change_username.send_keys(" 3в")
                with open (path, 'w') as file:
                    data = json.load(file)
                    
                data.append(contact_name)
            
                with open (path, 'w') as file:
                    json.dump(data, file, indent=4)
                return contact_name
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()