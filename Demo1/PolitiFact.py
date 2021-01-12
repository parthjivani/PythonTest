from selenium import webdriver
import pytest
from selenium.webdriver.support.select import Select
import tkinter

class TestSenarioOne():

    def test_OpenChromeBrowser(self):
        global driver
        driver = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        url = "https://www.politifact.com/"
        driver.get(url)
        print("Browser Opened with Url" + url)

    def test_SenarioThird(self):
        Amount = '20'
        driver.find_element_by_xpath(".//input[@name='amount']").send_keys(Amount)
        Select_DropdDown = Select(driver.find_element_by_xpath(".//select[@name='installmentPeriod']"))
        DDValue = 'yearly'
        Select_DropdDown.select_by_value(DDValue)
        driver.find_element_by_xpath(".//button[@class='c-button']").click()
        Radiod_selection = driver.find_element_by_xpath(".//input[@value='" + DDValue + "']").is_selected()
        print(Radiod_selection)

    def test_SenarioOne(self):
        driver.find_element_by_xpath(".//a/span[text()='Menu']").click()

        for i in range(1, 8):
            Lables = driver.find_element_by_xpath("(.//label[@class='m-togglist__label'])[" + i + "]").text
            print(Lables)
        driver.find_element_by_xpath(".//a/span[text()='Menu']").click()
