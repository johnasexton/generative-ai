# CODEY CHAT

# imports
import sys
import os
import vertexai
import IPython
import pandas as pd
from IPython.display import display, Markdown
from vertexai.language_models import CodeChatModel
from vertexai.language_models import TextGenerationModel
from vertexai.language_models import ChatModel
# from vertexai.language_models import MultimodalModel

# variables
PROJECT_ID = "initialkubetest"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}
# MODEL_NAME = "gemini-pro-vision"  # @param {type:"string"}
MODEL_NAME = "text-bison@001"  # @param {type:"string"}

# initialize vertex-ai
vertexai.init(project=PROJECT_ID, location=LOCATION)
from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Image,
    Part,
)

# load the specific generative_models
model = TextGenerationModel("gemini-pro")
code_chat_model = CodeChatModel.from_pretrained("codechat-bison@001")
chatmodel = ChatModel("gemini-pro-vision")
# generation_model = TextGenerationModel("gemini-pro-vision")
generation_model = TextGenerationModel.from_pretrained("text-bison@001")
# multimodal_model = MultimodalModel("gemini-pro-vision")

# code below parses but produces no output, still debugging!

# assumes: from vertexai.language_models import CodeChatModel

def write_a_function(temperature: float = 0.5) -> object:
    """Example of using Codey for Code Chat Model to write a function."""

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1024,  # Token limit determines the maximum amount of text output.
    }

    # assumes: code_chat_model = CodeChatModel.from_pretrained("codechat-bison@001")
    chat = code_chat_model.start_chat()

    response = chat.send_message(
        "Please help write a function to calculate the min of two numbers", **parameters
    )
    print(f"Response from Model: {response.text}")

    return response
