# -*- coding:utf-8 -*-
'''
Created on 2015. 10. 08
@author: AhnSeongHyun
'''


def local_url_for(endpoint, **values):
    from os.path import split
    from os.path import join
    dir, file = split(values['filename'])
    dirname = split(dir)[1]
    return join(join("./", dirname), file)


def convert_static_html(config, contents):
    try:

        from jinja2 import Environment
        from jinja2 import PackageLoader
        env = Environment(loader=PackageLoader('plate', 'templates'),
                          autoescape=False,
                          extensions=['jinja2.ext.autoescape'])

        t = env.get_template('index.html')
        config.SUPPORT_LANG = [str(lang) for lang in config.SUPPORT_LANG]

        if config.exist('LOGO_IMG'):
            logo_img = config.LOGO_IMG
        else:
            logo_img = None

        if config.exist('LOGO_TITLE'):
            logo_title = config.LOGO_TITLE
        else:
            logo_title = None

        rendered_template = t.render(API_TITLE=config.TITLE,
                                     IS_SEARCH=config.SEARCH_ON,
                                     LOGO_TITLE=logo_title,
                                     LOGO_IMG=logo_img,
                                     SUPPORT_LANGUAGES=config.SUPPORT_LANG,
                                     DOCS=contents,
                                     COPYRIGHT=config.COPYRIGHT,
                                     url_for=local_url_for)
        return rendered_template

    except Exception as e:
        raise e
