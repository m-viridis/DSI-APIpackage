import requests
import json

from google.colab import userdata

token = userdata.get('utordsi')
headers = {'Authorization': 'Bearer ' + token}

def Github_commits_err(url=str) -> None:
  try:
    req = requests.get(url, headers=headers)
    req.raise_for_status()
    print(req.status_code)
    r_json = json.loads(req.text)
    print(r_json)
  except requests.exceptions.HTTPError:
    raise requests.exceptions.HTTPError('url argument needs to match the following format: "https://api.github.com/repos/USER_NAME/REPO_NAME/stats/code_frequency" wherein USER_NAME and REPO_NAME are edited to match a repo url')