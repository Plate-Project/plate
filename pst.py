# -*- coding:utf-8 -*-

# pst : Python Static Tool

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass

from plate.common import pst_logger as logger


def convert_mode(config_file_path):
    from os.path import join
    from os.path import isdir
    import os
    import shutil

    if not config_file_path:
        sys.exit()

    from plate.common.config import Config
    config = Config.load_conf(config_file_path)

    try:

        # create documents
        logger.info("Creating APIDocument")
        from plate.api_document import APIDocument
        api_doc = APIDocument(config)
        logger.info("  API Document index " + api_doc.index_file_path)
        logger.info("  API Document Files " + ", ".join(api_doc.toc['ORDER']))

        from plate.common import convert_static_html
        rendered_template = convert_static_html(config=config, contents=api_doc.contents)
        logger.info("Converting APIDocument to HTML")

        path = "./plate/static"
        dirs = os.listdir(path)

        if not isdir(config.STATIC.DIR):
            os.mkdir(config.STATIC.DIR)

        logger.info("Creating dir " + str(config.STATIC.DIR))

        for d in dirs:
            src_dir = join(path, d)
            dst_dir = join(config.STATIC.DIR, d)

            if isdir(dst_dir):
                shutil.rmtree(dst_dir)
            shutil.copytree(src_dir, dst_dir)
            logger.info("  Copying dir " + src_dir + " to " + dst_dir)

        html_file_path = join(config.STATIC.DIR, config.STATIC.HTML)
        logger.info("Writing file " + html_file_path)
        with open(html_file_path, 'w') as f:
            f.write(rendered_template)

    except Exception as e:
        logger.exception(e)
        if isdir(config.STATIC.DIR):
            shutil.rmtree(config.STATIC.DIR)
            shutil.rmtree(config.STATIC.DIR)
            shutil.rmtree(config.STATIC.DIR)
            shutil.rmtree(config.STATIC.DIR)
        import traceback
        logger.error(traceback.format_exc())


def parse_argument():
    import optparse
    p = optparse.OptionParser('-f [config file path]')
    try:
        p.add_option('-f', dest='config_file_path', type='string', default='./config.json')
        options, args = p.parse_args()
        return options.config_file_path
    except:
        print(p.get_usage())
        sys.exit()


if __name__ == '__main__':
    logger.info("Welcome to the Plate Static Tool 0.2.5.")
    convert_mode(config_file_path=parse_argument())
    logger.info("Finished.")
