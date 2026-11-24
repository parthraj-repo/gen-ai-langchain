from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

user_review=input('write a review')

class review(TypedDict):
    key_themes: Annotated[list[str], 'write down all the keys']
    review: Annotated[str, ' a brief summary of the review']
    sentiment: Annotated[str, 'return sentiment either negative or positive']
    pros: Annotated[Optional[list[str]], 'write doen all the pros']
    optional_sentiment: Annotated[Literal['pos','neg'], 'return sentiment of the review either pos or neg']

model=ChatOpenAI()
structured_model=model.with_structured_output(review)

result=structured_model.invoke(user_review)

print(result)
print(result['review'])   # only review

print(result['sentiment'])  # only sentiment
 


