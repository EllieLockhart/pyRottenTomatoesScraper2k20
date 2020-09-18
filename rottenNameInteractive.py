# Interactive Movie Name Query for pyRottenTomatoesScraper2k20
# the purpose of this project is to provide an interactive interface by which
# the user can conduct scraping based queries (no official or authorized)
# APIs are used due to Rotten Tomatoes strict restrictions on researcher
# use of their data, which undermines data scientists' access to 
# information on the public reception of films

# all pyRottenTomatoesScraper2k20 code is subject to GPL3, license in repo
# copyright Eleanor A. Lockhart 2020
# PURPOSE OF THIS PYTHON SCRIPT: provides an interactive query interface
# by which the user can find out the ID/URL of a Rotten Tomatoes entry
# for a particular film so that further scraping queries can be attempted

# basic imports from libraries
#from lxml.html.soupparser import fromstring
# root = fromstring(tag_soup)
from bs4 import BeautifulSoup
import requests

# introductory script prints to console
print("Interactive Movie Name Query Script")

findMovie=1
# first we need to find out what film the user wants to get the RT URL for
while findMovie is 1:
    print("Name of film to be queried:")
    filmQueryName=input()
    rtSearchURL="https://www.rottentomatoes.com/search?search="+filmQueryName
    nowQueryBS4URL=rtSearchURL

    # fetch raw HTML from Rotten Tomatoes search page for the film title
    # being queried
    html_content = requests.get(rtSearchURL).text

    # parse the RottenTomatoes results into readable form
    soup = BeautifulSoup(html_content)
    print(soup.text)
    results = soup.find_all("a", {"data-qa" : "info-name"})
    print(len(results))
    print(rtSearchURL)