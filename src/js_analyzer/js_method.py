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
            JsIdentifier(argument) if argument.type != 'AssignmentPattern'
            else JsIdentifier(argument.left)
            for argument in data.value.params
        ]
        if len(self.arguments) > 0:
            log.debug(
                'Found arguments\n\n%s\n'
                % ', '.join(
                    [str(argument.name) for argument in self.arguments]
                )
            )

    def find_attributes(self):
        """Generator that searches for member attributes assigned in any
        methods. This usually occurs in class constructors, but may also
        occur in other places.

        ---
        `yields -> JsIdentifier`
        > Creates an instance of JsIdentifier for each attribute discovered.
        """
        log.debug('Searching for attributes in method %s()' % self.name)
        for attribute in self.recursive_attribute_search(self._body.body):
            yield attribute

    def recursive_attribute_search(self, body: list):
        """Recursive search for member attributes.

        ---
        Required Positional Arguments:

        `[0] body: list`
        > The body of a block expression as found in data produced
        by `esprima.parse()`.
        """
        for statement in body:
            try:
                if (statement.type == 'ExpressionStatement'
                        and statement.expression.type
                        == 'AssignmentExpression'
                        and statement.expression.left.object.type
                        == 'ThisExpression'):
                    attribute = JsIdentifier(
                        statement.expression.left.property)
                    if statement.expression.right.type == 'ArrayExpression':
                        attribute.set_type('Array')
                    yield attribute
                elif statement.body.type == 'BlockStatement':
                    for attribute in self.recursive_attribute_search(
                            statement.body.body):
                        yield attribute
            except AttributeError as error:
                log.debug(str(error))
                # AttributeError suggests this is not a supported statement
                # type. Move on to the next one.
                continue

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'arguments': [
                argument.to_dict() for argument in self.arguments
            ]
        }
