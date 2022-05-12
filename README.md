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

### IEX Data 
1. Configure your own `.env` file - this is not saved to git. See `.env.example` for necessary keys and `config.py` for how they get used.
This is a non-exhaustive list of what you will need
* An IEX API token - https://iexcloud.io/console/home, it should be the public key, not the secret, and start with `pk_`
2. In a console with your `finance-python` python environment active, run `jupyter-lab` in a console
3. Run the `StockExplorer.ipynb` notebook

### To Use Selenium / Web Scrapers

* We use google chrome. Make sure you have chrome downloaded and take note of which version you have (Chrome -> About)
* Follow the install instructions for your OS on https://selenium-python.readthedocs.io/installation.html
    * 1.2 - Your selenium should be installed when you `pip install -r requirements.txt`
    * 1.3 - I haven't tested this on windows
    * 1.4 - Skip
    * 1.5 - Download the correct driver (open chrome, go to "about" and see which version you have), unzip it, and move it to be on your system path
    * 1.6 - Skip

* When you finish the install, you should be able to run this code to see if selenium is installed correctly and
 can find your driver. This code below should open up a new window with python.
```
from selenium import webdriver
driver = webdriver.Chrome()
```

To run the marriage data scraper, do
```
from marriage_scraper import *
print(data)
```
