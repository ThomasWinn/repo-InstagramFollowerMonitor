from selenium import webdriver
from time import sleep

class InstagramBot:

    ''' 
    always need an init function that will run on a new instance of this class
    
    Opens instagram on chrome -> pushes Log In -> fills in username & password -> pushes
    no turning on notification 
    
    '''
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

        self.driver.get("https://instagram.com")
        sleep(2)

        '''Clicks on "log in" on instagram.com'''
        '''Clicking element = ("//__HTMLClassifier__[@__fieldType__ = "Target"]")\.click()'''
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()

        sleep(2)

        '''Typing in username and password into respective fields then clicking submit'''
        self.driver.find_element_by_xpath("//input[@name= \"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name= \"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type= "submit"]')\
            .click()

        sleep(4)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()

        sleep(3)
    
    def getUnfollowed(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username))\
            .click()
        
        sleep(2)

        

myBot = InstagramBot('thomaswinn1', 'S@die2011')
myBot.getUnfollowed()
