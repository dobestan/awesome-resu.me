import requests


class GithubRepository(object):
    """Github Repository related functions."""

    # TODO: refactor this class with Github Developer API.
    # https://developer.github.com/v3/

    def __init__(self, username, *args, **kwargs):
        self.username = username

        self.repository_url = self.get_repository_url()
        self.raw_readme_url = self.get_raw_readme_url()

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

    def get_raw_readme_url(self, branch='master'):
        """Return raw README.md url."""

        raw_readme_url = "https://raw.githubusercontent.com/{username}/awesome-{username}/master/README.md".format(
            username=self.username,
        )
        return raw_readme_url

    def get_readme_content(self):
        """Return README.md contents from repository."""

        response = requests.get(self.raw_readme_url)

        # default type of response.content is "bytes".
        # return type should be a "str" with UTF8 encoding.
        return response.content.decode('utf8')
