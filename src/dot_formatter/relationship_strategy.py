from abc import ABC, abstractmethod


class RelationshipStrategy(ABC):
    @abstractmethod
    def compose_string(self, source_class: str,
                       target_class: str, label: str) -> str:
        pass
