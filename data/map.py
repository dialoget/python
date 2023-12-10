import sys
sys.path.append('../')
from data.user import *
from data.prompt import *

FromEnv = {
    "API token": GITHUB_API_TOKEN,
    "GitHub Organization": GITHUB_ORGANIZATION_DEFAULT,
    "Repository": GITHUB_REPOSITORY_DEFAULT,
}
FromArgs = {
    "API token": api_token,
    "GitHub Organization": org_name,
    "Repository": repo_name,
}
