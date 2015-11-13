from django.test import TestCase

from multisites.utils.github import *


class GithubUtilsTestCase(TestCase):

    def setUp(self):
        self.username = 'dobestan'

        self.valid_github_repository_url = "https://github.com/dobestan/awesome-dobestan"
        self.invalid_github_repository_url = "https://github.com/dobestan/not-awesome-dobestan"

    def test_get_repository_url(self):
        self.assertEqual(
            get_repository_url(self.username),
            self.valid_github_repository_url,
        )

    def test_is_repository_valid(self):
        self.assertTrue(
            is_repository_valid(self.valid_github_repository_url),
        )
        self.assertFalse(
            is_repository_valid(self.invalid_github_repository_url),
        )
