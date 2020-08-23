class JsIdentifier:
    def __init__(self, data_: dict):
        self.name = data_['name']
        self.type = 'any'

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'type': self.type
        }
