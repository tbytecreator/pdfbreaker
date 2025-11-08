# main.py

from pdf_struct.readers.pdf_reader import PdfReader
from pdf_struct.parsers.text_parser import TextParser
from pdf_struct.transformers.struct_transformer import StructTransformer

def main(file_path):
    # Step 1: Read the PDF file
    pdf_reader = PdfReader()
    raw_text = pdf_reader.read_pdf(file_path)

    # Step 2: Parse the raw text
    text_parser = TextParser()
    parsed_data = text_parser.parse_text(raw_text)

    # Step 3: Transform the parsed data into structured format
    struct_transformer = StructTransformer()
    structured_data = struct_transformer.transform_data(parsed_data)

    return structured_data

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_pdf>")
        sys.exit(1)

    file_path = sys.argv[1]
    structured_data = main(file_path)
    print(structured_data)