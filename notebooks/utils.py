"""Helper functions and params"""
from pathlib import Path

from pandas import DataFrame
import spacy


DATA_PATH = Path("../data")
RAW_PATH = DATA_PATH / 'raw'
CLEANED_PATH = DATA_PATH / "cleaned"
MODELS_PATH = DATA_PATH / "models"

PARAMS = {
    'DATA_PATH': DATA_PATH,
    'RAW_PATH': RAW_PATH,
    'JOB_PATHS': list(RAW_PATH.glob("*jobs.csv")),
    'CLEANED_PATH': CLEANED_PATH,
    'LINES_PATH': CLEANED_PATH / "normalised_jobs.txt",
    'MODELS_PATH': MODELS_PATH,
    'BIGRAM_MODEL_PATH': MODELS_PATH / "bigram_model.model",
    'TRIGRAM_MODEL_PATH': MODELS_PATH / "trigram_model.model",
}


nlp = spacy.load("en_core_web_md")


# Define a couple of generator functions to handle the cleaning
def line_generator(df: DataFrame, col: str):
    """Generator for lines of text from a DataFrame column"""
    for text in df[col]:
        try:
            text.split()
            for line in text.split('\n'):
                yield line.strip()
        except Exception:
            print(type(text))
            print(text)
            breakpoint()


def parse_lines(df: DataFrame, col: str):
    """
    spaCy-parse text in a DataFrame column line by line
    
    spaCy won't detect newlines as sentence boundaries, so must do this explicitly first
    """
    for parsed_text in nlp.pipe(line_generator(df, col)):
        for sent in parsed_text.sents:
            yield ' '.join([token.lemma_.lower() for token in sent if not (token.is_punct or token.is_space)])
