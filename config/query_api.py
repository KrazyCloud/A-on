from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch


def get_answers(user_input, cleaned_transcript):
    # Initialize tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("Falconsai/question_answering_v2")
    model = AutoModelForQuestionAnswering.from_pretrained("Falconsai/question_answering_v2")

    max_seq_length = 254
    
    # Split the text into chunks
    chunks = [cleaned_transcript[i:i + max_seq_length] for i in range(0, len(cleaned_text), max_seq_length)]
    
    # Initialize variables to store answers
    all_answers = []

    # Process each chunk separately
    for chunk in chunks:
        inputs = tokenizer(user_input, chunk, return_tensors="pt", max_length=max_seq_length, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)

        # Get the answer text and append it to the list of answers
        answer_start_index = torch.argmax(outputs.start_logits)
        answer_end_index = torch.argmax(outputs.end_logits) + 1
        answer = tokenizer.decode(inputs.input_ids[0][answer_start_index:answer_end_index])
        all_answers.append(answer)
    return all_answers
