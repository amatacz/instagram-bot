import random 
import time
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


CREDENTIALS = {"a.matacz93": "Cytrynowaaa1", "matacza93": "Cytrynowaaa1"}

class InstagramBot:
    driverpath = None
    
    def __init__(self):
        self.driver = Chrome(executable_path=self.driverpath)

# Login function ==================================================

    def login(self):
        self.driver.get("https://instagram.com")
        navbar = "//*[@id='mount_0_0_1P']/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div"
        cookies_click = "//*[@id='mount_0_0_KT']/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]"

        allow_cookies = WebDriverWait(self.driver, 10).until(exp.element_to_be_clickable((By.XPATH, "//button[text()='Only allow essential cookies']"))).click()
        time.sleep(3)

        choosing_creds = 0
        #choosing_creds = random.randint(0, len(CREDENTIALS))
        input_username = self.driver.find_element(By.NAME, "username")
        input_username.send_keys(list(CREDENTIALS.keys())[choosing_creds])
        input_password = self.driver.find_element(By.NAME, "password")
        input_password.send_keys(list(CREDENTIALS.values())[choosing_creds])
        time.sleep(2)
        log_in_click = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]").click()

        save_password = WebDriverWait(self.driver, 10).until(exp.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))).click()
        notification_off = WebDriverWait(self.driver, 10).until(exp.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))).click()

        print("[+] Logged .... ")

# Like new posts function ==================================================

    def do_like(self):

        with open("tags.txt", 'r') as f:
            tags = [line.strip() for line in f]

        tag = random.choice(tags)


        searchbox = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
        searchbox.clear()
        searchbox.send_keys(tag)
        time.sleep(5)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(4)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(3)
        print("[+] Posts found ....")
        time.sleep(4)


        
        # grid = self.driver.find_element(By.TAG_NAME, "article")

        # rows = [row.find_elements(By.CLASS_NAME, "_ac7v _aang") for row in grid]
        # print("[+] Rows found ....")
        # print(rows)

        photo = self.driver.find_elements(By.XPATH, "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd']")
        for img in photo:
            img.get_attribute('href').click()
            
        # print("[+] Photos found ....")
        # print(photo)

        # img_links = [img.find_element(By.TAG_NAME, "a").get_attribute('href') for img in photo]

        # for img in img_links:
        #     img.click() 



        # section = [sec.find_element(By.TAG_NAME, "section") for sec in article]
        # button = [btn.find_element(By.TAG_NAME, "button") for btn in section]


        # for btn in button:
        #     label = btn.find_element(By.TAG_NAME, "svg").get_attribute('aria-label')
        #     if label != 'Like':
        #         print("[+] Already liked ....")
        #     time.sleep(randint(1,5))
        #     btn.click()
        #     print("[+] Like On Post ....")
        #     time.sleep(randint(1,5))
        # # self.driver.refresh()

