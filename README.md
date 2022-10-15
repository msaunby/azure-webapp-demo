# azure-webapp-demo

Simple examples of web application hosting on Azure

## Overview

This repository contains a simple Python web application using the Plotly Dash library. Dash makes it easy to create Flask web applications with data from Pandas or Numpy.

Testing web applications on your development system is straightforward, but deploying to a hosting service can seem daunting, so this project provides some simple recipes for free/cheap deployment on Azure.  I picked Azure as students can get free credit each year, but there are many other hosting providers. Students can apply for Azure credit here <https://azure.microsoft.com/en-us/free/students/>

## Building the application

Any non-trivial Python application will have dependencies, typically imported modules, and it is important to ensure that the deployed version of your program uses the same versions of these as were used when testing. It's also important to ensure the same Python version is used.  This can be achieved using Pip requirement files and other tools to create a re-distributable project.

<https://packaging.python.org/en/latest/tutorials/packaging-projects/>

## Containers

Containers are useful tool for distributing software applications.  Rather than distribute the program code and configuration files we distribute an executable *image*.

<https://www.docker.com/resources/what-container/>

### Building a container image

The composition of our container is described in a ```Dockerfile```.  This file tells the Docker *build* program what the base image will be, typically a version of Linux with a minimal set of tools for the programming language used for the application to be run, and also describes how to install your program with all necessary libraries.

### Running a container

Containers can be run anywhere there is a suitable hosting environment. On your development machine this is most likely the Docker Engine program, but on Azure this will be the Azure App Service or the Azure Kubernetes Services.

## Development environment

### GitHub

GitHub provides cloud services for building and deploying software in addition to version control.  This demo makes use of GitHub Actions to automate the building and deployment of a Docker container.

<https://docs.github.com/repositories/releasing-projects-on-github/managing-releases-in-a-repository?tool=webui>


### Visual Studio Code

### Azure Cloud Shell
