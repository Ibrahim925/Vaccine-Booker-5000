import os
from dotenv import load_dotenv
from selenium import webdriver
import time

load_dotenv()

file = os.getenv('FILE')
url = os.getenv('URL')
print(file)
driver = webdriver.Chrome(file)
driver.get(url)

time.sleep(2)

# Click reschedule button on first sign up
resched_btn = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div/article/div/div/div[2]/flowruntime-lwc-body/div/flowruntime-list-container/div/slot/flowruntime-screen-field[6]/slot/flowruntime-lwc-field/div/flowruntime-lwc-field-impl/div/article/div/lightning-layout/slot/lightning-layout-item[2]/slot/div/button[1]')
resched_btn.click()
time.sleep(1)

while True:
     try:
          # Open location select
          location_slct = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div/article/div/div/div[2]/div/div/div[4]/article/div[2]/p/div/div/lightning-combobox/div/lightning-base-combobox/div')
          location_slct.click()
          time.sleep(0.75)


          #Click milton
          milton = driver.find_element_by_xpath('//*[@id="input-76-2-76"]')
          milton.click()
          time.sleep(0.5)

          #Appointment select
          appointment_slct = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div/article/div/div/div[2]/div/div/div[4]/article[2]/div[2]/p/div/div/lightning-combobox/div/lightning-base-combobox/div')
          appointment_slct.click()
          time.sleep(0.1)

          #Date select
          date = driver.find_elements_by_xpath('//*[@role="option"]')[7]
          month = date.text.split(' ')[0]
          day = int(date.text.split(' ')[1].split(",")[0])

          print(f"{month} {day} --------------------")

          if month == 'December' and day == 21:
               date.click()
               break
          else:
               date.click()
               location_slct.click()
               time.sleep(0.1)
               halton_hills = driver.find_element_by_xpath('//*[@id="input-76-1-76"]')
               halton_hills.click()

     except:
          continue


time_btn = driver.find_elements_by_xpath('//*[@type="button"]')[3]
time_btn.click()

submit_btn = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div/article/div/div/div[2]/div/div/div[4]/div/div[2]/button')
submit_btn.click()