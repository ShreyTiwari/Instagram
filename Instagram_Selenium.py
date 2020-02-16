# Program to gather your followers and people who you follow, difference them and find out the people who you follow but dont follow you back.
# Youtube Tutorial link: https://www.youtube.com/watch?v=BGU2X5lrz9M

# Requirements:
#     - Gecko
#     - Selenium
#     - Python 3.6 or above

""" Importing the required headers """
# Webdriver is for navigation through the webpages. Library with the common keys (used in keyboard shortcuts) such as enter etc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# System libraries that will come in handy
import time
import random
import sys
from pynput.keyboard import Key, Controller

""" The Instagram class with all the functionality """
class Instagram:
    # Initialization of the object at the time of creation
    def __init__(self, username, password):
        # Initialize the username and password for the user
        self.username = username
        self.password = password
         
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        # profile.set_preference("browser.fullscreen.autohide", True)
        self.driver = webdriver.Firefox(firefox_profile = profile)

    # To close the webdriver in case of any issues
    def closeBrowser(self):
        self.driver.close()

    # To login to the Instagram account
    def login(self):
        # Set the web driver
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)

        try:
            # Get function to make a https request. Go to the homepage of Instagram (wait for it to load)
            driver.get("https://www.instagram.com/")
            time.sleep(3)

            # Login using the username and password (time delays added to let the page load properly)
            login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
            login_button.click()
            time.sleep(3)
            user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
            user_name_elem.clear()
            user_name_elem.send_keys(self.username)
            passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
            passworword_elem.clear()
            passworword_elem.send_keys(self.password)
            passworword_elem.send_keys(Keys.RETURN)
            time.sleep(3)

        except:
            return False

        url = driver.current_url
        if("login" in url):
            return False
        return True

    def goToHomePage(self):
        driver = self.driver
        profile_button = driver.find_element_by_xpath("//a[@href='/shrey_twr/']")
        profile_button.click()
        time.sleep(2)

        return 

    # Returns a list of followers
    def getFollowers(self):
        driver = self.driver
        print("\n--------------------------- Getting Followers ---------------------------")

        # Followers button Xpath: /html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span
        number_of_followers = (driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")).text
        print("You have", number_of_followers, "followers!\n")

        followers_button = driver.find_element_by_xpath("//a[@href='/shrey_twr/followers/']")
        followers_button.click()
        time.sleep(2)

        keyboard = Controller()
        keyboard.press(Key.tab)
        keyboard.press(Key.tab)
        for i in range(int(1.25 * int(number_of_followers.strip()))):
            keyboard.press(Key.down)
            time.sleep(0.1)

        # List Xpath: /html/body/div[4]/div/div[2]/ul/div 
        # Name1 Xpath: /html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[2]/div[2]/div
        # Name2 Xpath: /html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[2]/div[2]/div 
        # Name 'n' Xpath: /html/body/div[4]/div/div[2]/ul/div/li['n']/div/div[1]/div[2]/div[2]
        
        followers = []
        x = 0
        for i in range(1, int(number_of_followers.strip()) + 1):
            """ Paths that point to the user name """
            # path1 = "/html/body/div[4]/div/div[2]/ul/div/li[" + str(i) + "]/div/div[2]/div[2]/div"
            # path2 = "/html/body/div[4]/div/div[2]/ul/div/li[" + str(i) + "]/div/div[1]/div[2]/div[2]"
            
            """ Paths that point to the user handle """
            path1 = "/html/body/div[4]/div/div[2]/ul/div/li[" + str(i) + "]/div/div[1]/div[2]/div[1]/a"
            path2 = "/html/body/div[4]/div/div[2]/ul/div/li[" + str(i) + "]/div/div[2]/div[1]/div/div/a"
            paths = [path1, path2]
            #print(path)
            name = ""
            
            try:
                element = WebDriverWait(driver,5).until(
                    EC.presence_of_element_located((By.XPATH, paths[x]))
                )
                name = element.text
            except:
                if(x == 0):
                    x = 1
                else:
                    x = 0

                element = WebDriverWait(driver,5).until(
                    EC.presence_of_element_located((By.XPATH, paths[x]))
                )
                name = element.text
            
            print(name)
            followers.append(name)

        keyboard.press(Key.backspace)

        return followers

    # Returns a list of accounts that you are following
    def getFollowingAccounts(self):
        driver = self.driver
        print("\n--------------------------- Getting Following Accounts ---------------------------")

        # Number of people you are following button Xpath: /html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span
        number_of_people_following = (driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span")).text
        print("You are following", number_of_people_following, "accounts!\n")

        followers_button = driver.find_element_by_xpath("//a[@href='/shrey_twr/following/']")
        followers_button.click()
        time.sleep(2)

        keyboard = Controller()
        keyboard.press(Key.tab)
        keyboard.press(Key.tab)
        time.sleep(0.1)
        keyboard.press(Key.tab)
        time.sleep(0.1)
        keyboard.press(Key.tab)
        for i in range(int(1.25 * int(number_of_people_following.strip()))):
            keyboard.press(Key.down)
            time.sleep(0.1)

        # List Xpath: /html/body/div[4]/div/div[2]/ul/div 
        # Name1 Xpath: /html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[2]
        # Name2 Xpath: /html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[2]/div[2]/div 
        # Name 'n' Xpath: /html/body/div[4]/div/div[2]/ul/div/li['n']/div/div[1]/div[2]/div[2]
        
        following = []
        x = 0
        for i in range(1, int(number_of_people_following.strip()) + 1):
            """ Paths that point to the user name """
            # path1 = "/html/body/div[4]/div/div[2]/ul/div/li[" + str(i) + "]/div/div[2]/div[2]/div"
            # path2 = "/html/body/div[4]/div/div[2]/ul/div/li[" + str(i) + "]/div/div[1]/div[2]/div[2]"
            
            """ Paths that point to the user handle """
            path1 = "/html/body/div[4]/div/div[2]/ul/div/li[" + str(i) + "]/div/div[1]/div[2]/div[1]/a"
            path2 = "/html/body/div[4]/div/div[2]/ul/div/li[" + str(i) + "]/div/div[2]/div[1]/div/div/a"
            paths = [path1, path2]
            #print(path)
            name = ""
            
            try:
                element = WebDriverWait(driver,5).until(
                    EC.presence_of_element_located((By.XPATH, paths[x]))
                )
                name = element.text
            except:
                if(x == 0):
                    x = 1
                else:
                    x = 0

                element = WebDriverWait(driver,5).until(
                    EC.presence_of_element_located((By.XPATH, paths[x]))
                )
                name = element.text
            
            print(name)
            following.append(name)

        keyboard.press(Key.backspace)

        return following

if __name__ == "__main__":

    print("\n--------------------------- Welcome ---------------------------")
    # Add your username and password
    username = input("Enter your name: ")
    password = input("Enter your password: ")

    # Login to Instagram
    ig = Instagram(username, password)
    success = ig.login()

    print("\nAttempting to Login...")
    print("-------------------------------------------")
    if(success):
        print("Logged in successfully")
        print("-------------------------------------------\n")
    else:
        print("There was a Error during Login")
        print("-------------------------------------------\n")
        print("Closing Browser Session")
        ig.closeBrowser()
        exit(1)


    # Getting the required data
    ig.goToHomePage()
    followers = ig.getFollowers()
    followingAccounts = set(ig.getFollowingAccounts())

    ig.closeBrowser()

    # The important part is the difference (followingAccounts - Followers), i.e who you are following but are not following you
    for follower in followers:
        if(follower in followingAccounts):
            followingAccounts.remove(follower)

    print("\n--------------------------- Result ---------------------------")
    print("Number of accounts not following you back are: ", len(followingAccounts))
    print("The people you need to stop following are:")
    for i in followingAccounts:
        print(i)

    exit(0)