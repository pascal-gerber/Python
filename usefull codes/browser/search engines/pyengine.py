import requests
from bs4 import BeautifulSoup
# Make a request to the website
r = requests.get('https://bola.kompas.com/')
# Create an object to parse the HTML format
soup = BeautifulSoup(r.content, 'html.parser')
# Retrieve all popular news links (Fig. 1)
link = []
for i in soup.find('div', {'class':'most__wrap'}).find_all('a'):
    i['href'] = i['href'] + '?page=all'
    link.append(i['href'])
# For each link, we retrieve paragraphs from it, combine each paragraph as one string, and save it to documents (Fig. 2)
documents = []
for i in link:
    # Make a request to the link
    r = requests.get(i)
  
    # Initialize BeautifulSoup object to parse the content 
    soup = BeautifulSoup(r.content, 'html.parser')
  
    # Retrieve all paragraphs and combine it as one
    sen = []
    for i in soup.find('div', {'class':'read__content'}).find_all('p'):
        sen.append(i.text)
  
    # Add the combined paragraphs to documents
    documents.append(' '.join(sen))

print(documents)
