import bs4
import requests # import requests or you can use urllib for the same purpose
import time


# lets get the data from webpage in text format using requests library
request = requests.get('https://countrycode.org/').text

# now use beautifull soup to get the html elements 
soup = bs4.BeautifulSoup(request, 'lxml')

# as we are using countrycode.org this site has data in tbody tag so lets find this tag
table = soup.find('tbody')

# as it is a html table we need to fetch the rows that is tr tag find that
countries = table.find_all('tr')

# lets save the data in dictionary so that we don't have to run the site again and again we will fetch data from this
# dictionary
data_dict = {}

# as each row (tr) has number of td elements, we have to run loop on it 
for i in countries:
    
    # now find all td elements in tr
    data = i.find_all('td')
    # save that data in dictionary
    data_dict[data[0].text] = data[1].text
    
print('* Country Code Finder *')
print()
time.sleep(0.5)
while(True):
    x = input('Enter country name = ')
    for i in data_dict.keys():
        if x.lower()==i.lower():
            print(data_dict[i])
            break
    time.sleep(0.5)    
