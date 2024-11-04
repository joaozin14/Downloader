import streamlit as st
from pytubefix import *
from download_youtube import download

st.markdown("""
    <h1 class="titulo">Downloader</h1> 
    <style>
    .titulo{
        text-align: center;
        color: #c4302b;
        text-shadow: 2px 2px 5px red;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" class="imagem-livre">
    <style>
    .imagem-livre {
        position: absolute;
        left: 470px;
        bottom: 15px;
        width: 60px; 
        height: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <h2 class="texto">Insira a URL do vídeo para que o download inicie 👍🏻</h2> 
    <style>
    .texto {
        text-align: center;
        color: #c4302b;
        text-shadow: 2px 2px 5px red;
        margin-top: 80px;
        font-size: 25px; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    .stDownloadButton > button {
        color: white;
        background-color: #c4302b;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

input_text = st.text_input("")

if input_text:
    try:
        video_buffer, title = download(input_text)
        st.download_button(
            label="Baixar vídeo",
            data=video_buffer,
            file_name=f"{title}.mp4",
            mime="video/mp4"
        )
    except Exception as e:
        st.error(f"Erro ao processar o vídeo: {e}")