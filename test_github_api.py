import unittest
from unittest.mock import patch
from github_api import get_repos, get_commit_count

class TestGitHubAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_repos_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        repos = get_repos('testuser')
        self.assertEqual(repos, ['repo1', 'repo2'])

    @patch('requests.get')
    def test_get_commit_count_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{}] * 5
        commit_count = get_commit_count('testuser', 'repo1')
        self.assertEqual(commit_count, 5)

if __name__ == '__main__':
    unittest.main()
