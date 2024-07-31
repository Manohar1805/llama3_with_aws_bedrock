from langchain_community.llms import Bedrock
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import boto3

bedrock_client=boto3.client(service_name="bedrock-runtime",
             region_name="us-east-1",
             )
model_id="meta.llama3-8b-instruct-v1:0"

llm=Bedrock(
    model_id=model_id,
    client=bedrock_client
)

def my_model(user_prompt):
    prompt=PromptTemplate(input_variables=["user_text"],
                          template="you are a chatbot , provide the answer for {user_prompt}")
    
    bedrock_chain=LLMChain(llm=llm,prompt=prompt)
    response=bedrock_chain({"user_prompt":user_prompt})

    return response

user_prompt="what is python"

reponse=my_model(user_prompt)['text'].strip()

print(reponse)