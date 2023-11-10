from gtts import gTTS
import pdfplumber
from art import tprint
from pathlib import Path

class PdfToMp3Converter:
    def __init__(self, file_path='test.pdf', language='en'):
        self.file_path = Path(file_path)
        self.language = language

    def check_file_validity(self):
        """Check if the file exists and is a valid PDF."""
        return self.file_path.is_file() and self.file_path.suffix.lower() == '.pdf'

    def process_pdf_to_mp3(self):
        """Process the PDF, extract text, convert to MP3, and save the audio file."""
        if self.check_file_validity():
            print('[+] Processing...')
            with pdfplumber.open(self.file_path) as pdf:
                pages = [page.extract_text() for page in pdf.pages]

            text = ''.join(pages)
            text = text.replace('\n', '')

            audio_file = self.file_path.stem + '.mp3'
            my_audio = gTTS(text=text, lang=self.language, slow=False)
            my_audio.save(audio_file)

            return f'[+] {audio_file} saved successfully!'
        else:
            return "Invalid file. Please provide a valid PDF file."

def main():
    tprint('PDF >> TO >> MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example, 'en' or 'ru': ")

    # Create an instance of the PdfToMp3Converter class
    converter = PdfToMp3Converter(file_path=file_path, language=language)

    # Process PDF to MP3 and print the result
    result = converter.process_pdf_to_mp3()
    print(result)

if __name__ == '__main__':
    main()
