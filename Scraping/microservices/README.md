# Software 

Table of Contents
=================

* [A Brief Introduction](#a-brief-introduction)
* [Pre requisites](#pre-requisites)
* [Running the API Service](#running-the-api-service)

* [Checking the API](#checking-the-api)



## A Brief Introduction

In this readme the two services are presented, the first one fails because walmart has an antibot protection so it only lets it load, the sample is in the image walmart_antibot.jpg in this directory.

After the other supermarket service is displayed it gets the products in json format.


## Pre requisites

One must have Python installed in his local system for deploying this RESTFUL-API easily. Other than Python one must also have to install Python-Flask and its dependencies as mentioned in the requirements.txt file.


## Running the API Service

Start the server with the following commands docker 
```
docker build -t deploy-api .
```
```
docker run -p 8081:8081 deploy-api
```
Optional command, use if you can't find the binaries for the webdriver.
```
docker pull selenium/standalone-chrome
```

## Checking the API

In the following link you have the call in post and get so that both services can be tested with a preloaded example.

http://127.0.0.1:8081/swagger 

or

http://0.0.0.0:8081/swagger/
