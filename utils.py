import spacy
from spacy import displacy

# Function to load spaCy model for Named Entity Recognition (NER)
def load_spacy_model():
    nlp = spacy.load("en_core_web_sm")  # You can use a more advanced model if needed
    return nlp

# Function to display named entities in the report
def show_named_entities(report_text):
    nlp = load_spacy_model()
    doc = nlp(report_text)
    return [(ent.text, ent.label_) for ent in doc.ents]
