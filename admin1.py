from github import Github
from github import get_github3_client
# Creating this to mass update all of our repos settings.
g = Github("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") # Your personal token
static_gh = None
def gh():
    global static_gh
    if not static_gh:
        static_gh = get_github3_client()
    return static_gh
def fetch_admins(owner, repo):
    """get all repository admins."""
    admins = set()
    repo = gh().repository(owner, repo)
    for collaborator in repo.collaborators():
        if collaborator.permissions["admin"]:
            admins.add(collaborator.login)
    return admins
