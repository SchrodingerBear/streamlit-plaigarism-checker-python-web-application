import nltk
import os

nltk_data_path = os.path.expanduser('~/nltk_data')
if nltk_data_path not in nltk.data.path:
    nltk.data.path.append(nltk_data_path)

print("Updated NLTK Paths:", nltk.data.path)  # Debugging output

nltk.download('punkt', download_dir=nltk_data_path, quiet=True)
nltk.download('stopwords', download_dir=nltk_data_path, quiet=True)
