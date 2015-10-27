# -*- coding:utf-8 -*-
'''
Created on 2015. 08. 31
@author: AhnSeongHyun
'''

import logging
logger = logging.getLogger('logger')

from common import syntax_highlight


class APIDocument(object):

    def __init__(self, config):
        from os.path import join

        self.config = config 
        self.index_file_path = join(self.config.API_DOC_PATH, self.config.API_DOC_INDEX_PATH)
        self.toc = self.read_index(self.index_file_path)
        self.contents = self.create_api_docs()

    def total_reload_docs(self):
        logger.info("total_reload_docs")
        self.toc = self.read_index(self.index_file_path)
        self.contents = self.create_api_docs()

    def read_index(self, index_file_path):
        import json
        from collections import OrderedDict
        return json.load(open(index_file_path), object_pairs_hook=OrderedDict)

    def create_api_docs(self):
        from os.path import join
        from os.path import split
        from collections import OrderedDict

        docs = OrderedDict()
        for doc_file in self.toc["ORDER"]:

            doc_file = join(self.config.API_DOC_PATH, doc_file)
            from common import conv_md2html
            with open(doc_file, 'r') as f:
                html = conv_md2html(f.read())
                docs[split(doc_file)[1]] = self.modify_html(self.highlight_syntax(self.reordering(html)))

        return docs.values()

    def reordering(self, html):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html)

        up_tags = []
        for up_tag in soup.h1.next_siblings:

            if 'name' in up_tag and up_tag.name in ['pre', 'blockquote']:
                up_tags.append(up_tag)

        up_tags = reversed(up_tags)

        for up_tag in up_tags:
            for prev in up_tag.previous_siblings:
                if prev.name == 'h2':
                    prev.insert_after(up_tag)
                    break
        return soup

    def highlight_syntax(self, soup):
        code_tags = soup.find_all('code')

        for code in code_tags: 
            if code.has_attr('class'):
                lang = code['class']
                code.parent['class'] = "highlight " + lang[0]
                del code['class']
                code.name = "span"

                in_pre_code = syntax_highlight(lang[0], code.string)
                if self.config.CLIPBOARD:
                    print code.string
                    in_pre_code+='<blockquote class="highlight ' + lang[0] + '"><p><a href="#" class="clipboard" data-clipboard-text="'+code.string+'"  data-clipboard-action="copy">copy</a></p></blockquote>'

                
                code.parent.replaceWith(in_pre_code)

        return soup

    def modify_html(self, soup):
        tags = []
        title_tags = ['h1', 'h2', 'h3', 'h4']
        [tags.extend(soup.find_all(title_tag)) for title_tag in title_tags]

        # h1, h2 add id attribute
        for tag in tags:
            id_str = tag.string.lower()
            splitted = id_str.split(' ')

            if len(splitted) > 0:
                tag['id'] = '-'.join(splitted)
 

        return soup.prettify(formatter=None)






# <blockquote>
# <p>
# <a>


# soup = BeautifulSoup("<blockquote></blockquote>")
# blockquote = soup.blockquote
# blockquote['class'] = 'highlight ' + lang[0]
# p = soup.new_tag('p')
# a = soup.new_tag('a', href="#")
# a.attrs("")



# blockquote.
