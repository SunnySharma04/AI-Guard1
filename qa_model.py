from transformers import pipeline

# Function to load the question-answering model
def load_qa_model():
    # Using a pre-trained BERT-based model fine-tuned for question-answering
    return pipeline("question-answering", model="deepset/roberta-base-squad2")

# Function to answer user questions based on the cleaned report
def get_answer(model, context, question):
    result = model(context=context, question=question)
    return result['answer']
