# PDF Struct Extractor

PDF Struct Extractor is a Python project designed to read PDF files and transform their content into structured data. This project provides a command-line interface for users to easily interact with the PDF extraction functionality.

## Project Structure

```
pdf-struct-extractor
├── src
│   └── pdf_struct
│       ├── __init__.py
│       ├── cli.py
│       ├── main.py
│       ├── readers
│       │   └── pdf_reader.py
│       ├── parsers
│       │   └── text_parser.py
│       ├── transformers
│       │   └── struct_transformer.py
│       ├── schemas
│       │   └── schema.py
│       └── utils.py
├── tests
│   ├── test_pdf_reader.py
│   └── test_transformer.py
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To use the PDF Struct Extractor, you can run the command-line interface provided in `cli.py`. This allows you to specify the PDF file you want to process and receive structured data as output.

## Example

1. Place your PDF file in the desired directory.
2. Run the command:

```
python src/pdf_struct/cli.py --file path/to/your/file.pdf
```

3. The output will be the structured data extracted from the PDF.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.