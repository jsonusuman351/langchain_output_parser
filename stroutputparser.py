from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1", task="text-generation")

model=ChatHuggingFace(llm=llm)

# 1st prompt..........detailed report

template1=PromptTemplate(
    template='write a detailed report on the topic: {topic}',
    input_variables=['topic']
)

# 2nd prompt..........summary of the report
template2=PromptTemplate(
    template='write 5 line summary on the following text.\n{text}',
    input_variables=['text']
)


prompt1=template1.invoke({'topic':'Artificial Intelligence'})

result=model.invoke(prompt1)

prompt2=template2.invoke({'text':result.content})
summary=model.invoke(prompt2)

print(summary.content)  