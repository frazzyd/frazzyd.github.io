import os, sys

def htmlgenerator(directory):

    for file in os.listdir(directory):
        print '\t\t<div class="galleryWrap">'
        print '\t\t\t<img class="galleryImage" src="./images/gallery/fullsize/' + file + '.jpg" />'
        print '\t\t\t<div class="galleryOverlay">'
        print '\t\t\t\t<a href="./images/gallery/fullsize/' + file + ' data-title="Before the evening performance" data-lightbox="gallery"><p class="galleryDescription">Before the evening performance<span class=galleryLocation><br />Zhengzhou</span><span class=galleryDate><br />May 2017</span></p></a>'
        print '\t\t\t</div>'
        print '\t\t</div>'
	
imagefolder = './images/gallery/fullsize/'
htmlgenerator(imagefolder)
