import sys
sys.path.append('../../')
from data.env import GITHUB_API_URL
from src.update_repo_on_github2 import update_repo_on_github2
from data.prompt import *
#from data.map import *

#print(FromEnv)
#api_token="API token"
#repo_name="Repository"
#org_name="GitHub Organization"
f'Connect to the github API {GITHUB_API_URL} with {api_token}'
f'Update a {repo_name} on {org_name}'
f'with a {description}'
f'on the {domain}'
result = update_repo_on_github2(api_token, org_name, repo_name, description, domain, GITHUB_API_URL)
#print(result)
print(result == 200)


# f'Connect to {Github,github_url,GITHUB_API_URL} by {"API token",api_token,GITHUB_API_TOKEN}'
