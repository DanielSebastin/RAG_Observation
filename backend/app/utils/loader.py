import os
from pypdf import PdfReader
from docx import Document

def load_txt(path):
    with open(path,"r",encoding="utf-8") as f:
        return f.read()

def load_pdf(path):
    reader=PdfReader(path)
    text=""
    for page in reader.pages:
        text+=page.extract_text() or ""
    return text

def load_docx(path):
    doc=Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_document(path):
    ext=os.path.splitext(path)[1].lower()

    if ext==".txt":
        return load_txt(path)
    elif ext==".pdf":
        return load_pdf(path)
    elif ext==".docx":
        return load_docx(path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")