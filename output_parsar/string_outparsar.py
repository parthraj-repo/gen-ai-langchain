from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Step 1: Create string output parser
parser = StrOutputParser()

# Step 2: Create prompt template
template = PromptTemplate(
    template="Explain {topic} in simple words.",
    input_variables=["topic"]
)

# Step 3: Initialize model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="YOUR_API_KEY"
)

# Step 4: Format prompt
final_prompt = template.format(topic="Machine Learning")

# Step 5: Invoke model
response = model.invoke(final_prompt)

# Step 6: Parse output
result = parser.parse(response.content)

print(result)
print(type(result))