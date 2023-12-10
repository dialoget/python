import sys
sys.path.append('../../')
from src.update_repo_on_github import update_repo_on_github
from data.map import *
#from lib.dialoget import *



#print(FromEnv)
#api_token="API token"
#repo_name="Repository"
#org_name="GitHub Organization"
f'Update a {repo_name} on {org_name}'
f'Set a {description}'
f'Set a {domain}'
result = update_repo_on_github(api_token, org_name, repo_name, description, domain)
#print(result)
print(result == 200)


# f'Connect to {Github,github_url,GITHUB_API_URL} by {"API token",api_token,GITHUB_API_TOKEN}'
