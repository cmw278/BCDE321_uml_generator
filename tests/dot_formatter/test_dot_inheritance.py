from unittest import TestCase
from dot_formatter import DotInheritance
from test_dot_association import TestDotAssociation

# Test data dictionary
from test_data import DATA


class TestDotInheritance(TestDotAssociation):

    def setUp(self):
        source_class = DATA['relationship']['source_class']
        target_class = DATA['relationship']['target_class']
        self.test_data = {
            'options': {
                'label': '',
                'arrowtail': 'empty'
            },
            'source_class': source_class,
            'target_class': target_class
        }
        self.relationship = DotInheritance(
            source_class,
            target_class
        )

    def test_to_string(self):
        source = self.test_data['source_class']
        target = self.test_data['target_class']
        label = self.test_data['options']['label']
        arrow = self.test_data['options']['arrowtail']
        expected = ('\n%s -> %s [\nlabel="%s"\narrowtail="%s"\n]'
                    % (target, source, label, arrow))
        actual = str(self.relationship)
        self.assertEqual(actual, expected)
