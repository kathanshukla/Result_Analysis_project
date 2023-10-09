from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

match = [] #defining array for storing sgpa of every student
id = [] #defining array for storing ids of every student
#importing chrome driver
path = 'C:/Users/lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

for i in range(1,4):
    s = Service(path)
    driver = webdriver.Chrome(service=s)
    driver.get("https://charusat.edu.in:912/UniExamResult/")
    driver.implicitly_wait(3)

    #selection depstar
    institute_ = driver.find_element(By.XPATH, '//*[@id="ddlInst"]')
    institute_.send_keys("DEPSTAR")

    #selecting BTECH(CS)
    degree_ = driver.find_element(By.XPATH, '//*[@id="ddlDegree"]')
    degree_.send_keys("BTECH(CS)")

    #selecting semister
    sem_ = driver.find_element(By.XPATH, '//*[@id="ddlSem"]')
    sem_.send_keys("6")

    #selecting month of exam
    exam_ = driver.find_element(By.XPATH, '//*[@id="ddlScheduleExam"]')
    exam_.send_keys("APRIL 2023")

    #selecting id
    s_id = driver.find_element(By.XPATH, '//*[@id="txtEnrNo"]')
    s_id.send_keys("20dcs"+'{0:03}'.format(i))
    if("20dcs"+'{0:03}'.format(i) == "20dcs014" or "20dcs"+'{0:03}'.format(i) == "20dcs127"):
        continue
    #pressing enter
    s_id.send_keys(Keys.ENTER)

    #extracting sgpa
    match_ = driver.find_element(By.XPATH, '//*[@id="uclGrd1_lblSGPA"]')
    match_ = match_.text
    id.append("20dcs"+'{0:03}'.format(i))
    match.append(match_)

    #closing the tab
    driver.close();

# print(id)
# print(match)

df = pd.DataFrame(id,columns = ['Student_id'])
df["SGPA"] = match
print(df)

df.to_csv("C:\\Users\\lenovo\\Desktop\\result_student.csv")

while (1):
    pass
