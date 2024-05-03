import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get response from my llm Llama2 model

def getLlamaResponse(input_text,no_of_words,blog_style):
    # Llama2 model
    llm = CTransformers(model = 'model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config = {'max_new_tokens':256,
                                  'temperature':0.01})
    # Prompt Template
    template = '''
    Write a blog for {blog_style} job profile for a topic {input_text}
    within {no_of_words}.
        '''
    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_of_words"],
                            template=template)
    # Generation of response from Llama2 Model
    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_of_words=no_of_words))
    print(response)
    return response

# Using streamlit to create a UI
st.set_page_config(page_title="Generate Blogs", 
                   page_icon="🤖", 
                   layout='centered', 
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the blog topic")

# creating 2 more columns for additional 2 fields

col1, col2 = st.columns([5,5])

with col1:
    no_of_words = st.text_input('No of words')
    
with col2:
    blog_style=st.selectbox("For whom blog is written",
                            ('Researchers','Scientist','Common Person'),index=0)
    
submit = st.button("Generate")

# Final Response
if submit:
    st.write(getLlamaResponse(input_text,no_of_words,blog_style))