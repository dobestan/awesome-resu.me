require 'github/markup'

filename = ARGV[0]
content = ARGV[1]

result = GitHub::Markup.render(
  filename,
  content
)

$stdout.write result
