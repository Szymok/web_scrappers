urls=['https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/']

categories=['Overview', 'XPerformance', 'Valuation', 'Dividends', 'Margins', 'Income Statement', 'Balance Sheet', 'Oscillators', 'Trend=Following']

import os
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd

user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
FireFoxDriverPath=ps.path.join(os.getcwd(), 'Drivers', 'geckodriver.exe')
FireFoxProfile=webdriver.FirefoxProfile()
FireFoxProfile.set_preference('general.useragent.override', user_agent)
browser=webdriver.Firefox(executable_path=FireFoxDriverPath)
browser.implicitly_wait(7)

url=''
browser.get(url)