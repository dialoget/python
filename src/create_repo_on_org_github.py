import sys
sys.path.append('../')
from data.env import GITHUB_API_URL
from lib.dialoget import dialoget

#f'Connect to {GITHUB_API_URL} by {api_token}'
#@dialoget('Connect {GITHUB_API_URL} on {api_token}, Set a {description}, Set a {domain}')
#@dialoget('Update {GITHUB_API_URL} on {api_token}, Set a {description}, Set a {domain}')
@dialoget('Update a {repo_name} on {org_name}, Set a {api_token}, Set a {GITHUB_API_URL}','../../')
def create_repo_on_org_github(repo_name, org_name, api_token, GITHUB_API_URL):
    # Endpoint to create a repo within an organization
    url = f'{GITHUB_API_URL}/repos/{org_name}/{repo_name}/pages'

    try:
        url = f'{GITHUB_API_URL}/repos/{org_name}/{repo_name}/pages'
        #print(url)
    except:
        print("Something went wrong")
        exit(1)
    #print(api_token, org_name, repo_name, description, domain)
    return 200

# result = update_repo_on_github(api_token, org_name, repo_name, description, domain)
# (result.status == 200)



#def create_repo_on_org_github(api_token, repo_name, org_name, description, domain, GITHUB_API_URL='https://api.github.com'):