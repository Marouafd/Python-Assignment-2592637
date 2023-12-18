import unittest
from unittest.mock import patch
from newPy import read_names, read_values, generate_abbreviations_for_word, calculate_score

class TestNewPy(unittest.TestCase):
    def setUp(self):
        # Set up any initial conditions for your tests
        pass

    def tearDown(self):
        # Clean up after each test
        pass

    def test_read_names(self):
        # Test the read_names function with your provided trees.txt
        names = read_names('trees.txt')
        expected_names = [
            'Alder', 'Crab Apple', 'Common Ash', 'Silver Birch', 'Downy Birch', 'European Beech', 'Box', 'Wild Cherry',
            'Bird Cherry', 'Blackthorn', 'Wych Elm', 'Smooth-leaved Elm', 'Common Hawthorn', 'Midland Hawthorn',
            'Common Hazel', 'European Hornbeam', 'European Holly', 'Common Juniper', 'Small-leaved Lime',
            'Large-leaved Lime', 'Field Maple', 'Pedunculate Oak', 'Sessile Oak', 'Scots Pine', 'Aspen', 'Black Poplar',
            'European Rowan', 'Common Whitebeam', 'Service Tree', 'Wild Service Tree', 'Strawberry Tree', 'Bay Willow',
            'Crack Willow', 'White Willow', 'Almond-leaved Willow', 'European Yew', 'Alder Buckthorn', 'Purging Buckthorn',
            'Elder', 'Common Dogwood', 'Rock Whitebeam', 'Sea-buckthorn', 'Spindle', 'Sallow', 'Grey Willow',
            'Purple Willow', 'Common Osier', 'Eared Willow', 'Guelder Rose', 'Wayfaring tree', 'Common Privet', "Plot's Elm"
        ]
        self.assertEqual(names, expected_names)

    def test_read_values(self):
        # Test the read_values function with your provided values.txt
        values = read_values('values.txt')
        expected_values = {
            'A': 25, 'B': 8, 'C': 8, 'D': 9, 'E': 35, 'F': 7, 'G': 9, 'H': 7,
            'I': 25, 'J': 3, 'K': 6, 'L': 15, 'M': 8, 'N': 15, 'O': 20, 'P': 8,
            'Q': 1, 'R': 15, 'S': 15, 'T': 15, 'U': 20, 'V': 7, 'W': 7, 'X': 3,
            'Y': 7, 'Z': 1
        }
        self.assertEqual(values, expected_values)

    def test_generate_abbreviations_for_word(self):
        # Mock the random.sample function to always return 'BC'
        with patch('random.sample', return_value=['B', 'C']):
            abbreviations = generate_abbreviations_for_word('ABC', {'A': 10, 'B': 5, 'C': 8})

        # Test the generated abbreviations
        self.assertEqual(abbreviations, {('ABC', 0)})

    def test_calculate_score(self):
        # Test the calculate_score function with a sample abbreviation and word
        score = calculate_score('ABC', 'ABC', {'A': 10, 'B': 5, 'C': 8})
        self.assertEqual(score, 0)

if __name__ == '__main__':
    unittest.main()
