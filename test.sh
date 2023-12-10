#!/bin/bash
cd test/apitee  || exit
python3 update_repo_on_github.py
python3 update_repo_on_github2.py
python3 create_repo_on_org_github.py