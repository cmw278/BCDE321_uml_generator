from js_analyzer import JsIdentifier


class JsMethod:
    def __init__(self, data_: dict):
        self.name = data_['key']['name']
        self.arguments = [
            JsIdentifier(argument) for argument in data_['value']['params']
        ]
        self._body = data_['body']

    def get_attributes(self) -> list:
        attributes = []
        for expression in self._body['body']:
            if (expression['expression']['type']
                    == 'AssignmentExpression'
                    and expression['expression']['left']['type']
                    == 'MemberExpression'):
                attributes.append(
                    JsIdentifier(
                        expression['expression']['left']['property']
                    )
                )
        return attributes
