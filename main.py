# A noter, la librairie requests envoie automatiquement les headers encoding gzip et deflate et decode la réponse 
import requests
import re

# Request simple
url = 'https://en0cuocorbcbyp.x.pipedream.net/fichier.txt'
r = requests.get(url)

status_code = r.status_code
headers = r.headers
html = r.text

# Gestion du timeout
url = 'https://en0cuocorbcbyp.x.pipedream.net/timeout.php'
try:
    r = requests.get(url, timeout=0.01)
except requests.exceptions.ConnectTimeout:
    print("TIMEOUT")


# On définie des headers
url = 'https://en0cuocorbcbyp.x.pipedream.net/fichier.txt'
headers = {'user-agent': 'MyBot', 'Referer': 'https://www.facebook.com'}
r = requests.get(url, headers=headers)


# avec authentification
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('login', 'password')
url = 'https://httpbin.org/basic-auth/login/password'
r = requests.get(url, auth=basic)

# avec des paramètres GET
url = 'https://en0cuocorbcbyp.x.pipedream.net/param.php'
params = {'tracking':'analytics', 'print':'1'}
r = requests.get(url, params=params)

# request POST avec params
url = 'https://en0cuocorbcbyp.x.pipedream.net/post_param.php'
params = {'tracking':'analytics', 'print':'1'}
r = requests.post(url, params=params)

# On envoie un fichier
files = {'nom_du_fichier': open('fichier.txt', 'rb')}
url = 'https://en0cuocorbcbyp.x.pipedream.net/post_fichier.php'
r = requests.post(url, files=files)

# on recupère le nombre de redir et l'historique
url = 'https://httpbin.org/absolute-redirect/5'
r = requests.get(url)

if r.history:
    for hist in r.history:
        print(hist.url, hist.status_code)

# Envoyer un cookie
url = 'https://en0cuocorbcbyp.x.pipedream.net/set_cookies.php'
cookies = dict(nom_cookie='valeur_cookie')
r = requests.get(url, cookies=cookies)

# Récupérer les cookies
url = 'https://www.cnn.com/'
r = requests.get(url)
for k, v in r.cookies.items():
    print(k, v)

# Rechercher la présence d'un formulaire
url = 'https://www.python.org'
r = requests.get(url)
html = r.text
if re.search('method="post|get"', html, re.IGNORECASE):
    print('Trouvé')
else:
    print('pas trouvé')

# Récupérer la balise TITLE
url = 'https://www.python.org'
r = requests.get(url)
html = r.text
res = re.search('<title>([^<]+)</title>', html, re.IGNORECASE)
title = res.group(1)