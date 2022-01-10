import os
import requests
import json
 
# Username of User Authenticating
username = os.environ['username']
token = os.environ['token']
 
def fetch_repos(source,name):
    print(source)
    print(name)
    if source == "organization":
        repos = requests.get(' https://api.github.com/orgs/'+name+'/repos', auth=(username,token))
 
    if source == "user": 
        repos = requests.get(' https://api.github.com/users/'+name+'/repos', auth=(username,token))
    print(repos)
    repos = json.loads(repos.text)
 
    print("List of" + name + "'s repositories:")
    for repo in repos:  
        print(repo["name"])
 
    return repos
 
def fetch_issues(target_repo, repos):
 
    for repo in repos:
      if target_repo in repo["name"]:
         issues_url = repo["issues_url"]
         issues_url = issues_url.split("{/number}")
         issues_url = issues_url[0]
 
    issues = requests.get(issues_url, auth=(username,token))
 
    current_issues = []
    issues = json.loads(issues.text)
    for issue in issues:  
        current_issue = {}
        current_issue['title']=issue["title"]
        current_issue['labels']=[]
        for label in issue["labels"]:
            current_issue['labels'].append(label["name"])
        current_issues.append(current_issue)
 
    return {
        print(current_issues)
    }
 
source = input("Where do you plan to source your list of Repos from? [organization or user] : ")
name = input("What is the name of your organization or username you wish to query? : ")
repos = fetch_repos(source,name)
 
target_repo = input("Which Repo do you want to check the issues of? ")
 
fetch_issues(target_repo,repos)