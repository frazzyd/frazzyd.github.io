# Script:    webpage_search.py
# Author:    Fraser Dumayne
# Created:   29/06/2017
# Desc:      Search a given webpage for a given search term using BeautifulSoup.

import sys, bs4, urllib2
        
def webSearch(url, searchTerm):
    
    try:
        webpage = urllib2.urlopen(url).read() # Open the webpage
        pageContents = bs4.BeautifulSoup(webpage, "html.parser") # Collect contennts of webpage
        pageOutput = pageContents.get_text()# Get just the plaintext of the webpage

        if searchTerm in pageOutput: # Search for the word on the webpage
            print "Your search term, " + searchTerm + ", was successfully located."
        else:
            print "Your search term, " + searchTerm + ", was not found."
            
    except IOError as error: # Provide error if URL cannot be located
        print 'Exception: URL not found: ' + str(error)
    except Exception as error: # Catch all other errors
        print 'Exception: ' + str(error)

    return

def main():
    sys.argv.append(r'http://www.fraserdumayne.co.uk')
    sys.argv.append('Fraser')
    
    if len(sys.argv) != 3:
        print 'Please enter a valid URL (e.g. \'http://www.fraserdumayne.co.uk\') and a valid search term'
        return

    webSearch(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()
