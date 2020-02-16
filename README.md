# Instagram

Repository to use API's and GUI automation to get a list of your followers and followees. Makes use of some public API's and selenium framework for GUI automation.<br />

Instagram_API.py makes use of the instaloader library to get the list of followers and followees. However the api is rate limited and pauses for 10mins every time the request threshold is exceeded. Recommended for when a small number of accounts are to be queried. Make sure to use pip to install the instaloader library before hand.<br />

The Instagram_Selenium.py script makes use of the Selenium framework to navigate to your home page and extract the followers and followees. This script isn't rate limited but could take a long time to complete if millions of accounts are being queried. Make sure to have the selenium framework installed and the browser interfacing setup beforehand.
