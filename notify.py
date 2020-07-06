import requests
from bs4 import BeautifulSoup

url = 'https://www.mohfw.gov.in' 
url1 = 'https://covid19.karnataka.gov.in/english'
res = requests.get( url )
res1 = requests.get( url1 )
html = res.text
html1 = res1.text

soup = BeautifulSoup( html, 'html.parser' )
soup1 = BeautifulSoup( html1, 'html.parser' )
active_cases = soup.find('li', {'class': 'bg-blue'}).strong.text
cured_cases = soup.find('li', {'class': 'bg-green'}).strong.text
confirmed_cases = int(active_cases)+int(cured_cases)
deaths = soup.find('li', {'class': 'bg-red'}).strong.text

kar_total_cases = soup1.find_all('li', {'class': 'bg-orange'})[1].strong.text

print( 'INDIA \nConfirmed Cases - ' + str(confirmed_cases) + '\nActive Cases - ' + active_cases + '\nDeath - ' + deaths + '\nKARNATAKA - Total Cases - ' + kar_total_cases )

updates = {'Confirmed Cases':confirmed_cases,'Active Cases':active_cases,'Death':deaths,'Total Cases':kar_total_cases}

variables[ 'Updates' ] = updates
