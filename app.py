# Bring in deps
import os 
from apikey import apikey 

# Fixed for the new imports moving to 0.2.0
import streamlit as st 
#from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
#from langchain.utilities import WikipediaAPIWrapper 
#from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain_community.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('🦜🔗 YouTube GPT Creator')
prompt = st.text_input('Plug in your prompt here') 

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} '
)

# Memory 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# Llms
llm = OpenAI(temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

wiki = WikipediaAPIWrapper()

# Adapted for dict outputs of .invoke
# Show stuff to the screen if there's a prompt
if prompt: 
    title = title_chain.invoke(prompt)
    wiki_research = wiki.run(prompt) 
    script = script_chain.invoke(input={'title':title['title'], 'wikipedia_research':wiki_research})

    with st.expander('Title History'): 
        st.info(title['title'])

    with st.expander('Script History'): 
        st.info(script['script'])

    with st.expander('Wikipedia Research'): 
        st.info(wiki_research)
