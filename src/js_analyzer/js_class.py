from js_analyzer import JsMethod
import logging

log = logging.getLogger('JsClass')


class JsClass:
    def __init__(self, data: object, *, log_level: int = logging.INFO):
        self._log_level = log_level
        log.setLevel(log_level)
        self.name = data.id.name
        log.info('Found class %s' % self.name)
        self.methods = []
        log.debug('Searching for methods...')
        self.find_methods(data.body)
        self.attributes = []
        log.debug('Searching for attributes...')
        self.find_attributes()
        if len(self.attributes) > 0:
            log.debug(
                'Found attributes:\n\n%s\n'
                % (', '.join(attribute.name for attribute in self.attributes))
            )

    def find_methods(self, data: object) -> None:
        for method_data in data.body:
            if method_data.type == 'MethodDefinition':
                self.methods.append(JsMethod(method_data,
                                    log_level=self._log_level))

    def find_attributes(self) -> None:
        for method in self.methods:
            for attribute in method.find_attributes():
                self.attributes.append(attribute)

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'attributes': [
                attribute.to_dict() for attribute in self.attributes
            ],
            'methods': [
                method.to_dict() for method in self.methods
            ]
        }
