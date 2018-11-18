# GET1033

This repo serves to create an average face of NUS students.

<img src="https://averagefaces.files.wordpress.com/2018/11/50_females1.gif" alt="drawing" width="300"/>

Read the full story [here](https://averagefaces.wordpress.com/2018/11/16/the-results/)
Watch the video [here](https://www.youtube.com/watch?v=Ohfu2fE8yeo)


# Workflow
Office 365 scrapper and IVLE scrapper ---> sorter -----> landmark creator ------> average face creator

# Landmark creator
scripts/landmark_creator.py 

Requires shape_predictor_68_face_landmarks.dat to run, dlib. (google it). 
To run, just input the directory of the photos. Will output .txt files required for makeaverage.py.

Adapted from [here](https://github.com/andrewjeminchoi/simple-face-average)

# Average face creator
scripts/makeaverage.py

Requires opencv. To run, just input the directory of the photos. Requires pre-generated .txt files from the landmark creator. It will ask for the number of randomed sample photos. If you want to use all the photos in the directory, input "0".

The resultant average image will be created in the current working directory with the filename of the parents, and the parent of the parent directory.


# IVLE scrapper
scripts/ivle_scrapper.py

Input the image url you would like to start bruteforce scrapping.

# Office 365 scrapper
scripts/office_scrapper.py

Uses table.csv to append the results of the scrapping. Requires the security token of a signed in session on Office 365 email.

# Sorter
scripts/sorter.py

Input the directory of the scrapped pictures. Requires the table from the Office 365 scrapper to compare the NUSNET ID of the image files to the table, and sort them into respective faculties.


