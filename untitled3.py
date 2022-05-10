# -*- coding: utf-8 -*-
"""
Created on Tue May 10 07:49:48 2022

@author: Alumno
"""
acl=int(input("ingrese el # de ACL: "))
if acl>=1 and acl<=199:
    print("es un acl estandar: ")
elif acl>=100 and acl>=199:
    print(" es un acl extendida")
else: 
    print("el # ingresado no es de un acl")
