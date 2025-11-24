"""
Extract Stormlight Handbook for reference
"""

import sys
import os

try:
    import PyPDF2
    pdf_library = "PyPDF2"
except ImportError:
    print("Error: PyPDF2 not installed")
    print("Run: pip install PyPDF2")
    sys.exit(1)

def extract_handbook():
    pdf_path = "STC_Stormlight_Handbook_digital.pdf"
    output_path = "Handbook_extracted.txt"
    
    print(f"Extracting: {pdf_path}")
    print(f"Output: {output_path}")
    
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            total_pages = len(pdf_reader.pages)
            print(f"Total pages: {total_pages}")
            
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(f"=== Stormlight Handbook Extraction ===\n")
                output_file.write(f"=== Total Pages: {total_pages} ===\n\n")
                
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    print(f"Processing page {page_num}/{total_pages}...", end='\r')
                    
                    text = page.extract_text()
                    
                    if text.strip():
                        output_file.write(f"\n{'='*60}\n")
                        output_file.write(f"PAGE {page_num}\n")
                        output_file.write(f"{'='*60}\n\n")
                        output_file.write(text)
                        output_file.write("\n")
                
                print()
                print(f"[SUCCESS] Extracted to: {output_path}")
                
    except Exception as e:
        print(f"[ERROR] {e}")
        return False
    
    return True

if __name__ == "__main__":
    extract_handbook()

