import requests
import json
import os

org_name = input("Enter organization name:")
output_file_path = input("Enter output file path:")
page_no = 1
while True:
    # To get all the repositories of a particular organization
    response = requests.request("GET", url=f"https://api.github.com/orgs/{org_name}/repos", params={"page": page_no})

    # Converting json data into dict format
    repos_list = json.loads(response.text)
    if len(repos_list) == 0:
        break
    for i in range(0, len(repos_list)):
        # Get relative path of repository, eg: amfoss/cms
        repo_name = repos_list[i]["full_name"]
        # Run perceval command to fetch commits and append them to output file
        os.system(f"perceval git --json-line https://github.com/{repo_name} >> {output_file_path}")
    page_no += 1
