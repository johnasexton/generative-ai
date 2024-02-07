# imports
import sys
import os
import vertexai
import IPython
import pandas as pd
from IPython.display import display, Markdown
from vertexai.language_models import CodeChatModel

# project specific variables
PROJECT_ID = "[initialkubetest]"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}
MODEL_NAME = "text-bison@001"  # @param {type:"string"}

# initialize vertex-ai
vertexai.init(project=PROJECT_ID, location=LOCATION)
from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Image,
    Part,
)

# import vertexai text generation model
from vertexai.language_models import TextGenerationModel
from vertexai.language_models import ChatModel
# from vertex.ai.language_models import MultimodalModel

# load the generative_models
chatmodel = ChatModel("gemini-pro-vision")
generation_model = TextGenerationModel("gemini-pro-vision")
# multimodal_model = MultimodalModel("gemini-pro-vision")
# model = TextGenerationModel("gemini-pro")
# generation_model = TextGenerationModel.from_pretrained("text-bison@001")

# the non-working part is below this comment, everything above has been debugged

from vertexai.language_models import CodeChatModel


def write_a_function(temperature: float = 0.5) -> object:
    """Example of using Codey for Code Chat Model to write a function."""

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1024,  # Token limit determines the maximum amount of text output.
    }

    code_chat_model = CodeChatModel.from_pretrained("codechat-bison@001")
    chat = code_chat_model.start_chat()

    response = chat.send_message(
        "Please help write a function to calculate the min of two numbers", **parameters
    )
    print(f"Response from Model: {response.text}")

    return response


if __name__ == "__main__":
    write_a_function()

# from langchain import PromptTemplate
# from langchain.chains.question_answering import load_qa_chain
# from langchain.document_loaders import PyPDFLoader
# from langchain.embeddings import VertexAIEmbeddings
# from langchain.llms import VertexAI
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import Chroma

prompt = "Give me ten interview questions for the role of prompt engineer."

print(
    generation_model.predict (
        prompt=prompt, temperature=0.2, top_k=0, top_p=0.9
    ).text
)
