import os

# Signing in and setting the subscription
SubscriptionId = '07c29cd9-f0b0-42f7-be1c-01d2cfc5ee2c'
Location = 'northeurope'
os.system('az login')
os.system(f'az account set --subscription {SubscriptionId}')

# Creating the test environment
ResourceGroup = 'TestingRG'
TemplateName = 'TestTemplate'
os.system(f'az group create --name {ResourceGroup} --location {Location}')
 
# Deploying the test VM
TemplateFile = 'TestEnvTemplates/DeployTestVM.json'
ParameterFile = '@TestEnvTemplates/TestVMParameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')


# Deploying the test database
TemplateFile = 'TestEnvTemplates/DeployTestDB.json'
ParameterFile = '@TestEnvTemplates/TestDBParameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# Creating the production environment
ResourceGroup = 'ProductionRG'
TemplateName = 'ProductionTemplate'
os.system(f'az group create --name {ResourceGroup} --location {Location}')

# Deploying two production VMs
TemplateFile = 'ProdEnvTemplates/DeployProdVM.json'
ParameterFile = '@ProdEnvTemplates/ProdVM1Parameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')
ParameterFile = '@ProdEnvTemplates/ProdVM2Parameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')


# Deploying the production database
TemplateFile = 'ProdEnvTemplates/DeployProdDB.json'
ParameterFile = '@ProdEnvTemplates/ProdDBParameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')