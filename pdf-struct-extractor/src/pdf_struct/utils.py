def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def read_file(file_path):
    """Reads the content of a file and returns it."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """Writes content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def validate_pdf_path(file_path):
    """Validates if the provided file path is a PDF file."""
    return file_path.lower().endswith('.pdf')