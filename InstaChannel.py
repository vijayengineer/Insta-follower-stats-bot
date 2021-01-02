from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

INSTAGRAM_USERNAME = ""
INSTAGRAM_PWD = ""
TARGET_ACCT = "" #channel name
chromedriver_path = "path/to/chromedriver"


class InstaChannel:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        self.follower_info_list = []
        self.followers_list = []
        self.following_list = []
        self.posts_list = []

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        cookie_button = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/button[1]")
        cookie_button.click()
        time.sleep(1.5)
        email_field = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_field.send_keys(INSTAGRAM_USERNAME)
        pwd_field = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pwd_field.send_keys(INSTAGRAM_PWD)
        pwd_field.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCT}")
        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]')
        for i in range(1, 10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(0.3)
        
    def gather_stats(self):
        for i in range(1,200):
            time.sleep(1)
            follower_info = self.driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[3]/div/div[1]/div[2]/div[1]/span/a')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_info)
            self.follower_info_list.append(follower_info.text)
            follower_info.click()
            time.sleep(1)
            followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]')
            self.followers_list.append(followers.text)
            following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]')
            self.following_list.append(following.text)
            posts = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]')
            self.posts_list.append(posts.text)
            self.driver.execute_script("window.history.go(-1)")
        return [self.follower_info_list,self.followers_list,self.following_list,self.posts_list]
    