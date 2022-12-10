#! /home/me/developer/nslookup/nslookup/bin/python3

import sys
from domain_whois import domain_name_registration


if __name__ == "__main__":

    if not len(sys.argv) == 2:        
        print('Argumento inválido. Tente novamente.')            
    else:
        dominio = sys.argv[1]           
        domain_name_registration(dominio)       