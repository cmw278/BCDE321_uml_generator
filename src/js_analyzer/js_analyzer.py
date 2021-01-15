import esprima
from js_analyzer import JsClass
from pathlib import Path
import logging

log = logging.getLogger('JsAnalyzer')


class JsAnalyzer:
    def __init__(self, name: str):
        log.debug('Initializing analyzer...')
        log.info('Analyzing %s...' % name)
        self.name = name
        self.classes = []

    def load_file(self, filepath: Path) -> None:
        if filepath.suffix.lower() != '.js':
            log.warning('Cannot process `%s` filetype. Skipping file `%s`'
                        % (filepath.suffix, filepath.name))
            return None
        log.info('Opening file: %s' % filepath)
        file_ = open(filepath)
        log.debug('File opened.')
        data = esprima.parse(file_.read())
        file_.close()
        del file_
        self.load_data(data)

    def load_data(self, data: object) -> None:
        log.debug('Searching for classes...')
        for class_data in data.body:
            if class_data.type == 'ClassDeclaration':
                self.classes.append(JsClass(class_data))

    def to_dict(self) -> dict:
        return {
            'folder_name': self.name,
            'classes': [class_.to_dict() for class_ in self.classes]
        }
