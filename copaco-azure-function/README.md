# Test Azure Functions

## Set-up to work locally 
Install the project requirements:
```shell
npm install
```
```shell
pip install -r requirements.txt
```
```shell
sls offline build
```

To run a local version of the Azure Function to test with, use:
```shell
sls offline
```
After it, you can check if it works properly with next two endpoints:

To deploy the function to your Azure account use:

Here is a link to a [Local "One Random Quote"](http://localhost:7071/api/randquote)

Here is a link to a [Local "Filtered Quotes"](http://localhost:7071/api/quotes/les)
## Deploy the functions
To deploy your version of the Azure Function use:

```shell
sls deploy
```
To check already deployed test functions follow the links:

Here is a link to [One Random Quote](https://sls-weur-dev-copaco-azure-function.azurewebsites.net/api/randquote?code=aeKDfekEHHloNVGWLX9E63lNOCCltPQtzGWdrEqDLyq7AzFuzGwFOQ==).

Here is a link to [Filtered Quotes](https://sls-weur-dev-copaco-azure-function.azurewebsites.net/api/quotes/les?code=J0dMDIZjDq04gNhXzvb8AeXOVoO-0PAYLHeCuv5XwB8jAzFuNooU9Q==)


