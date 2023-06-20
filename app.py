import streamlit as st
import openai
import os
from Configuracion import secret_key

openai.api_key  = secret_key
#DALL-E 
def get_dalle(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024")
    return response['data'][0]['url']
#Chat GPT 3.5
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # este es el grado de aleatoriedad de la salida del modelo
    )
    return response.choices[0].message["content"]

st.set_page_config(
    page_title="ChatPlus",layout="wide",
    page_icon="📱"
)

import base64

main_bg = "earth-leaf-greenery-wallpaper-preview.jpg"
main_bg_ext = "jpg"

side_bg = "earth-leaf-greenery-wallpaper-preview.jpg"
side_bg_ext = "jpg"

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://user-images.githubusercontent.com/93687273/217873392-7fee4e67-6c2e-401b-bb81-229509cdca67.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
def sidebar_bg(side_bg):

   side_bg_ext = 'gif'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
side_bg = '8e7f7da679e6aca5cdf9e84b930c531f_AdobeExpress.gif'
sidebar_bg(side_bg)
   

def main():
  text= st.sidebar.text_input(":white[CHAT-GPT]",
                           help="Escribe tu consulta en el espacio y presiona () para enviar. ",
                           placeholder="Escribe aquí")
  if st.sidebar.button("Response"):
   prompt = f"""
    Responder el texto delimitado en comillas \.
    ```{text}```
    """ 
   response = get_completion(prompt)
   st.write(response)
  

   
  texto2=st.sidebar.text_input(placeholder="Escribe aquí",label=":white[DALL-E]")
  if st.sidebar.button("Response "):
   prompt = f"{texto2}"
   response = get_dalle(prompt)
   #st.write(response)
   st.image(response)   
if __name__ =="__main__":
    main()
    
