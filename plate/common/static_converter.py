# -*- coding:utf-8 -*-


from os.path import join
from os.path import split

from bs4 import BeautifulSoup
from jinja2 import Environment
from jinja2 import PackageLoader

from plate.common import is_absolute


def local_url_for(endpoint, **values):
    dir_path, file_path = split(values['filename'])
    dir_path = dir_path[0].replace("/", "./") + dir_path[1:]
    return join(dir_path, file_path)


def convert_static_html(config, contents):
    """
    Render plate template to HTML

    In case of ``python plate.py -m convert`` use this method.

    :param config: config instance
    :param contents: converted html from markdown
    :return: rendered html
    """
    try:
        env = Environment(loader=PackageLoader('plate', 'templates'),
                          autoescape=False,
                          extensions=['jinja2.ext.autoescape'])

        t = env.get_template('index.html')
        config.SUPPORT_LANG = [str(lang) for lang in config.SUPPORT_LANG]

        logo_img = config.LOGO_IMG if config.exist('LOGO_IMG') else None
        logo_title = config.LOGO_TITLE if config.exist('LOGO_TITLE') else None

        rendered_template = t.render(API_TITLE=config.TITLE,
                                     IS_SEARCH=config.SEARCH_ON,
                                     LOGO_TITLE=logo_title,
                                     LOGO_IMG=logo_img,
                                     IS_LOGO_ABSOLUTE_URL=is_absolute(logo_img),
                                     SUPPORT_LANGUAGES=config.SUPPORT_LANG,
                                     DOCS=contents,
                                     COPYRIGHT=config.COPYRIGHT,
                                     FAVICON=config.FAVICON,
                                     url_for=local_url_for)

        soup = BeautifulSoup(rendered_template)
        return soup.prettify()

    except Exception as e:
        raise e
