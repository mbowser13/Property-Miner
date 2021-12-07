from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def minerPrinceWilliam (s):
    driver = webdriver.Chrome('/Users/mbowser/Documents/PropertyMiner/WebDriver/chromedriver') ## Location for the chromedriver

    driver.get("http://pwc.publicaccessnow.com/GPINSearch.aspx") ## Pointer to the real estate assessment website

    search_bar = driver.find_element_by_name("owner") ## Variable containing the search bar element

    search_bar.clear() ## Clear the search bar to make sure it is fully clear
    search_bar.send_keys(s) ## Send the parcel ID input to the search bar
    search_bar.send_keys(Keys.RETURN) ## Enter input

    driver.implicitly_wait(10) ## Allow for page to load by setting an implicit wait time

    ## Set xpaths for all variables
    owner = driver.find_element_by_xpath('/html/body/form/div[4]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/span[3]/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td[2]')
    owner_add1 = driver.find_element_by_xpath('/html/body/form/div[4]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/span[3]/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]')
    owner_add2 = driver.find_element_by_xpath('/html/body/form/div[4]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/span[3]/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr/td/table/tbody/tr[4]/td[2]')
    pin = driver.find_element_by_xpath('/html/body/form/div[4]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/span[1]/div/div/div[2]/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td[1]/font')
    prop_add = driver.find_element_by_xpath('/html/body/form/div[4]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/span[3]/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td')

    ## Convert all xpaths to text
    owner_text = owner.text
    owner_add_text1 = owner_add1.text
    owner_add_text2 = owner_add2.text
    owner_add = owner_add_text1 + " " + owner_add_text2
    pin_text = pin.text
    prop_add_text = prop_add.text


    ## Returns
    return pin_text, owner_text, owner_add, prop_add_text.replace('\n','')

    ## Close web driver
    driver.close() ## Close out of driver
