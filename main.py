import pandas as pd
from datetime import datetime
from commons.csv_writer import CSVWriter

from driver.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

import random
from time import sleep
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import constants
import id


def login(driver):
    """Function to login to the linkedin"""
    driver.find_element(id.login_email,'css_selector').send_keys(os.environ.get('email'))
    sleep(2)
    driver.find_element(id.login_password,'css_selector').send_keys(os.environ.get('password'))
    sleep(2)
    driver.find_element(id.signin_button).click()
    sleep(5)


def getUserDetails(i, link):
    """get user details"""
    name=dr.find_element(id.name,'class_name').text
    description=dr.find_element(id.description,'class_name').text
    dr.load_url(link + 'detail/contact-info/')
    try:
        phone=dr.find_element(id.phone_number,'class_name').text
        phone = ''.join(phone.split()[1:])
        phone=phone.replace('(Mobile)','')
        phone=phone.replace('(Home)','')
    except:
        phone = ""
    try:
        email=dr.find_element(id.email,'class_name').text
        email = email.split()[1]
    except:
        email = ""
    df.at[i, "Description"] = description
    df.at[i, "Email Address"] = email
    df.at[i, "Phone Number"] =phone
    df.at[i,'Attempt Date']=datetime.today().date()
    df.at[i,'Profile link'] =link
    print("###########################")
    print("Name: " + name)
    print("Description: " + description)
    print("Email: " + email)
    print("Phone: " + phone)
    print()
    connectionsCSV.save_csv()

if __name__ == "__main__":
    dr = WebDriver()
    dr.load_url('https://www.linkedin.com/')
    connectionsCSV = CSVWriter(constants.CSV_FileName)
    login(dr)

    limit=random.randint(constants.User_MIN_WAIT,constants.User_MAX_WAIT)
    count=int(connectionsCSV.totalToday())
    df=connectionsCSV.read_csv()
    for i in range(len(df)):
        try:
            if count>limit:
                break
            if pd.isnull(df.loc[i,'Attempt Date']) and not 'Error' in df.loc[i,'Message']:
                query=df.loc[i,'First Name']+' '+df.loc[i,'Last Name']+' '+df.loc[i,'Company']
                query=query.replace('nan', '')
                dr.find_element(id.search).clear()
                dr.find_element(id.search).send_keys(query)
                sleep(2)
                dr.find_element(id.search).send_keys(Keys.ENTER)
                sleep(random.randint(5, 10))
                dr.find_element(id.profile_link_search,'class_name').click()
                sleep(random.randint(7, 15))
                getUserDetails(i,dr.currentURL)
                count += 1
                sec=random.randint(constants.User_MIN_WAIT,constants.User_MAX_WAIT)
                print("Sleep for " + str(sec) + " seconds")
                sleep(sec)
        except KeyboardInterrupt:
            print('Thank You')
            print(f"Total {count} user scrapped successfully today")
            break
        except Exception as e:
            df.at[i,'Message']='Error: '+str(e)
            print(e)






