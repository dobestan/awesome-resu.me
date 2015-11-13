import requests


def get_repository_url(username):
    """Return full github url with <username>/awesome-<username>."""

    repository_url = "https://github.com/{username}/awesome-{username}".format(
        username=username,
    )
    return repository_url


def is_repository_valid(repository_url):
    """Check given github repository url is valid or not."""

    response = requests.get(repository_url)

    if response.status_code == 200:
        return True
    return False
