from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template= ChatPromptTemplate([
    ('system', 'you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])


# load chat history

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
    

# now invoke chat_template