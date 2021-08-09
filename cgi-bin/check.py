#!/usr/bin/python3

import  cgi
import  cgitb
import  time
import  subprocess

cgitb.enable() # to show error in CGI progrm  in your web portal 

# to accept data from  web httpd server 
webdata=cgi.FieldStorage()
print("Content-Type: text/html") # this response is comming from httpd server 
print("")

print("<h1> Hello CGI  </h1>")
# my login DB 
login={'user':'lnb','password':'LnbDevops'}
#print(webdata)
# only extracting data 
username=webdata.getvalue('u')
pass1=webdata.getvalue('p')
# checking  auth 

if  username ==  login['user']  and  pass1  == login['password']  :
    print("logged IN successfully.....")
    print("now you can access project page..")
    print("please wait...")
    print('<meta http-equiv="refresh" content="1;url=http://3.81.114.88/list.html" />')

else :
    print("check your user name and password ")
    print(" you can try again...")
    time.sleep(1)
    print('<a href="http://3.81.114.88/"> click to try again </a>')



