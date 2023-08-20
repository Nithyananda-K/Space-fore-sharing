import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    driver.maximize_window()
    user_name = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    user_name.send_keys("admin")                                                   # username : admin
    password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password.send_keys("Hacker@4321")                                              # password : Hacker@4321
    login_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
    login_btn.click()                                                              # login_button
    time.sleep(5)

    # //div[@role='table']/div[2]/div[1]/div[1]/div[3]       complete table
    # //div[@role='table']/div[2]/div[9]/div[1]/div[4]       specific cell

    # first_part //div[@role='table']/div[2]/div[        rows (50)--> so dynamically row value should change b/w 1-50
    # second_part - ]/div[1]/div[                        col (9) --> so dynamically row value should change b/w 1-9
    # tp ]
    employee_name= "Aman"
    print("Employee - ", find_employee_status(driver, employee_name))

def find_rows_col(driver):
    # //div[@role='table']/div[2]/div[1]/div[1]/div[3]

    # //div[@role='table']/div[2]/div[9]/div[1]/div[4]
    # fp - //div[@role='table']/div[2]/div[
    # 1-9
    # sp - ]/div[1]/div[
    # 1- 9
    # tp ]

    # Row
    # //table[contains(@id,"cust")]/tbody/tr
    # //div[@role='table']/div[2]/div[9]/div[1]/div[4]
    # find out the number of rows
    row_elements = driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div")
    row = len(row_elements)
    print(row)

    # Col
    # // table[contains( @ id, "cust")] / tbody / tr[2] /

    # find out the number of rows
    col_elements = driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div[1]/div/div")
    col = len(col_elements)
    print(col)
    return row, col

def find_employee_status(driver, employee_name):
    row, col = find_rows_col(driver)                 # save the row, col  [stored as a local variable]
    first_part = "//div[@role='table']/div[2]/div["
    second_part = "]/div/div["
    third_part = "]"
    employee_status = None
    for i in range(1, row + 1):                           # for iterate rows  range(1,10) -> (1, 9+1)
        for j in range(1, col + 1):                       # for iterate cols  range(1,10)
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if employee_name in data:
                     # (hard coded) data //div[@role='table']/div[2]/div[2]/div[1]/div[3]
                employee_status_path = f"{dynamic_path}/following-sibling::div[3]"
                employee_status = driver.find_element(By.XPATH, employee_status_path).text
                print(f"{employee_name} employee status is  {employee_status}")
                if employee_status == "Terminated":
                    edit_employee_delete_btn = f"{dynamic_path}//following-sibling::div/div/button[1]"
                    driver.find_element(By.XPATH, edit_employee_delete_btn).click()
                break

    return employee_status