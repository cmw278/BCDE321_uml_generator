class JsIdentifier:
    def __init__(self, data: object):
        self.name = data.name
        self.type = 'any'

    def set_type(self, new_type: str) -> None:
        self.type = new_type

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'type': self.type
        }
