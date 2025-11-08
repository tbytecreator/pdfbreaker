import unittest
from pdf_struct.transformers.struct_transformer import StructTransformer

class TestStructTransformer(unittest.TestCase):

    def setUp(self):
        self.transformer = StructTransformer()

    def test_transform_data(self):
        parsed_data = {
            'title': 'Sample Title',
            'author': 'Sample Author',
            'content': 'This is a sample content extracted from the PDF.'
        }
        expected_output = {
            'title': 'Sample Title',
            'author': 'Sample Author',
            'content': 'This is a sample content extracted from the PDF.'
        }
        result = self.transformer.transform_data(parsed_data)
        self.assertEqual(result, expected_output)

    def test_transform_empty_data(self):
        parsed_data = {}
        expected_output = {}
        result = self.transformer.transform_data(parsed_data)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()