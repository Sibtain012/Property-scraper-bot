import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from house_details import house_address_list, house_prices_list, links

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfoRqTHevETi27hmwrarJIDfrTCbSm2LInkvQTPjc6PCurUZA/viewform?usp=header"
for address, price, link in zip(house_address_list, house_prices_list, links):

    driver.get(form_url)
    time.sleep(3)
    #Wait for the form input field to load
    first_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    second_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    third_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    first_input.send_keys(address)
    second_input.send_keys(price)
    third_input.send_keys(link)

    #Submit the form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(2)  # Wait for submission confirmation

    # Optional: Go back to submit another response
    another_response = driver.find_elements(By.LINK_TEXT, "Submit another response")
    if another_response:
        another_response[0].click()
    else:
        driver.get(form_url)

    time.sleep(2)
