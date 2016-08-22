# -*- coding:utf-8 -*-


class DocumentTraceFile(object):
    """

    """

    def __init__(self, tracing_file_path, is_index_file=False):
        if tracing_file_path:
            self.file_path = tracing_file_path
            self.is_index_file = is_index_file
        else:
            raise Exception("tracing_file_path is None.")
