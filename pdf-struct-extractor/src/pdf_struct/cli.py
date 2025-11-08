import argparse
from .readers.pdf_reader import PdfReader
from .parsers.text_parser import TextParser
from .transformers.struct_transformer import StructTransformer

def main():
    parser = argparse.ArgumentParser(description="PDF Structure Extractor")
    parser.add_argument('file_path', type=str, help='Path to the PDF file to be processed')
    
    args = parser.parse_args()
    
    # Read the PDF file
    pdf_reader = PdfReader()
    raw_text = pdf_reader.read_pdf(args.file_path)
    
    # Parse the raw text
    text_parser = TextParser()
    parsed_data = text_parser.parse_text(raw_text)
    
    # Transform the parsed data into structured format
    struct_transformer = StructTransformer()
    structured_data = struct_transformer.transform_data(parsed_data)
    
    # Output the structured data
    print(structured_data)

if __name__ == "__main__":
    main()