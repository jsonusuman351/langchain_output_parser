from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1", task="text-generation")

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template=PromptTemplate(template='give me the name ,age,and city of a fictional person\n{format_instructions}',input_variables=[],partial_variables={'format_instructions':parser.get_format_instructions()})


chain= template | model | parser
response=chain.invoke({}) 
print(response)