from django.views.generic import TemplateView
from django.http import HttpResponse, Http404

from multisites.utils.github import GithubRepository


class HomeView(TemplateView):
    template_name = 'resume.html'

    def dispatch(self, *args, **kwargs):

        self.http_host = self.request.META.get('HTTP_HOST')
        self.subdomain = self.http_host.split('.')[0]

        self.github_repository = GithubRepository(self.subdomain)

        # TODO: Speed-up this rendering process via caching.
        # README.md does not needed to be update on every request.
        self.rendered_readme_content = self.github_repository.get_rendered_readme_content()

        # TODO: Should redirect to main site if repository does not exist.
        if not self.github_repository.is_repository_valid():
            raise Http404("Github Repository does not exist")

        return super(HomeView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['resume'] = self.rendered_readme_content

        return context
