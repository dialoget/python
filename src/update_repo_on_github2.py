import sys
sys.path.append('../')
from lib.dialoget import dialoget

@dialoget('Update a {repo_name} on {org_name}, Set a {description}, Set a {domain}', '../../')
# Connect to the github API @GITHUB_API_URL with @api_token'
# Update a @repo_name on @org_name
# with a @description
# on the @domain
def update_repo_on_github2(api_token, org_name, repo_name, description, domain, GITHUB_API_URL='https://api.github.com'):
    """
    Update the description of a specific GitHub repository.

    This function uses the GitHub API to update the repository's description field.
    It requires an API token with appropriate permissions to modify repository settings.

    Parameters:
    - api_token (str): The personal access token for GitHub API authentication.
    - org_name (str): The name of the organization under which the repository exists.
                      Use the username for repositories owned by an individual user.
    - repo_name (str): The name of the repository to be updated.
    - description (str): The new description text for the repository.
    - domain (str): The custom domain to use for API requests. This is useful if you
                    are using GitHub Enterprise with a different domain than github.com.
    - GITHUB_API_URL (str, optional): The base URL for the GitHub API. Defaults to
                                      'https://api.github.com', which is the public API URL.

    Returns:
    None - This function does not return a value but raises an exception if the update fails.

    Raises:
    - HTTPError: An error from the requests module 'requests.exceptions.HTTPError' if the
                 HTTP request returned an unsuccessful status code.
    - Exception: A general exception if the update was unsuccessful, with an error message
                 indicating the failure reason.

    Usage:
    ```python
    update_repo_on_github2('<your_api_token>', 'my-org', 'my-repo', 'New description', 'https://github.my-domain.com')
    ```
    """

    # Code to perform the API request to update the repository description would go here.
    # The 'requests' library would typically be used to make the HTTP request.
    # Example:
    #   headers = {'Authorization': f'token {api_token}'}
    #   data = {'description': description}
    #   response = requests.patch(f'{GITHUB_API_URL}/repos/{org_name}/{repo_name}',
    #                             json=data, headers=headers)
    #   response.raise_for_status()  # Raise an HTTPError if the request returned an
    #                                # unsuccessful status code.

    # Endpoint to create a repo within an organization
    url = f'{GITHUB_API_URL}/repos/{org_name}/{repo_name}/pages'

    try:
        url = f'{GITHUB_API_URL}/repos/{org_name}/{repo_name}/pages'
        # print(url)
    except:
        print("Something went wrong")
        exit(1)
    # print(api_token, org_name, repo_name, description, domain)
    return 200

# result = update_repo_on_github(api_token, org_name, repo_name, description, domain)
# (result.status == 200)


# f'Connect to {Github,github_url,GITHUB_API_URL} by {"API token",api_token,GITHUB_API_TOKEN}'
