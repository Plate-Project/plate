
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import current_app
from flask import render_template

views_blueprint = Blueprint('views', __name__, url_prefix='/')


@views_blueprint.route('/')
def index():
    from ..watchdocs import DocumentTraceQueue
    from ..api_document import APIDocument
    document_trace_queue = DocumentTraceQueue()
    api_doc = APIDocument()
    if not document_trace_queue.is_empty():
        api_doc.total_reload_docs()
        document_trace_queue.clear()

    temp = [str(lang) for lang in current_app.config['SUPPORT_LANG']]
    current_app.config['SUPPORT_LANG'] = temp

    logo_img = current_app.config['LOGO_IMG'] if 'LOGO_IMG' in current_app.config else None
    logo_title = current_app.config['LOGO_TITLE'] if 'LOGO_TITLE' in current_app.config else None

    from datetime import datetime
    from ..common import is_absolute
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