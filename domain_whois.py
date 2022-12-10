#! /home/me/developer/nslookup/nslookup/bin/python3

# pip install python-whois

import whois
from datetime import date as dt
from domain_nslookup import nslookup

def domain_name_registration(domain):
    w = whois.whois(f"{domain}")
      
    if w.domain_name == None:
        print('Domínio não registrado. Tente novamente.')
    else:
        domain_name(w)
        creation_date(w)
        updated_date(w)
        expiration_date(w)        
        nslookup(domain)


def domain_name(value):
    print(":" * (len(value) + 10))
    if isinstance(value.domain_name, str):
        print("Domínio:",value.domain_name.upper())
    else:
        domain_name = list(value.domain_name)
        print("Domínio:",domain_name[0])   

    
def creation_date(value):     
    if isinstance(value.creation_date, dt):
        print("Criado:",value.creation_date.strftime("%d/%m/%y"))
    else:
        print("Criado:",value.creation_date[0].strftime("%d/%m/%y"))


def updated_date(value):     
    if isinstance(value.updated_date, dt):
        print("Alterado:",value.updated_date.strftime("%d/%m/%y"))
    else:
        print("Alterado:",value.updated_date[0].strftime("%d/%m/%y"))


def expiration_date(value):    
    if isinstance(value.expiration_date, dt):
        print("Expiração:",value.expiration_date.strftime("%d/%m/%y"))
    else:
        print("Expiração:",value.expiration_date[0].strftime("%d/%m/%y"))

    print(":" * (len(value) + 10))