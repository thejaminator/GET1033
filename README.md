# GET1033

"Hey man, that guy really has that biz kid vibes!"
Ever wondered if we can tell a person's faculty from their face?

This repo serves to create an average face of NUS students. Later I sort it according to faculty and try to build a predictive model to test if there are certain features that we can use to distinguish between faculties.
The scrapper may not work anymore - it was made around 1 year ago 

<img src="https://averageface.files.wordpress.com/2018/11/50_females1.gif" alt="drawing" width="300"/>

Read the full story [here](https://averageface.wordpress.com/)



# Workflow
Office 365 scrapper and IVLE scrapper ---> sorter -----> landmark creator ------> average face creator

# Landmark creator
scripts/landmark_creator.py 

Requires shape_predictor_68_face_landmarks.dat to run with contains the weights for landmark detection. Also, you need to install dlib
To run, just input the directory of the photos. Will output .txt files required for makeaverage.py.

Adapted from [here](https://github.com/andrewjeminchoi/simple-face-average)

# Average face creator
scripts/makeaverage.py

Requires opencv. To run, just input the directory of the photos. Requires pre-generated .txt files from the landmark creator. It will ask for the number of randomed sample photos. If you want to use all the photos in the directory, input "0".
This script differs from the script from andrewjeminchoi's as instead of taking in all .jpg, it will find the .txt files and then match with the corresponding .jpg file. This prevents the script crashing when a .jpg file does not have an accompanying .txt file.

The resultant average image will be created in the current working directory with the filename of the parents, appended with the parent of the parent directory.

Adapted from [here](https://github.com/andrewjeminchoi/simple-face-average)


# IVLE scrapper
scripts/ivle_scrapper.py

Input the image url you would like to start bruteforce scrapping for face images.
Update: not sure if IVLE has been totally deprecated which breaks this script.

# Office 365 scrapper
scripts/office_scrapper.py

Uses table.csv to append the results of the scrapping. Requires the security token of a signed in session on Office 365 email.

# Sorter
scripts/sorter.py

Input the directory of the scrapped pictures. Requires the table from the Office 365 scrapper to compare the NUSNET ID of the image files to the table, and sort them into respective faculties.


