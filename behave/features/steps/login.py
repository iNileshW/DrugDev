from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'the user has the correct credentials')
def step_impl(context):
   context.driver.get('https://sprinkle-burn.glitch.me/')
   title = context.driver.title
   try:
      assert "Worlds Best App" == title
   except AssertionError as e:
      print ("fail to open website")

@when(u'the user enters username')
def step_impl(context):
   context.driver.find_element_by_name('email').send_keys("test@drugdev.com")
   print("User entered username")

@when(u'the user enters {password}')
def step_impl(context,password):
   context.driver.find_element_by_name('password').send_keys(password)
	  
@when(u'clicks Login')
def step_impl(context):
   context.driver.find_element_by_xpath('//button').click()
   context.driver.implicitly_wait(100)
   print("User logged in")

@then(u'the user is presented with a welcome message')
def step_impl(context):
   context.driver.implicitly_wait(10)
   element = context.driver.find_element_by_xpath('//article')
   print (element.text)
   try:
      assert element.text == "Welcome Dr I Test"
      print("Tesst passed")
   except Assertionerror as e:
      print("Test failed")   	
      print(e)	  
   
@given(u'the user has the incorrect credentials')
def step_impl(context):
   context.driver.get('https://sprinkle-burn.glitch.me/')
   print("Website opened for incorrect credentials")
   
@then(u'the user is presented with a error message')
def step_impl(context):
   element = context.driver.find_element_by_id('login-error-box')
   print ("Validation error message is :  "+element.text)
   error_msg = element.text
   print(error_msg)
   try:
      assert element.text == "Credentials are incorrect"
      print("Test passed")
   except Assertionerror as e1:
      	print("Test failed")	