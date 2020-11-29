import requests
import json
import os

org_name = input("Enter organization name:")
output_file_path = input("Enter output file path:")

# To get all the repositories of a particular organization
response = requests.request("GET", url=f"https://api.github.com/orgs/{org_name}/repos")

# Converting json data into dict format
repos_list = json.loads(response.text)

for i in range(0, len(repos_list)):
    # Get relative path of repository, eg: amfoss/cms
    repo_name = repos_list[i]["full_name"]
    # Run perceval command to fetch commits and append them to output file
    os.system(f"perceval git --json-line https://github.com/{repo_name} >> {output_file_path}")