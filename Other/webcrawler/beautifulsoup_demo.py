"""
beautifulsoup  - HTML (and more) parser
The 'beautifulsoup' python package is needed in this program

In PyCharm:
    File -> Settings
    Scroll down and click on Project Interpreter
    Look in the list for "beautifulsoup4"
    If it is in the list, nothing further is needed
    If it is NOT in the list it needs to be installed:
        Click the (plus-sign) '+' in the upper-right corner of the list box
        Start to enter "beautifulsoup" in the search box
        A list of all available packages will start to appear in a list
        Select "beautifulsoup4" from the list
        Make sure the "Install to user's site packages directory" is checked
        Click the "Install Package" button in the lower left to install the package

Other IDEs:
    Set up a Virtual Environment
    'pip install beautifulsoup'
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup  

html = urlopen("http://www.wikipedia.org")
bsobject = BeautifulSoup(html.read(), "html.parser")
print(bsobject.title)  # only print code with <title> tag
print(bsobject.h1)     # only print <h1> tags
