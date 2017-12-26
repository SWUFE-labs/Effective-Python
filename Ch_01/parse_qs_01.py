"""One line logic solution to evaluating missing values in a query string
using an 'or' expression."""

from urllib.parse import parse_qs

# For query string 'red=5&blue=0&green='
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)

red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)
