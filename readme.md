# 🦜🔗 YouTube GPT Creator

This project is intended to help you get a quickstart on Large Language Models (LLMs).  You will learn how to build your very own AutoGPT model using a framework that is taking the programming community by storm  - LangChain.

We will use streamlit, langchain, Wikipedia and openai to develop a web app that takes a keyword input and produces a title and script for a video. 

Watch this made on YouTube - https://youtu.be/MlK6SIjcjE8

# Setup the sample
To use the script, you will need to follow these steps:
- Clone the repository via `git clone https://github.com/nicknochnack/Langchain-Crash-Course.git` and `cd` into the cloned repository.
- Install the required packages: `pip install -r requirements.txt`
- Copy the .env.template file to .env: `cp .env.template .env`. This is where you will set the following variables.
- Set your OpenAI API key in the OPENAI_API_KEY
   
# Run the sample
- Run the script: `streamlit run app.py`

# What to expect
Streamlit will spin up a page that will look like this
<img src=/assets/start.png>
Go ahead and type in the keyword / subject for which you would like this program to do research on wikipedia and write up the script for your video and press return / enter.  After a few seconds, you will see details on the page for your quick start script including the research used from Wikipedia search.
<img src=/assets/page.png height=400>

Have fun creating your YouTube video.