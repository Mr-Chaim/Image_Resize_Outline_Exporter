# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 23:11:53 2017

@author: samir
"""

import cv2
import csv
import numpy as np
from numpy import array

np.set_printoptions(threshold=np.inf)
a = 10
BLACK = [0,0,0]
imgPath = 'C:\\CSVFiles\\SourcePics\\jpegs\\porsche-thumbwhite'
imgEdgesMap = (imgPath + 'edges.png')
img = cv2.imread(imgPath + '.jpg')
gray1 = cv2.Canny(img, 200, 200)

cv2.imwrite(imgEdgesMap, gray1)
img2 = cv2.imread(imgEdgesMap)    

numRows = len(img)
numCols = len(img[0])

if numRows > numCols:
    squareSize = numRows
    topBottom = (squareSize - numCols)/2
    squareEdgesFull = cv2.copyMakeBorder(img2,0,0,topBottom,topBottom, cv2.BORDER_CONSTANT, value=BLACK)
    cv2.imwrite(imgEdgesMap, squareEdgesFull)
    
else:
    squareSize = numCols
    topBottom = (squareSize - numRows)/2
    squareEdgesFull = cv2.copyMakeBorder(img2,topBottom,topBottom,0,0, cv2.BORDER_CONSTANT, value=BLACK)
    cv2.imwrite(imgEdgesMap, squareEdgesFull)

def csvWriter():
    img3 = cv2.imread(dst2)
    imgPathCSV = open((imgPath + str(a) + 'by' + str(a) + '.csv'),"w+")
    writeToCsv = csv.writer(imgPathCSV, lineterminator = '\n')
    firstItemFound = 0
    for r in xrange (0,a):
        for c in xrange (1,a):
            if int(img3[r][a-c][1]) >= 1:
                if firstItemFound == 0:
                    firstItemFound = 1
                    row = r
                    column = c
                writeToCsv.writerow([(a-c)-column,(a-r)-row])
                break         
    for r2 in xrange (1,(a)):
        for c2 in xrange (0,(a)):
            if (img3[a-r2][c2][1]) >= 1:
                #print c2
                #print column
                writeToCsv.writerow([((c2)-column),((r2)-row)])
                break    
    imgPathCSV.close
        
    

while a<=50:
    dst2 = (imgPath + str(a) + 'by' + str(a) + '.png')
    dsize = (a,a)
    small = cv2.resize(img2,dsize, interpolation= cv2.INTER_AREA)
    cv2.imwrite (dst2, small)
    img3 = cv2.imread(dst2)
    csvWriter()
    a+=10