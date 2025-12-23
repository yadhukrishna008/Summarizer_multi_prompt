from pydantic import BaseModel


class SummarizeResponseList(BaseModel):
    summaries: list[str]

class SummarizeRequest(BaseModel):
    text:str

class SummarizeResponse(BaseModel):
    text:str


prompts= [
    """Summarize the following text in one concise paragraph. 
    Do not include any extra details or commentary. Only return the summary.

    Text:
    {TEXT}
    Summary:
    """,
    """Please summarize the following text into 2-3 concise sentences.
    Do not include any extra details, explanations, or commentary — only the summary.
    
    Text:
    {TEXT}
    Summary:
    """,
    """Summarize the following text in 1–2 sentences.
    Do not repeat phrases from the original text.
    Return only the summary.
    
    Text:
    {TEXT}
    Summary:
    """,
    """Create a clear and concise summary of the text below.
    Focus only on the main ideas and ignore examples or minor details.
    Return only the summarized text.
    Text:
    {TEXT}
    Summary:
    """,
    """Summarize the text below in a single sentence.
    Keep it under 25 words.
    Return only the summary.
    
    Text:
    {TEXT}
    Summary:
    """
]