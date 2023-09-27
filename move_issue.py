import sys
from github import Github, Auth

token, issue_number = sys.argv[1], int(sys.argv[2])
g = Github(token)

repo_A = g.get_repo("ycedres/repoOrigin") 
repo_B = g.get_repo("ycedres/repoTarget")

issue = repo_A.get_issue(issue_number)

if "good first issue" in [label.name for label in issue.get_labels()]:
    new_issue = repo_B.create_issue(
        title=issue.title,
        body=f"Originally reported by: {issue.user.login}\n\n{issue.body}",
        labels=[label.name for label in issue.get_labels() if label.name != "good first issue"] 
    )
    
    issue.create_comment(f"This issue has been moved to {new_issue.html_url}.")
    issue.edit(state="closed")

