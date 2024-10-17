import requests

def get_repos(user_id):
    try:
        response = requests.get(f'https://api.github.com/users/{user_id}/repos')
        response.raise_for_status()
        repos = response.json()
        return [(repo['name']) for repo in repos]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def get_commit_count(user_id, repo_name):
    try:
        response = requests.get(f'https://api.github.com/repos/{user_id}/{repo_name}/commits')
        response.raise_for_status()
        commits = response.json()
        return len(commits)
    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 409:
            # Handle the 409 Conflict error (likely due to an empty repository or API issue)
            print(f"Conflict error: No commits found for repo '{repo_name}'")
            return 0
        else:
            print(f"HTTP error occurred: {http_err}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

def get_repos_and_commits(user_id):
    repos = get_repos(user_id)
    repo_commits = []
    for repo in repos:
        commit_count = get_commit_count(user_id, repo)
        repo_commits.append(f"Repo: {repo}, Number of commits: {commit_count}")
    return repo_commits

if __name__ == '__main__':
    user_id = 'naccardo3' 
    print(get_repos_and_commits(user_id))
     
