# Fintech_Reco
##Mini captstone mid-term project of Mani Nagaraj & Sperks

###Details of deployment:
    -Front-end using Flask API with html forms and css styling
    -Submit text through website for sentiment analysis 
    -ML Model accepts text from HTML form
    -Text Classification using TfidfVectorizer, LinearSVC 
    -Returns the positive or negative assesment to the user


###The model behind the scenes: 
    -Downloads IMDB movie data set from Hugging Face
    -Uses the training data to build the ML model
    -Preprocesses data using TfidfVectorizer and builds classification model using LinearSVC
    ![image](https://user-images.githubusercontent.com/46502113/147180782-2ad51bea-7e32-45d7-a8e1-b2c2f7ace6b6.png)

 
###This application has been Dockerized :-) 
Steps to deploy container are:
Clone this repo & change directory into repo, then run these two commands-
```
docker build -t minicap .
docker run -p 8000:5000 minicap
```
