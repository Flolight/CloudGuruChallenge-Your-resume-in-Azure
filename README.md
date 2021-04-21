# A Cloud Guru Challenge: Your resume in Azure

Hi there!

This repository is hosting the code and documentation of the A Cloud Guru Challenge: Your resume in Azure.

The idea is to build a resume and host it using Azure services.

## The steps

* [X] Create a GitHub repository
* [X] Create the website (HTML, CSS...)
* [X] Add a visitor counter on the website
  * [X] Create CosmoDB database
  * [X] Create Azure function to get number of views
* [X] Deploy the website to Azure Static Web App
* [X] Enable HTTPS and custom domain support
* [X] Set up GitHub actions
* [ ] Add tests to the counter function

Additional steps:

* [ ] Migrate out of Azure static web apps
  * [x] Azure Blob storage
  * [x] HTTPS
  * [x] Custom domain
  * [x] Function
  * [ ] CI/CD Github Actions
    * [X] Static website
    * [X] Counter Function (Python)
Last step:

* [ ] Write a blog post to describe the process

## My journey

I already worked on the Cloud Resume challenge before. The goal was to host my resume on AWS.

I have a decent knowledge of AWS and passed the AZ-900 but I'm not working on a daily basis with Azure. This challenge is a way to get some experience with it.

### Static hosting

* Use Azure Static Apps
* Configure Custom domain
  * Add to your DNS entries a CNAME pointing to the Static App url
  * Verify it (Custom domains > Add+)

### Azure function

* Create an Azure account
* Install VSCode extension and Core tools (v3) (run `func`in terminal to check the installation)
* Configure a new HTTPTrigger (with Python for me)
* Create CosmosDB account from portal (serverless mode)
* Create a Cosmos container
* Create a document with a counter property

* Add CORS for the static website to be able to call the Azure function
  
> don't forget to check the Enable Access-Control-Allow-Credentials option

### Host static website

[Tutorial](https://docs.microsoft.com/fr-fr/azure/storage/blobs/storage-blob-static-website)

* create a storage account and run the following:
* 
az storage blob service-properties update --account-name floresume2021 --static-website --404-document error.html --index-document index.html

az storage blob upload-batch -s /Users/flo/repos/CloudGuruChallenge-Your-resume-in-Azure/front -d '$web' --account-name floresume2021

### Azure CDN

[Tutorial](https://docs.microsoft.com/fr-fr/azure/storage/blobs/static-website-content-delivery-network)

### Map a custom domain

[Tutorial](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-custom-domain-name?tabs=azure-portal#enable-https)

Use cdnverify to avoid downtime when migrating

Custom domain https with CDN managed certificates

### Github action

* Generate deployment credentials and copy the json for later use

```sh
az ad sp create-for-rbac --name {myStaticSite} --role contributor --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group} --sdk-auth
```
az ad sp create-for-rbac --name floresume --role contributor --scopes /subscriptions/b2348720-5caf-4463-899f-1891ed1130c4/resourceGroups/flo-resume --sdk-auth

* Add a secret to Github repository with the json

* Create a new workflow under .github/workflows/

(link to be added to the workflow file...)

> Note that if you are using Azure Static Web Apps, the workflow file is already generated.

### Scripting

[Tutorial](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-create-first-template?tabs=azure-cli)

[ARM template reference](https://docs.microsoft.com/en-us/azure/templates/)

* [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

* Use az login to set up credentials

* Create a template.json and set up the blank template

* Create resource group for the template

```sh
az group create \
--name resumeGroup \
--location "East US 2"
```

```sh
templateFile="{path to your template file}"
az deployment group create \
  --name blanktemplate \
  --resource-group resumeGroup \
  --template-file $templateFile
```

* Add storage resource

templateFile="/Users/flo/repos/CloudGuruChallenge-Your-resume-in-Azure/templates/azurestoragedeploy.json"
az deployment group create \
  --name addstorage \
  --resource-group flo-resume \
  --template-file $templateFile \
  --parameters storageName=resumeflo2021

templateFile="/Users/flo/repos/CloudGuruChallenge-Your-resume-in-Azure/templates/azurefunctiondeploy.json"
az deployment group create \
  --name addfunction \
  --resource-group flo-resume \
  --template-file $templateFile \
  --parameters storageName=resumeflo2021