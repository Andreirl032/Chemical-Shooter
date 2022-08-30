from os import walk
import pygame

def importfolder(path):
    surfacelist=[]

    for _,__,imgfiles in walk(path):
        for image in imgfiles:
            fullpath=path + '/' + image
            imagesurface=pygame.image.load(fullpath).convert_alpha()
            surfacelist.append(imagesurface)
    return surfacelist       