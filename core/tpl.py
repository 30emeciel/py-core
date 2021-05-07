from babel.dates import format_date
from jinja2 import Environment, select_autoescape, PackageLoader, ChoiceLoader, FileSystemLoader

SLACK_DATE_FORMAT = "date"


def slack_date_format(dt):
    return f"<!date^{int(dt.timestamp())}^{{{SLACK_DATE_FORMAT}}}|{date_format(dt)}>"


def date_format(d, fmt="medium"):
    return format_date(d, locale='fr', format=fmt)


def pluralize(number, singular='', plural='s'):
    if number == 1:
        return singular
    else:
        return plural


env = Environment(
    extensions=['jinja2.ext.i18n'],
    loader=ChoiceLoader([
        FileSystemLoader("templates"),
        PackageLoader("core", "templates"),
        ]),
    autoescape=select_autoescape(
        enabled_extensions=('html', 'htm', 'xml'),
        default_for_string=False,
        default=False,
    )
)
env.filters["dateformat"] = date_format
env.filters["slackdateformat"] = slack_date_format
env.filters["pluralize"] = pluralize


def render(template, data):
    tpl = env.get_template(template)
    return tpl.render(data)
