# finance-python
Experiments working with financial data

## Environment Setup
1. Get miniconda
2. Create the vitual environment
```
conda create -n finance-python python=3.10
conda activate finance-python
pip install -r requirements.txt
```

### To Use Selenium / Web Scrapers
Follow the install instructions for your OS on https://selenium-python.readthedocs.io/installation.html

We use google chrome.

* 1.2 - Your selenium should be installed when you `pip install -r requirements.txt`
* 1.3 - I haven't tested this on windows
* 1.4 - Skip
* 1.5 - Download the correct driver (open chrome, go to "about" and see which version you have), unzip it, and move it to be on your system path
* 1.6 - Skip

When you finish the install, you should be able to run this code
```
from selenium import webdriver
driver = webdriver.Chrome()
```
This should open up a new window with python.
