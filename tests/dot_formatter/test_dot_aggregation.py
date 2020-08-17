from unittest import TestCase
from dot_formatter import DotAggregation
from test_dot_inheritance import TestDotInheritance

# Test data dictionary
from test_data import DATA


class TestDotAggregation(TestDotInheritance):

    def setUp(self):
        # TODO: Implement DotAggregation
        self.skipTest('Awaiting implementation of DotAggregation')
        source_class = DATA['relationship']['source_class']
        target_class = DATA['relationship']['target_class']
        label = DATA['relationship']['label']
        self.test_data = {
            'options': {
                'label': label,
                'arrowtail': 'ediamond'
            },
            'source_class': target_class,
            'target_class': source_class,
        }
        self.relationship = DotAggregation(
            source_class,
            target_class,
            label
        )
