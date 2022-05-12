import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def load_and_accept_disclaimer():
    driver = webdriver.Chrome()
    tcc_link = "https://www.tccsearch.org/"
    driver.get(tcc_link)
    disclaimer_link_id = "cph1_lnkAccept"
    disclaimer_link = driver.find_element("id", disclaimer_link_id)
    disclaimer_link.click()
    return driver


def search_marriage_page(driver, date_from: dt.date, date_to: dt.date):
    driver.get("https://www.tccsearch.org/Marriage/SearchEntry.aspx")
    date_inputs = driver.find_elements("xpath", "//input[@title='mm/dd/yyyy']")
    assert len(date_inputs) == 4, f"expected 4 date elements, got {len(date_inputs)}"
    application_date_from = date_inputs[0]
    format_mmddyyyy = "%m/%d/%Y"
    application_date_from.send_keys(Keys.BACKSPACE*8 + date_from.strftime(format_mmddyyyy))
    application_date_to = date_inputs[1]
    application_date_to.send_keys(Keys.BACKSPACE*8 + date_to.strftime(format_mmddyyyy))
    search_btn = driver.find_element("id", "cphNoMargin_SearchButtons2_btnSearch")
    search_btn.click()
    return driver


def read_marriage_results_table(driver):
    table_rows = driver.find_elements("xpath", "//tr[@adr]")
    data = []
    for i in range(len(table_rows)):
        row_element = table_rows[i]
        print(row_element.text)
        try:
            cells = row_element.find_elements("xpath", "./td")
            date = cells[10].text
            person1 = cells[12].text
            person2 = cells[13].text
            data.append({
                "date": date,
                "person1": person1,
                "person2": person2
            })
        except:
            print("Error on row")
            continue
    return driver, data


def main():
    driver = load_and_accept_disclaimer()
    date_to = dt.date(2022, 5, 12)
    date_from = dt.date(2022, 5, 1)
    driver = search_marriage_page(driver, date_from, date_to)
    driver, data = read_marriage_results_table(driver)
    return driver, data

driver, data = main()
