import os
from pypdf import PdfReader, PdfWriter, PaperSize

# Folder configuration
DOCS_FOLDER = './documents'
COVERS_FOLDER = './covers'
OUTPUT_FILENAME = 'projeto_completo.pdf'

# Default cover fallback
DEFAULT_COVER = 'default.pdf'


def add_pdf_preserve_aspect(writer, path, A4_WIDTH, A4_HEIGHT):
    """
    Add pages from a PDF to the writer:
    - Preserves original aspect ratio
    - Scales to fit within A4
    - Centers content on the page
    """
    reader = PdfReader(path)

    for page in reader.pages:
        original_width = float(page.mediabox.width)
        original_height = float(page.mediabox.height)

        # Calculate proportional scale
        scale = min(A4_WIDTH / original_width, A4_HEIGHT / original_height)

        new_width = original_width * scale
        new_height = original_height * scale

        # Calculate centering offsets
        x_offset = (A4_WIDTH - new_width) / 2
        y_offset = (A4_HEIGHT - new_height) / 2

        # Apply scaling
        page.scale_by(scale)

        # Create blank A4 page
        new_page = writer.add_blank_page(width=A4_WIDTH, height=A4_HEIGHT)

        # Merge transformed page into A4 canvas
        new_page.merge_transformed_page(
            page,
            [1, 0, 0, 1, x_offset, y_offset]
        )


def find_cover(doc_name):
    """
    Cover selection strategy:
    1. Look for a cover with the same name as the document
    2. Fallback to default cover
    3. Return None if no cover is found
    """
    specific_cover = os.path.join(COVERS_FOLDER, doc_name)

    if os.path.exists(specific_cover):
        return specific_cover

    default_cover = os.path.join(COVERS_FOLDER, DEFAULT_COVER)

    if os.path.exists(default_cover):
        return default_cover

    return None


def merge_architecture_project():
    writer = PdfWriter()

    # A4 dimensions
    A4_WIDTH = PaperSize.A4.width
    A4_HEIGHT = PaperSize.A4.height

    # Load document list
    try:
        documents = sorted([
            f for f in os.listdir(DOCS_FOLDER)
            if f.lower().endswith('.pdf')
        ])
    except FileNotFoundError:
        print("Error: 'documents' folder not found.")
        return

    if not documents:
        print("No PDF files found in documents folder.")
        return

    print(f"{len(documents)} document(s) found.")

    # Process each document
    for doc in documents:
        doc_path = os.path.join(DOCS_FOLDER, doc)

        print(f"\nProcessing: {doc}")

        # Find matching cover
        cover_path = find_cover(doc)

        if cover_path:
            print(f"  Adding cover: {os.path.basename(cover_path)}")
            add_pdf_preserve_aspect(writer, cover_path, A4_WIDTH, A4_HEIGHT)
        else:
            print("  No cover found")

        # Add document pages
        print("  Adding document pages")
        add_pdf_preserve_aspect(writer, doc_path, A4_WIDTH, A4_HEIGHT)

    # Write output file
    try:
        with open(OUTPUT_FILENAME, "wb") as f:
            writer.write(f)

        print(f"\nOutput generated: {OUTPUT_FILENAME}")

    except Exception as e:
        print(f"Error while saving file: {e}")


if __name__ == "__main__":
    # Requirement: pip install pypdf
    merge_architecture_project()
