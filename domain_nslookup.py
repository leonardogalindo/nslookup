#! /home/me/developer/nslookup/nslookup/bin/python3

# https://pypi.org/project/requests/


import dns.resolver, dns.reversename
import json
import requests


def ns(value):    
    print()
    try:
        result = dns.resolver.resolve(f'{value}', 'NS')        
        for val in result:
            print('SERVIDORES DNS: ', val.to_text())
    except:        
        print("Nenhum registro NS encontrado.")   
    

def a(value):
    print()
    print("Tipo A:")

    try:
        print(f"Endereço: {value}")
        result = dns.resolver.resolve(f'{value}', 'A')                 
        for val in result:
            ip = val.to_text()               
	
        print('IP:', ip) 
        dns_revername(ip)       
        isp(ip)

    except:
        print("Nenhum registro A encontrado.")  


def dns_revername(ip):
    
    try:
        addrs = dns.reversename.from_address(ip)        
        print("HOSTNAME:",str(dns.resolver.resolve(addrs,"PTR")[0]))
    except:
        print("Nenhum HOSTNAME encontrado.")


def isp(ip):

    # Your API key, available from your account page
    YOUR_GEOLOCATION_KEY = '381150a10dba49658c32c3da24570d4a'
   

    # IP address to test
    ip_address = ip

    response = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=' + YOUR_GEOLOCATION_KEY + '&ip_address=' + ip_address)
    result = json.loads(response.content)

    connection = result['connection']

    print()
    print("Organização:")
    print(connection['organization_name'])
    
    
def mx(value):
    try:
        print()
        print("Tipo MX:")
        answers = dns.resolver.resolve(f'{value}', "MX")        
        for rdata in answers:
            print(rdata.exchange, '-',f"PRIORIDADE[{rdata.preference}]",)
    except:        
        print("Nenhum registro MX encontrado.")

      


def cname(value): 
    print()
    print("Tipo CNAME:") 
    try:       
        result = dns.resolver.resolve(f'{value}', 'CNAME')           
        for a in result:
            print(' CNAME:', a.target)            
    except:
        print("Nenhum registro CNAME encontrado.")    


def txt(value):
    
    print()
    print("Tipo TXT:")
    try:
        result = dns.resolver.resolve(f'{value}', 'TXT')        
        for val in result:
            print('TXT:', val.to_text())
    except:
        print("Nenhum registro TXT encontrado.")

def soa(value):

    print()
    print("Tipo SOA:")
    try:
        result = dns.resolver.resolve(f'{value}', 'SOA')        
        for val in result:
            print('SOA: ', val.to_text())
    except:
        print("Nenhum registro SOA encontrado.")



def nslookup(value):
      
    ns(value)
    a(value)    
    mx(value)
    cname(value)
    txt(value)
    soa(value)