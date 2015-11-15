import os
import subprocess


class MarkupRenderer(object):
    ruby_executable_path = os.path.dirname(__file__)
    ruby_executable_filename = 'renderer.rb'

    ruby_executable = os.path.join(
        ruby_executable_path,
        ruby_executable_filename,
    )

    def render(content, *args, **kwargs):
        filename = kwargs.get('filename', 'README.md')

        result = subprocess.check_output(
            [
                'ruby',
                MarkupRenderer.ruby_executable,
                filename,
                content,
            ],
        )

        return result.decode('utf8')
