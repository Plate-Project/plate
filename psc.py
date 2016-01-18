# -*- coding:utf-8 -*-

# Plate Static Converter

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass

from plate.common import logger


def convert_mode(config_file):
    from os.path import join
    from os.path import isdir
    import os
    import shutil

    if not config_file:
        sys.exit()

    try:
        from plate.common.config import Config
        config = Config.load_conf('./config.json')

        # create documents
        from plate.api_document import APIDocument
        api_doc = APIDocument(config)

        from plate.common import convert_static_html
        rendered_template = convert_static_html(config=config, contents=api_doc.contents)

        path = "./static"
        dirs = os.listdir(path)

        if not isdir(config.STATIC.DIR):
            os.mkdir(config.STATIC.DIR)

        for d in dirs:
            src_dir = join(path, d)
            dst_dir = join(config.STATIC.DIR, d)
            if isdir(dst_dir):
                shutil.rmtree(dst_dir)
            shutil.copytree(src_dir, dst_dir)

        with open(join(config.STATIC.DIR, config.STATIC.HTML), 'w') as f:
            f.write(rendered_template)

    except Exception as e:
        logger.exception(e)
        if isdir(config.STATIC.DIR):
            shutil.rmtree(config.STATIC.DIR)
        import traceback
        logger.error(traceback.format_exc())
