# A Cloud Guru Challenge: Your resume in Azure

Hi there!

This repository is hosting the code and documentation of the A Cloud Guru Challenge: Your resume in Azure.

The idea is to build a resume and host it using Azure services.

## The steps

* [X] Create a GitHub repository
* [X] Create the website (HTML, CSS...)
* [ ] Add a visitor counter on the website
  * [X] Create CosmoDB database
  * [ ] Create Azure function to get number of views
* [X] Deploy the website to Azure Static App
* [ ] Enable HTTPS and custom domain support
* [X] Set up GitHub actions
* [ ] Write a blog post to describe the process

## My journey

I already worked on the Cloud Resume challenge before. The goal was to host my resume on AWS.

I have a decent knowledge of AWS and passed the AZ-900 but I'm not working on a daily basis with Azure. This challenge is a way to get some experience with it.

### Azure function

* Create an Azure account
* Install VSCode extension and Core tools (v3) (run `func`in terminal to check the installation)
* Configure a new HTTPTrigger (with Python for me)
* Create CosmosDB account from portal (serverless mode)
* Create a Cosmos container
* Create a document with a counter property
  