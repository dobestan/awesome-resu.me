from django.test import TestCase

from markup.utils.renderer import MarkupRenderer


class MarkupRendererTestCase(TestCase):

    def test_render(self):
        self.assertTrue(
            MarkupRenderer.render(
                "# hello world #",
            ),
            "<h1>hello world</h1>\n",
        )

        self.assertTrue(
            MarkupRenderer.render(
                "* One\n* Two",
            ),
            "<ul>\n<li>One</li>\n<li>Two</li>\n</ul>\n",
        )
