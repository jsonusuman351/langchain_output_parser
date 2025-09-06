from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1", task="text-generation")

model=ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(..., description="The name of the person")
    age: int = Field(gt=18, description="The age of the person")
    city: str = Field(..., description="The city where the person lives")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(template='give me the name ,age,and city of a fictional {place}person\n{format_instructions}',input_variables=['place'],partial_variables={'format_instructions':parser.get_format_instructions()})

chain= template | model | parser
final_result=chain.invoke({'place':'from India '})
print(final_result)