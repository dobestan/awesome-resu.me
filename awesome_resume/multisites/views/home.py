from django.views.generic import View
from django.http import HttpResponse, Http404

from multisites.utils.github import GithubRepository
from markup.utils.renderer import MarkupRenderer


class HomeView(View):

    def dispatch(self, *args, **kwargs):

        self.http_host = self.request.META.get('HTTP_HOST')
        self.subdomain = self.http_host.split('.')[0]

        self.github_repository = GithubRepository(self.subdomain)

        return super(HomeView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):

        # TODO: Should redirect to main site if repository does not exist.
        if not self.github_repository.is_repository_valid():
            raise Http404("Github Repository does not exist")

        return HttpResponse(
            self.github_repository.get_rendered_readme_content(),
        )
