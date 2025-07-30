import os
import gradio as gr
from webui import create_app  # Adjust import based on webui.py structure
from fastapi import FastAPI
from gradio.fastapi_app import mount_gradio_app

# Initialize FastAPI app
fastapi_app = FastAPI()

# Initialize Gradio app
gradio_app = create_app()  # Assumes webui.py has a create_app() function

# Mount Gradio app on FastAPI
app = mount_gradio_app(fastapi_app, gradio_app, path="/")

# Vercel serverless function handler
def handler(request):
    return app(request)