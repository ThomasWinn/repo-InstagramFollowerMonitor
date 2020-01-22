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
        '''
            Clicking element = ("//__HTMLClassifier__[@__fieldType__ = "Target"]")\.click()
            Or you can just click get full xpath for convienience
        '''
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
    
    '''     
    click profile -> click following -> get names in following -> click followers ->
    get names in followers -> condense both lists to get people not following back
    
    '''
    def getUnfollowed(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username))\
            .click()
        
        sleep(2)

        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]")\
            .click()

        following = self._get_names()

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()

        followers = self._get_names()
        
        # for all users you are following that are not in the followers list
        not_following_back = [user for user in following if user not in followers]

        print(not_following_back)


    def _get_names(self):
        sleep(2)

        # uncomment if there is a suggestions list of users when you're scrolling down
        #suggestions = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        #self.driver.execute_script('arguments[0].scrollIntoView()', suggestions)
        #sleep(2)

        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")

        # On each scroll compare the height of the box with the height of the box before scroll
        # If height same then stop
        last_height = 0
        height = 1

        while last_height != height:
            last_height = height
            sleep(1)

            # scroll to bottom of scroll box then return height of scroll box
            height = self.driver.execute_script("""
                    arguments[0].scrollTo(0, arguments[0].scrollHeight);
                    return arguments[0].scrollHeight;
                    """, scroll_box)

        # finds all instagram username and returns it in links
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        # close button 
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

# Initialize function and calls the getUnfollowed function
myBot = InstagramBot('USRNAME', 'PW')
myBot.getUnfollowed()

