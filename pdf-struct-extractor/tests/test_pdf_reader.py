import unittest
from pdf_struct.readers.pdf_reader import PdfReader

class TestPdfReader(unittest.TestCase):

    def setUp(self):
        self.pdf_reader = PdfReader()

    def test_read_pdf_valid_file(self):
        # Assuming there's a sample PDF file for testing
        content = self.pdf_reader.read_pdf('sample.pdf')
        self.assertIsInstance(content, str)
        self.assertGreater(len(content), 0)

    def test_read_pdf_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            self.pdf_reader.read_pdf('invalid_file.pdf')

    def test_read_pdf_empty_file(self):
        # Assuming there's a way to create an empty PDF for testing
        content = self.pdf_reader.read_pdf('empty.pdf')
        self.assertEqual(content, '')

if __name__ == '__main__':
    unittest.main()