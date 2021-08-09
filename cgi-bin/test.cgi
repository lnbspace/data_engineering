#!/usr/bin/python3

import cgi,cgitb,time,subprocess,os


cgitb.enable()

print("Content-type: text/html")
print("")
out=subprocess.getoutput('date')
print("<pre>")
print(out)
print("</pre>")
