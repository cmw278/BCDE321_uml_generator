import esprima
from js_analyzer import JsClass


class JsAnalyzer:
    def __init__(self):
        self._classes = []

    def load_file(self, filepath: str) -> None:
        file_ = open(filepath)
        data = esprima.parse(file_.read())
        file_.close()
        del file_
        self.load_data(data)

    def load_data(self, data_: dict) -> None:
        if 'body' in data_:
            self._classes.append(
                JsClass(class_dict) for class_dict in
                data_['body'] if class_dict['type'] == 'ClassDeclaration')
