# repo-InstagramFollowerMonitor
Python Script to see who is not following you back on Instagram

### Requirements

Before use you must install chrome web driver and selenium

Selenium: `pip3 install selenium`

chrome web driver: `https://chromedriver.chromium.org` -> download latest stable release -> mv ~/download/chromedriver /usr/local/bin

Inside the Python code: `myBot = InstagramBot('__USERNAME__', '__PASSWORD__')` change Username and Password to YOUR username and password

### How this works
Opens instagram in a chrome browser and stores all the "following" users into a list and the "followers" users into another list
then makes another list that compares all users in the following list that is not in the followers list and stores them in the newly
created list.