# Script:    imdbcastinfo.py
# Author:    Fraser Dumayne
# Created:   03/07/2017
# Desc:      Search for a given film then give related films of the cast and crew.

import sys

try:
    import imdb
except ImportError:
    print 'You need IMDbPY to run this script properly.'
    sys.exit(1)

def filmSearch(filmTitle):
    ''' Search for film titles and pick the top result '''
    
    i = imdb.IMDb() # Shortcut to imdb package
    
    try:
        results = i.search_movie(filmTitle) # Search for the film on IMDb
    except imdb.IMDbError, error: # Error checking
        print "Check your internet connection:"
        print error
        sys.exit(3)

    if not results: # Check that results were actually found
        print 'No matches were found for ' + filmTitle
        sys.exit(0)
    else:
        film = results[0] # Select first result from search
        i.update(film) # Obtain information from first result

    print 'Cast and crew information for ' + filmTitle + ' are as follows:\n'
    print 'Actor(s):'
    filmCast(film) # Continue to cast function to find top 3 actors latest films
    print '\nDirector(s):'
    filmDirector(film) # Continue to director function to find directors latest films
   
def filmCast(film):
    ''' Take a film and produce information on the top 3 cast members '''

    i = imdb.IMDb() # Shortcut to imdb package

    try:
        
        castAll = film['cast'] # Get entire cast
        castMain = castAll[:3] # Get top 3 actors

        for actor in castMain: # Loop through top 3 actors
            
            actorID = i.get_imdbID(actor) # Get actor ID
            actorInfo = i.get_person(actorID) # Get actor information based on ID
        
            lastThree = actorInfo.get('actor') or actorInfo.get('actress') # Get the films that they have acted in

            print '\n%s (%s) most recently starred in:' % (actorInfo['name'], actor.currentRole)

            for film in lastThree[:3]:
                print '%s (%s)' % (film['title'], film.get('year'))
                
    except imdb.IMDbError, error:
        print "Check your internet connection:"
        print error
        sys.exit(3)

def filmDirector(film):
    ''' Take a film and produce information on the director '''

    i = imdb.IMDb() # Shortcut to imdb package
    
    try:
        
        directors = film['director'] # Select the director(s) of the film
        
        for director in directors: # Loop through director(s)
            directorID = i.get_imdbID(director) # Get director ID
            directorInfo = i.get_person(directorID) # Get director information based on ID

            lastThree = directorInfo.get('director') # Get the films that the person has directed

            print '\n%s most recently directed:' % (directorInfo['name'])
            
            for film in lastThree[:3]:
                print '%s (%s)' % (film['title'], film.get('year'))
                
    except imdb.IMDbError, error:
        print "Check your internet connection:"
        print error
        sys.exit(3)
                
def main():
    #sys.argv.append('Lost in Translation') # Test Case

    if len(sys.argv) != 2:
        print "Please enter a valid film title"
        return

    filmSearch(sys.argv[1])

if __name__ == '__main__':
    main()
