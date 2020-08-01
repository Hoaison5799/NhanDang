# Main.py

import cv2
import numpy as np
import os

import DetectChars
import DetectPlates
import PossiblePlate

# module level variables ##########################################################################
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

showSteps = True
imgOriginalScene = cv2.imread("bike_back/6.jpg")

###################################################################################################
def Find(imgOriginalScene):

    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()         # attempt KNN training

    if blnKNNTrainingSuccessful == False:                               # if KNN training was not successful
        print("\nerror: KNN traning was not successful\n")  # show error message
        return                                                          # and exit program
    # end if


    if imgOriginalScene is None:                            # if image was not read successfully
        print("\nerror: image not read from file \n\n")  # print error message to std out
                                     # pause so user can see error message
        return                                              # and exit program
    # end if

    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates

    listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates

   # cv2.imshow("imgOriginalScene", imgOriginalScene)            # show scene image
    Chars = None
    if len(listOfPossiblePlates) == 0:                          # if no plates were found
        print("\nno license plates were detected\n")  # inform user no plates were found
    else:                                                       # else
                # if we get in here list of possible plates has at leat one plate

                # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
        listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
        licPlate = listOfPossiblePlates[0]
        if len(listOfPossiblePlates) <= 1:
            licPlate_1 = ""
        else: licPlate_1 = listOfPossiblePlates[1]
     #   cv2.imshow("imgPlate", licPlate.imgPlate)           # show crop of plate and threshold of plate
    #    cv2.imshow("imgThresh", licPlate.imgThresh)

        if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
            print("\nno characters were detected\n\n")  # show message
            return                                          # and exit program
        # end if

      #  drawRedRectangleAroundPlate(imgOriginalScene, licPlate)             # draw red rectangle around plate

        Chars = licPlate.strChars +" "+ licPlate_1.strChars
        if (len(licPlate.strChars) > len(licPlate_1.strChars)):
            Chars = licPlate_1.strChars +" "+ licPlate.strChars
        print("\nlicense plate read from image = " + Chars + "\n")  # write license plate text to std out
        print("----------------------------------------")

       # cv2.imshow("imgOriginalScene", imgOriginalScene)                # re-show scene image
     #   cv2.imwrite("imgOriginalScene.png", imgOriginalScene)  # write image out to file
    # end if else
    return Chars
# end main



###################################################################################################
if __name__ == "__main__":
    Find(imgOriginalScene)


















