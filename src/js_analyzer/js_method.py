from js_analyzer import JsIdentifier
import logging

log = logging.getLogger('JsMethod')


class JsMethod:
    def __init__(self, data: object, *, log_level: int = logging.INFO):
        self._log_level = log_level
        log.setLevel(log_level)
        self.name = data.key.name
        self._body = data.value.body
        log.info('Found method %s()' % self.name)
        log.debug('Searching for arguments...')
        self.arguments = [
            JsIdentifier(argument) for argument in data.value.params
        ]
        if len(self.arguments) > 0:
            log.debug(
                'Found arguments\n\n%s\n'
                % ', '.join(
                    [str(argument.name) for argument in self.arguments]
                )
            )

    def find_attributes(self):
        log.debug('Searching for attributes in method %s()' % self.name)
        for statement in self._body.body:
            if (statement.type == 'ExpressionStatement'
                    and statement.expression.type == 'AssignmentExpression'
                    and statement.expression.left.type == 'MemberExpression'):
                attribute = JsIdentifier(statement.expression.left.property)
                if statement.expression.right.type == 'ArrayExpression':
                    attribute.set_type('Array')
                yield attribute

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'arguments': [
                argument.to_dict() for argument in self.arguments
            ]
        }
