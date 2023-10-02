from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.carousell.sg/search/dell%20optiplex?sort_by=3")
driver.implicitly_wait(2)
results = driver.find_elements(By.XPATH,
                              "//p[@class='D_pw D_ot D_px D_pA D_pC D_pH D_pJ D_Bc D_pO']")
# wait = WebDriverWait(driver, timeout=4)s
# wait.until(lambda d: results.is_displayed())
# results = driver.find_elements(By.XPATH,
#                               "//p[@class='D_pw D_ot D_px D_pA D_pC D_pH D_pJ D_Bc D_pO']")
for i in results: 
    time = i.get_attribute('innerHTML')
    if str(time)[2] == 'd':
        break
    print(time)
    
    

