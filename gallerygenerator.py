import os, sys

def htmlgenerator(directory):

    for file in os.listdir(directory):
        print('\t\t<div class="galleryWrap">')
        print('\t\t\t<img src="./images/gallery/thumbnails/' + file + '"/>')
        print('\t\t\t<div class="galleryOverlay">')
        print('\t\t\t\t<a href="./images/gallery/thumbnails/' + file + ' data-title="Before the evening performance" data-lightbox="gallery"><span class=galleryLocation><br />Zhengzhou</span><span class=galleryDate><br />May 2017</span></p></a>')
        print('\t\t\t</div>')
        print('\t\t</div>')
	
imagefolder = './images/gallery/thumbnails/'
htmlgenerator(imagefolder)
