
# -*- coding: utf-8 -*-

from datetime import datetime

from flask import Blueprint
from flask import current_app
from flask import render_template

from plate.api_document import APIDocument
from plate.common.utils import is_absolute
from plate.watchdocs.document_trace_queue import DocumentTraceQueue

views_blueprint = Blueprint('views', __name__, url_prefix='/')


@views_blueprint.route('/')
def index():
    document_trace_queue = DocumentTraceQueue()
    api_doc = APIDocument()
    if not document_trace_queue.is_empty():
        api_doc.total_reload_docs()
        document_trace_queue.clear()

    current_app.config['SUPPORT_LANG'] = [str(lang) for lang in current_app.config['SUPPORT_LANG']]
    logo_img = current_app.config.get('LOGO_IMG', None)
    logo_title = current_app.config.get('LOGO_TITLE', None)

    return render_template("index.html",
                           API_TITLE=current_app.config['TITLE'],
                           IS_SEARCH=current_app.config['SEARCH_ON'],
                           LOGO_TITLE=logo_title,
                           LOGO_IMG=logo_img,
                           IS_LOGO_ABSOLUTE_URL=is_absolute(logo_img),
                           SUPPORT_LANGUAGES=current_app.config['SUPPORT_LANG'],
                           DOCS=api_doc.contents,
                           COPYRIGHT=current_app.config['COPYRIGHT'],
                           FAVICON=current_app.config['FAVICON'],
                           timestamp=datetime.now().strftime("%Y%m%d%H%M%S")
                           )
