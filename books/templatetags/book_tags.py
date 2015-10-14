from django import template
import datetime


class CurrentTimeNode2(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        context['current_time2'] = now.strftime(self.format_string)
        return ''


class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)

register = template.Library()


@register.tag(name="current_time")
def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        # token: 'current_time "%Y-%m-%d %I:%M %p"'
        tag_name, format_sting = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)

    return CurrentTimeNode(format_sting[1:-1])


@register.tag(name="current_time2")
def do_current_time2(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        # token: 'current_time "%Y-%m-%d %I:%M %p"'
        tag_name, format_sting = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)

    return CurrentTimeNode2(format_sting[1:-1])