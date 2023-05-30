# Software 

Table of Contents
=================

* [A Brief Introduction](#a-brief-introduction)
* [Pre requisites](#pre-requisites)
* [Running the API Service](#running-the-api-service)
* [Checking the API](#checking-the-api)



## A Brief Introduction

En este repositorio se usará para ejemplificar el uso de conceptos, bibliotecas y habilidades en software. 

Cada endpoint hace uso de una url para ser usado, sirviendo como microservicio.
El primero /supermecado, funciona como un ejemplo de un bot que obtiene los datos se forma automatica usando la libreria de Selenium y regresa en formato json la respuesta que se obtiene

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
