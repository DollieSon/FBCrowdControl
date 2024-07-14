import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def findAndClick(id):
    try:
        wLogin = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, id)))
    except:
        print(id +" button not found")
        driver.quit()
        exit()
    driver.find_element(By.ID,id).click()

# Initialize the Chrome driver
driver = webdriver.Chrome()
web = "https://www.facebook.com/live/producer/dashboard/327645667081793/COMMENTS/"
passwords = open('passwords.txt', 'r')
uname = passwords.readline()
pword = passwords.readline()
# Navigate to the URL
driver.get(web)
#Login
try:
    wLogin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
except:
    print("Login button not found")
    driver.quit()
    exit()
#find the username box
driver.find_element(By.ID,"email").send_keys(uname)
#find the password box
driver.find_element(By.ID,"pass").send_keys(pword)
#find the login button
findAndClick("loginbutton")
#x1ey2m1c xds687c x17qophe xg01cxk x47corl x10l6tqk x13vifvy x1ebt8du x19991ni x1dhq9h x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m
#//*[@id="mount_0_0_u3"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div


input("Press Enter to continue...")
elem = driver.find_element(By.XPATH,r'//div[@class="x9f619 x78zum5 xdt5ytf x1odjw0f xish69e x1xzabdm xh8yej3"]')


print("Hello World")



# It's a good practice to close the browser when done
driver.quit()

#class = x9f619 x78zum5 xdt5ytf x1odjw0f xish69e x1xzabdm xh8yej3
#article
#class = comment ? Y29tbWVudDozMjc2NDU2NjcwODE3OTNfNDM4NTM5MTI5MTc2NzMz
#x9f619 x78zum5 xdt5ytf x1odjw0f xish69e x1xzabdm xh8yej3
# Text Box class x1y1aw1k xn6708d xwib8y2 x1ye3gou
#x9f619 x78zum5 xdt5ytf x1odjw0f xish69e x1xzabdm xh8yej3