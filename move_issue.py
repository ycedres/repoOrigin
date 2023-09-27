import os
from github import Github

# Use GitHub token from environment variable
g = Github(os.environ['GITHUB_TOKEN'])

repo_A = g.get_repo("owner/repoSource")  # Replace 'owner' with the appropriate owner/organization name
repo_B = g.get_repo("owner/repoTarget")  # Replace 'owner' with the appropriate owner/organization name

issue_number = int(os.environ['ISSUE_NUMBER'])
issue = repo_A.get_issue(issue_number)

if "easy" in [label.name for label in issue.get_labels()]:
    # Create a new issue in repo B with the same content
    new_issue = repo_B.create_issue(
        title=issue.title,
        body=f"Originally reported by: {issue.user.login}\n\n{issue.body}",
        labels=[label.name for label in issue.get_labels() if label.name != "easy"]  # Copy labels excluding "easy"
    )
    
    # Close the original issue in repo A with a comment
    issue.create_comment(f"This issue has been moved to {new_issue.html_url}.")
    issue.edit(state="closed")

