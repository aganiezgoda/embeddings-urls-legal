# flake8: noqa
from langchain.prompts import PromptTemplate

template = """{summaries}

The text above presents a request for information sent by a citizen to a government institution and the institution's response.
The text above contains the official stance of the institution. 
Every text is independent from other texts. Don't mix information from different texts (sources).
Please reply to the question below using only the information present in the text or texts above.
If you can't find it, reply politely that the information is not in the knowledge base.
Detect the language of the question and answer in the same language. 
If asked for enumerations list all of them and do not invent any.
Each source has a name followed by a colon and the actual information, always include the source name for each fact you use in the response. Always use double square brackets to reference the filename source, e.g. [[info1.pdf.txt]]. Don't combine sources, list each source separately, e.g. [[info1.pdf]][[info2.txt]].
Try not to repeat questions that have already been asked.

Question: {question}
Answer:"""

PROMPT = PromptTemplate(template=template, input_variables=["summaries", "question"])

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)


