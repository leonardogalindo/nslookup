#! /home/me/developer/nslookup/nslookup/bin/python3


"""

nslookup.py [main.py] - Busca os tipos de entrada de zona dns do domínio

Autor       : Leonardo Galindo <dev@leonardogalindo.xyz>
Manutenção  : Leonardo Galindo

Esse programa recebe como parâmetro um domínio, onde será retornado os dados da zona de dns.

Exemplo:
Domínio: LOCAWEB.COM.BR
Criado: 12/01/98
Alterado: 13/12/21
Expiração: 12/01/23
:::::::::::::::::::::::::::::

SERVIDORES DNS:  NS1.locaweb.com.br.
SERVIDORES DNS:  NS3.locaweb.com.br.
SERVIDORES DNS:  NS2.locaweb.com.br.

Tipo A:
Endereço: locaweb.com.br
IP: 189.126.100.6
Nenhum HOSTNAME encontrado.

Organização:
Locaweb Serviços de Internet S/A

Tipo MX:
locaweb-com-br.mail.protection.outlook.com. - PRIORIDADE[0]

Tipo CNAME:
Nenhum registro CNAME encontrado.

Tipo TXT:
TXT: "google-site-verification=xvZKKCCcdrR4loCuKhSrGiDZNqlL5nu3vb_RIPFXVxU"
TXT: "google-gws-recovery-domain-verification=38998679"
TXT: "cloudflare-verify.locaweb.com.br=359738182-332152024"
TXT: "0d65707d6a5d4a8f5cf3ac6402c5cd96.locaweb.com.br"
TXT: "facebook-domain-verification=03em5wq0f0jaii0zxrqger8vdqq4xv"
TXT: "v=spf1 include:spf.protection.outlook.com include:_spflw.locaweb.com.br include:_spflw2.locaweb.com.br -all"

Tipo SOA:
SOA:  ns1.locaweb.com.br. hostmaster.locaweb.com.br. 2022031001 3600 600 1209600 3600


Histórioco:

Licença GPL.	
	

"""

import sys # https://docs.python.org/3/library/sys.html#module-sys

# a função domain_name_registration, foi importada do módulo: domain_whois
from domain_whois import domain_name_registration

# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    if not len(sys.argv) == 2: # esta condição verifica o tamanho da lista. Se o argumento foi passado corretamente, será alterado para falso para executar o else.   
        print('Argumento inválido. Tente novamente.')            
    else:
        domain = sys.argv[1] # variável domínio irá receber o valor na posição 1 da lista. Esse valor será capturado na entrada de dados          
        domain_name_registration(domain)       