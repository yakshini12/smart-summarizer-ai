import fitz  # PyMuPDF
from summarizer import summarize_text
from tts_speaker import speak_summary

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

if __name__ == "__main__":
    pdf_path = "test_doc.pdf"  # Make sure the file is in the same folder
    text = extract_text_from_pdf(pdf_path)

    print("\n📄 PDF Content Preview:\n", text[:500])

    summary = summarize_text(text, num_sentences=3)
    print("\n🧠 Summary:\n", summary)

    choice = input("\n🎧 Want to hear the summary? (y/n): ").lower()
    if choice == 'y':
        speak_summary(summary)
