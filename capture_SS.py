from selenium import webdriver
from PIL import Image
url=input("Enter the string value : ")#input the url from the user
Firefoxbrowser = webdriver.Firefox(executable_path='C:\\Users\\Sudhanshu Mishra\\Desktop\\geckodriver.exe')#change the path of driver for implenting running your system
Firefoxbrowser.get(url)#to open the webpage
Firefoxbrowser.save_screenshot('C:\\Users\\Sudhanshu Mishra\\Desktop\\a3.png')#to save the screenshot
Firefoxbrowser.quit()
Size_width=1024#set Width
Size_height=768#set Height
new_img = Image.open('C:\\Users\\Sudhanshu Mishra\\Desktop\\a3.png')#open the image to resize
new_img = new_img.resize((Size_width,Size_height),Image.ANTIALIAS)#resize the image
new_img.save('C:\\Users\\Sudhanshu Mishra\\Desktop\\a3.png')#save the resized image of size 1024*768
