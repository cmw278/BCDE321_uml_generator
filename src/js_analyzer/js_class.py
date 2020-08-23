from js_analyzer import JsMethod


class JsClass:
    def __init__(self, data_: dict):
        self.name = data_['id']['name']
        self.methods = []
        self.load_data(data_)
        self.attributes = []
        self.get_attributes()

    def load_data(self, data_: dict) -> None:
        if 'body' in data_:
            self._methods.append(
                JsMethod(method_data) for method_data in
                data_['body'] if method_data['type'] == 'MethodDeclaration')

    def get_attributes(self) -> None:
        attributes = [].append(
            method.get_attributes() for method in self.methods
        )
        self.attributes.append(attribute for attribute in attributes)
