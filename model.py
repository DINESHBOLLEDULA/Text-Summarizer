import torch
from transformers import BartForConditionalGeneration, BartTokenizer

model_name = "facebook/bart-large-cnn"

# Load model and tokenizer
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)


def generate_summary(text):

    text_to_summarize = text
    # Encode text to summarize
    inputs = tokenizer(text_to_summarize, return_tensors="pt")

    # Generate summary
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=512, early_stopping=True)
    summary = tokenizer.batch_decode(summary_ids, skip_special_tokens=True)[0]

    return summary