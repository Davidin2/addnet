#!/usr/bin/python3.8

import cgi
import ipaddress

form= cgi.FieldStorage()
red_add = form.getvalue("red-add")
red_delete = form.getvalue("red-delete")
print ("Content-type:text/html\r\n\r\n")
print("<html><body>")



if red_add:
    try:
        ip = ipaddress.IPv4Network(red_add)
        addfile=open("/home/ubuntu/fiber/cola_nuevos_rangos.txt", "a")
        addfile2=open("/home/ubuntu/fiber/cola_nuevos_rangos_hist.txt", "a")
        print(str(red_add), file=addfile)
        print(str(red_add), file=addfile2) 
        addfile.close()
        addfile2.close() 
        print(ip, " is a correct network. Network added") 
    except ValueError:
        print(red_add, " is a incorrect network. Not added")
    

if red_delete:
    try:
        ip = ipaddress.IPv4Network(red_delete)
        deletefile=open("/home/ubuntu/fiber/cola_borrar_rangos.txt", "a")
        deletefile2=open("/home/ubuntu/fiber/cola_borrar_rangos_hist.txt", "a") 
        print(str(red_delete), file=deletefile)
        print(str(red_delete), file=deletefile2)
        deletefile.close()
        deletefile2.close()

        print(ip, " is a correct network. Network deleted")
    except ValueError:
        print(red_delete, " is a incorrect network. Not deleted")

print("""<br><br><a href="http://ping.davidin.com/fiber/add.html">Go for other</a>""")
print("</body></html>")


