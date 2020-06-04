#!/usr/bin/python3
# Desenvolvido por Antonio Novaes
from github import *
import sys
TOKEN_USER= sys.argv[1]
REPOSITORIO = sys.argv[2]
BRANCH_REPO = sys.argv[3]
# or using an access token
g = Github(TOKEN_USER)
repo = g.get_repo(REPOSITORIO)
pulls = repo.get_pulls(state='open', sort='created', base=BRANCH_REPO)
for pr in pulls:
    print("Repositório: " + str(REPOSITORIO) + " -> " + str(pr.title) + " - numero do pull request: " + str(pr.number))
