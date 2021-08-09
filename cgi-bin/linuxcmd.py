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

print("<h1> Hello running linux command given by you </h1>")
cmd=webdata.getvalue('c')
# run command 

out=subprocess.getoutput(cmd)
print("<pre>")
print(out)
print("</pre>")
print('<meta http-equiv="refresh" content="5;url=http://3.81.114.88/linuxcmd.html" />')


