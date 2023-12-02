import re

def clean_transcript(text):
  # Remove timestamps
  text = re.sub(r"\[\d\d:\d\d\] ", "", text)

  # Remove speaker annotations
  text = re.sub(r"\(.\)\s?", "", text)

  # Remove unnecessary line breaks and whitespaces
  text = re.sub(r"\n\s+", " ", text)

  # Remove non-printable characters
  text = re.sub(r"[^\x00-\x7F]+", "", text)

  return text