import re
from django import template

register = template.Library()

@register.filter
def first_img(html_content):
    # print('html: ' + html_content)
    match = re.search(r'<img[^>]+src="([^">]+)"', html_content)
    if match:
        # print('image found')
        return match.group(1)
    return "/media/defaultImage.png"
