#!/usr/bin/python3.8

import cgi
import ipaddress

def anade_a_fichero(fichero,cadena):
    try:
        with open(fichero, "a") as f:
            print(str(cadena), file=f)
    except (OSError, IOError) as e:
        print ("Error abriendo el fichero, no se cargara"+str(fichero))



form= cgi.FieldStorage()
red_add = form.getvalue("red-add")
red_delete = form.getvalue("red-delete")
print ("Content-type:text/html\r\n\r\n")
print("<html><body>")



if red_add:
    try:
        ip = ipaddress.IPv4Network(red_add)
        anade_a_fichero("/home/ubuntu/fiber/cola_nuevos_rangos.txt",red_add)
        anade_a_fichero("/home/ubuntu/fiber/cola_nuevos_rangos_hist.txt",red_add)
        print(ip, " is a correct network. Network added") 
    except ValueError:
        print(red_add, " is a incorrect network. Not added")
    

if red_delete:
    try:
        ip = ipaddress.IPv4Network(red_delete)
        anade_a_fichero("/home/ubuntu/fiber/cola_borrar_rangos.txt",red_delete)
        anade_a_fichero("/home/ubuntu/fiber/cola_borrar_rangos_hist.txt",red_delete) 
        print(ip, " is a correct network. Network deleted")
    except ValueError:
        print(red_delete, " is a incorrect network. Not deleted")

print("""<br><br><a href="http://ping.davidin.com/fiber/add.html">Go for other</a>""")
print("</body></html>")


