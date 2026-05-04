import os
from pypdf import PdfReader, PdfWriter, PaperSize

# Folder configurations
DOCS_FOLDER = './documents'
COVERS_FOLDER = './covers'
OUTPUT_FILENAME = 'merged_document.pdf'

def merge_pdfs_with_normalization():
    writer = PdfWriter()
    
    # Standard A4 dimensions for consistency
    A4_WIDTH = PaperSize.A4.width
    A4_HEIGHT = PaperSize.A4.height

    # Get all PDF files from the documents folder
    try:
        documents = sorted([f for f in os.listdir(DOCS_FOLDER) if f.endswith('.pdf')])
    except FileNotFoundError:
        print(f"Error: The folder '{DOCS_FOLDER}' was not found.")
        return

    if not documents:
        print("No PDF files found in the documents folder.")
        return

    for doc_name in documents:
        doc_path = os.path.join(DOCS_FOLDER, doc_name)
        
        print(f"Processing: {doc_name}...")

        # 1. Add and Resize Document Pages
        doc_reader = PdfReader(doc_path)
        for page in doc_reader.pages:
            page.scale_to(width=A4_WIDTH, height=A4_HEIGHT)
            writer.add_page(page)

        # 2. Add and Resize Cover Page
        # This logic looks for a generic 'standard_cover.pdf' in the covers folder
        cover_path = os.path.join(COVERS_FOLDER, 'standard_cover.pdf') 
        
        if os.path.exists(cover_path):
            cover_reader = PdfReader(cover_path)
            for page in cover_reader.pages:
                page.scale_to(width=A4_WIDTH, height=A4_HEIGHT)
                writer.add_page(page)
        else:
            print(f"Warning: Cover not found at {cover_path}. Skipping cover for {doc_name}.")

    # Write the final merged file
    try:
        with open(OUTPUT_FILENAME, "wb") as output_file:
            writer.write(output_file)
        print(f"\nSuccess! '{OUTPUT_FILENAME}' generated with uniform page sizes.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    # Requirement: pip install pypdf
    merge_pdfs_with_normalization()

