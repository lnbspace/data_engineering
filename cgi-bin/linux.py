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

print("<h1> Hello all i can handle Linux command operations  operations .. </h1>")
print('<meta http-equiv="refresh" content="1;url=http://3.81.114.88/linuxcmd.html" />')



