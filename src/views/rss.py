
from sanic import Sanic
import sys
from sanic.response import json, text, html
from feedparser import parse
from jinja2 import Environment, PackageLoader, select_autoescape
enable_async = sys.version_info >= (3, 6)

app = Sanic()

# jinjia2 config
env = Environment(
    loader=PackageLoader('views.rss', '../templates'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']),
    enable_async=enable_async)


async def template(tpl, **kwargs):
    template = env.get_template(tpl)
    rendered_template = await template.render_async(**kwargs)
    return html(rendered_template)


@app.route("/html")
async def rss_html(request):
    url = "http://blog.howie6879.cn/atom.xml"
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append(
            {"title": article["title_detail"]["value"], "link": article["link"], "published": article["published"]})
    return await template('rss.html', articles=articles)