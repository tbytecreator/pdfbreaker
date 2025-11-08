class PdfReader:
    def read_pdf(self, file_path):
        import PyPDF2
        
        # Open the PDF file
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            
            # Extract text from each page
            for page in reader.pages:
                text += page.extract_text() + '\n'
        
        return text.strip()  # Return the extracted text, stripped of leading/trailing whitespace