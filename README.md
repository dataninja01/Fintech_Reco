# Fintech_Reco
Mini captstone mid-term project of Mani Nagaraj & Sperks

Details of deployment:
    -Front-end using Flask API with html forms and css styling
    -Submit text through website for sentiment analysis 
    -ML Model accepts text from HTML form
    -Text Classification using TfidfVectorizer, LinearSVC 
    -Returns the positive or negative assesment to the user
   
The model behind the scenes: 
    -Downloads IMDB movie data set from Hugging Face
    -Uses the training data to build the ML model
    -Preprocesses data using TfidfVectorizer and builds classification model using LinearSVC
 
This application has been Dockerized :-)  