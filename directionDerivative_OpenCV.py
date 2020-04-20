import cv2
import numpy
import matplotlib

def main():
    # Use this syntax to import an image
    imgPath = ""
    input1 = imgInput(imgPath)
    
    # Use this function to preview the output
    imgDisplay(input1)
    
def imgInput(imgPath):
    importedIMG = cv2.imread(imgPath, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
    return(importedIMG)
    
def imgDisplay(displayIMG):
    cv2.imshow('PREVIEW', displayIMG)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
    
if __name__ == "__main__":
    main()