from selenium import webdriver


driver= webdriver.Chrome(r"C:\webdrivers\chromedriver.exe")
driver.get('https://web.whatsapp.com/')

name = input('Name of the group or the user: ')
msg=input("enter your message: ")
count=int(input("enter the count: "))

input('enter anything after scanning the qr code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")


for i in range(count):
    msg_box.send_keys(msg)
    button=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
    button.click()
