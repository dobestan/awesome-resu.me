import requests


class GithubRepository(object):

    def __init__(self, username, *args, **kwargs):
        self.username = username
        self.repository_url = self.get_repository_url()

    def get_repository_url(self):
        """Return full github url with <username>/awesome-<username>."""

        repository_url = "https://github.com/{username}/awesome-{username}".format(
            username=self.username,
        )
        return repository_url

    def is_repository_valid(self):
        """Check given github repository url is valid or not."""

        response = requests.get(self.repository_url)

        if response.status_code == 200:
            return True
        return False
