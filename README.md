# Instagram

Repository to use API's and GUI automation to get a list of your followers and followees. Makes use of some public API's and Selenium framework for GUI automation. The scripts expect you to provide your password and have multifactor authentication turned off.<br />

## Instagram_API.py
Instagram_API.py makes use of the 'instaloader' library to get the list of followers and followees. However this API is rate limited and pauses for 10mins every time the maximum requests threshold is exceeded. Recommended when a small number of accounts are to be queried. Make sure to use pip to install the instaloader library before the script execution.<br />

## Instagram_Selenium.py
The Instagram_Selenium.py script makes use of the Selenium framework to navigate to your home page and extract the followers and followees. This script isn't rate limited but could take a long time to complete if millions of accounts are being queried. Make sure to have the selenium framework installed and the browser interfacing setup beforehand. In addition to this also have the 'pynput' library installed for python. 
