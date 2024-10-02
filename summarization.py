from transformers import T5Tokenizer, T5ForConditionalGeneration

# Function to summarize the cleaned report using the T5 model
def summarize_report(report_text):
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    model = T5ForConditionalGeneration.from_pretrained('t5-small')

    # Prepare the text for summarization
    input_text = "summarize: " + report_text
    input_ids = tokenizer(input_text, return_tensors='pt').input_ids
    summary_ids = model.generate(input_ids, max_length=200, num_beams=4, early_stopping=True)

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
