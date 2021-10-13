# Script:    twitteranalyse.py
# Author:    Fraser Dumayne
# Created:   06/07/2017
# Desc:      Search for a given term/username then return a graphical representation of the most commonly used words in tweets containing the given term/username.

import sys, operator
reload(sys)
sys.setdefaultencoding('utf8')

# Test if Tweepy exists on user computer
try:
    import tweepy
except ImportError:
    print 'You need Tweepy to obtain search results from Twitter'
    sys.exit(1)

# Test if matplotlib exists on user computer
try:
    import matplotlib.pyplot as graphPlot
except ImportError:
    print 'You need matplotlib to obtain a graph of your search results.'
    sys.exit(1)

def searchTwitter(searchTerm):
    ''' Search Twitter for a key word and save results'''

    # Authorization Keys to use Tweepy - Gained from https://apps.twitter.com/
    consumer_key = 'YOUR-CONSUMER-KEY-HERE'
    consumer_secret = 'YOUR-CONSUMER-SECRET-HERE'
    access_token =  'YOUR-ACCESS-TOKEN-HERE'
    access_secret = 'YOUR-ACCESS-SECRET-HERE'
    # Authorization Commands
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    searchResults = tweepy.API(auth).search(searchTerm) # Search Twitter for the given term

    with open('searchResults', 'w') as fileResults: # Create a new file to store tweets from search results
        for result in searchResults[:200]: # Store first 100 results from Twitter
            fileResults.write(result.text.lower()+'\n') # Lower case to stop words from being counted multiple times

    analyseFrequency('searchResults', searchTerm)

def analyseFrequency(filename, searchTerm):
    ''' Analyse text document for words and their frequency'''

    wordList = [] # Initialise list to store words after removing the stop words

    # Basic list to filter stopwords and stop the search term from appearing in results
    stopwords = ['if', 'i', 'rt', 'i', 'and', 'you', 'will', 'too', 'to', 'in', 'our', 'a',
                 'we', 'here', 'the', 'is', 'of', 'see', 'all', 'is', 'he', 'she', 'they',
                 'them', 'this', 'those', '.', ',', 'about', 'be', 'that', 'get', 'called',
                 'on', 'because', 'just', 'for', 'you\'re', 'from', '-', '+', 'as', 'has', ' ',
                 searchTerm]

    searchDictionary = {} # Create dictionary to store words and their frequency

    try:
        fileResults = open(filename, 'r') # Open the text file
        fileText = fileResults.read()  # Read the file
        fileWords = fileText.split()  # Split the file into seperate words
    except:
        print 'The file you are trying to find does not exist.'
        sys.exit(0)

    for word in fileWords: # Iterate through tweets
        if word not in stopwords: # Disallow stop words from being added to the list
            wordList.append(word)

    for wordNoStop in wordList: # Iterate through list without stop words
        searchDictionary.update({wordNoStop:wordList.count(wordNoStop)}) # Add words and their respective frequencies to a dictionary

    resultsGraph(searchDictionary)

def resultsGraph(searchDictionary):
    ''' Plot the most common words on a graph '''

    searchDictionary = dict(sorted(searchDictionary.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]) # Obtain the 10 most common words

    graphPlot.suptitle('Most Common Words', fontsize=16) # Give the graph a title
    graphPlot.xlabel('Words', fontsize=14) # Give the X-Axis a label
    graphPlot.ylabel('Frequency', fontsize=14) # Give the Y-Axis a label
    graphPlot.bar(range(len(searchDictionary)), searchDictionary.values(), align='center') # Create Bar Chart
    graphPlot.xticks(range(len(searchDictionary)), searchDictionary.keys(), rotation=45) # Give values for X-Axis

    graphPlot.show() # Show the graph to the user

def main():
    #sys.argv.append('scotland') # Test case

    if len(sys.argv) != 2:
        print "Please enter a valid search term"
        return

    searchTwitter(sys.argv[1].lower())

if __name__ == '__main__':
    main()
