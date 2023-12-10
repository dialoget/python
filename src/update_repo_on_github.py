import sys
sys.path.append('../')
from data.env import GITHUB_API_URL
from lib.dialoget import dialoget

@dialoget('Update a {repo_name} on {org_name}, Set a {description}, Set a {domain}','../../')
def update_repo_on_github(api_token, org_name, repo_name, description, domain):
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


# f'Connect to {Github,github_url,GITHUB_API_URL} by {"API token",api_token,GITHUB_API_TOKEN}'
