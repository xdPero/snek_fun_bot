import time
import yagmail
from selenium import webdriver
from selenium.webdriver.common.by import By



class Driver:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # No detection
        chrome_options.add_argument("--start-maximized")  # Open maximized
        chrome_options.add_argument("--disable-infobars")  # Hide "Chrome is being controlled..."
        chrome_options.add_argument("--disable-extensions")  # No extensions
        chrome_options.add_argument("--disable-notifications")  # No site notifications
        chrome_options.add_argument("--disable-popup-blocking")  # Allow popups (if needed)
        chrome_options.add_argument("--no-sandbox")  # Linux
        chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid issues in Docker or low-memory


        self.driver = webdriver.Chrome(chrome_options)


    def first_entry(self):
        self.driver.get('https://www.snek.fun/')
        time.sleep(2)

        new_button = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/button[2]')
        time.sleep(2)
        new_button.click()
        time.sleep(2)
        last_added = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[3]/div[1]/a/div/div[1]/div[2]/div/div[1]/div/span[1]')
        text_of_the_latest = last_added.text #first entry newest coin

        while True:
            time.sleep(2)
            refreshed = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div[1]/a/div/div[1]/div[2]/div/div[1]/div/span[1]')
            time.sleep(2.3)
            if refreshed.text != text_of_the_latest:
                break
            else:
                self.driver.refresh()

        email = "Enter your email here"
        receiver = "Enter receiver email here"
        password = "Enter your app password here" #2FA needs to be activated in your acc, look the readme file


        try:
            yag = yagmail.SMTP(user=email, password=password)
            yag.send(to=receiver, subject="Token Change", contents="There was a change in the newest token")
            print("Email sent successfully")
        except:
            print("Email could not be sent")






