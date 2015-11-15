from django.test import TestCase

from multisites.utils.github import GithubRepository


class GithubUtilsTestCase(TestCase):

    def setUp(self):
        self.username = 'dobestan'
        self.github_repository = GithubRepository(self.username)

        self.valid_github_repository_url = "https://github.com/dobestan/awesome-dobestan"

        self.invalid_username = 'invalid_dobestan'
        self.invalid_github_repository = GithubRepository(self.invalid_username)

    def test_get_repository_url(self):
        self.assertEqual(
            self.github_repository.get_repository_url(),
            self.valid_github_repository_url,
        )

    def test_is_repository_valid(self):
        self.assertTrue(
            self.github_repository.is_repository_valid(),
        )
        self.assertFalse(
            self.invalid_github_repository.is_repository_valid(),
        )
