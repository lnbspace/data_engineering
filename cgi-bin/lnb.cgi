#!/usr/bin/python3

import cgi,cgitb,time,subprocess,os


cgitb.enable()

web=cgi.FieldStorage()
cmd=web.getvalue('c')
print("Content-type: text/html")
print("")
print(cmd)
