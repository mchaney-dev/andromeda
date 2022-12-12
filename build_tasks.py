import os
from git import Repo

# get current file location
cwd = os.path.abspath(os.path.dirname(__file__))
url = 'https://github.com/mchaney-dev/andromeda/tree/development-base'
# copy necessary files and directories to cwd
# requires git to be installed and in PATH
Repo.clone_from(url=url, to_path=cwd)
os.system('pip install -r requirements.txt')