# -*- coding: utf-8 -*-
"""
khashayar_jamshidi@yahoo.com

@author: khashayar-jamshidi
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
###################     
class Instagram_Meta_Unfollow  :
    ###################     
    def __init__ (self,username,password):
        self.username = username
        self.password = password
        self.driver =  webdriver.PhantomJS()
        #self.driver =  webdriver.Firefox()
    ###################     
    def  CloseBrowrse(self):
        self.driver.close()
    ###################     
    def login (self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
       # driver.get('https://www.instagram.com/accounts/login/?source=reset_password')
        time.sleep(random.randint(Time_A,Time_B))
        user_name_box = driver.find_element_by_xpath("//input[@name='username']")
        user_name_box.clear()                                             
        user_name_box.send_keys(self.username)
        password_box = driver.find_element_by_xpath("//input[@name='password']")
        password_box.clear()
        password_box.send_keys(self.password)
        time.sleep(random.randint(3,10))
        password_box.send_keys(u'\ue007')
        time.sleep(random.randint(Time_A,Time_B))
        driver.get('https://www.instagram.com/'+username+'/')
        ################
        print("REDY PASSWORD & USERNAME") 
        scheight = .001
        while scheight < x:
            try:
                time.sleep(random.randint(Time_A,Time_B))
                driver.find_element_by_xpath('.//*[@href="/only.fire.god/following/"]').click()            
                time.sleep(random.randint(Time_A,Time_B))                      
                driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[3]/div/div[2]/div[1]/div/div/a').click()                
                print(driver.current_url)                    
                time.sleep(random.randint(Time_A,Time_B))
                driver.find_element_by_xpath('.//*[@aria-label="Following"]').click()            
                time.sleep(random.randint(Time_A,Time_B))              
                driver.find_element_by_xpath('.//*[@class="aOOlW -Cab_   "]').click()
                driver.get('https://www.instagram.com/'+username+'/')
                scheight += .001 
            except Exception as e:
                 time.sleep(3)
            
###################     
#x= .10 or.999
x=.50
###################     
#time
#smailtime Time_A <Time_B
Time_A = 8
#bigtime
Time_B = 30          
###################     
username = "Username Enter"
password = "password Enter"
###################
ig = Instagram_Meta_Unfollow(username, password)
ig.login()        
###################
while True:
    try:
        unf = random.choice(username)
        ig.unfollow_Meta(unf)                
    except Exception:
        ig.CloseBrowrse()
        time.sleep(20)
        ig = Instagram_Meta_Unfollow(username,password)
        ig.login()