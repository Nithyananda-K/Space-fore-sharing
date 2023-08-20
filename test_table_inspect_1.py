from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_tables():
    driver = webdriver.Firefox()
    driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()

    # sceanrio 01 how many rows in table
    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")  # --> //tr
    row = len(row_elements)
    print(row)

    # sceanrio 02 how many coloms in table
    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")  # -> //tr[2]/td"
    col = len(col_elements)
    # print(col)

    # first_part = "//table[contains(@id,'cust')]/tbody/tr["
    # second_part = "]/td["
    # third_part = "]"
    # // tr[2]/td[1]
    part_a = "//tr["
    part_b = "]/td["
    part_c = "]"

    values_in_table= []

    for i in range(2, row+1):  # range(1,10) -> 1, 9+1)
        for j in range(1, col+1):
            dynamic_p01 = f"{part_a}{i}{part_b}{j}{part_c}"
            # dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_p01).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_p01}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennet is in {country_text}")

            for value in data:
                values_in_table.append(value)

    final_value= "".join(values_in_table)
    print(final_value)

    # Find Helen Bennett's country

    driver.get("https://awesomeqa.com/webtable1.html")
    # Get the table
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")  # xpath chaining
    row_table = table.find_elements(By.TAG_NAME, "tr")  # //table[@summary='Sample Table']/tbody/tr[4]/td

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")  # //tr/td
        for e in cols:
            if "UAE" in e.text:
                print("Yes")
            # else:
            #     print("NO")




