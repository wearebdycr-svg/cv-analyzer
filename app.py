import streamlit as st
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

from ui.streamlit_ui import main

if __name__ == "__main__":
    main()
