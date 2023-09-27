import os
from github import Github

g = Github(os.environ['GITHUB_TOKEN'])

repo_A = g.get_repo("ycedres/repoOrigin") 
repo_B = g.get_repo("ycedres/repoTarget")

issue_number = int(os.environ['ISSUE_NUMBER'])
issue = repo_A.get_issue(issue_number)

if "easy" in [label.name for label in issue.get_labels()]:
    new_issue = repo_B.create_issue(
        title=issue.title,
        body=f"Originally reported by: {issue.user.login}\n\n{issue.body}",
        labels=[label.name for label in issue.get_labels() if label.name != "good first issue"] 
    )
    
    issue.create_comment(f"This issue has been moved to {new_issue.html_url}.")
    issue.edit(state="closed")

