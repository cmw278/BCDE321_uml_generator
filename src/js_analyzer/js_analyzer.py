import esprima
from js_analyzer import JsClass


class JsAnalyzer:
    def __init__(self):
        self._classes = []

    def load_file(self, filepath: str) -> None:
        file_ = open(filepath)
        data_ = esprima.parse(file_.read())
        file_.close()
        del file_
        self.load_data(data_)

    def load_data(self, data_: dict) -> None:
        if 'body' in data_:
            self._classes.append(
                JsClass(class_data) for class_data in
                data_['body'] if class_data['type'] == 'ClassDeclaration')
