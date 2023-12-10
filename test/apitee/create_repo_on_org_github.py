import sys
sys.path.append('../../')
from data.env import GITHUB_API_URL
from src.create_repo_on_org_github import create_repo_on_org_github
from data.prompt import *
#from lib.dialoget import *
#from data.map import *




# print(FromEnv)
# api_token="API token"
# repo_name="Repository"
# org_name="GitHub Organization"
#f'Connect to the github API {GITHUB_API_URL} with {api_token}'
#f'Create a {repo_name} on {org_name}'
result = create_repo_on_org_github(repo_name, org_name, api_token, GITHUB_API_URL)
# print(result)
print(result == 200)

# f'Connect to {Github,github_url,GITHUB_API_URL} by {"API token",api_token,GITHUB_API_TOKEN}'
