# ONE SHOT PROMPT

# imports
import vertexai
from vertexai.language_models import TextGenerationModel


def interview(
        temperature: 0.2,
        project_id: "initialkubetest",
        location: "us-central1",
) -> str:
    """Ideation example with a Large Language Model"""

    vertexai.init(project=project_id, location=location)
    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": 0.2,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        "Give me ten interview questions for the role of SRE.",
        **parameters,
    )
    print(f"Response from Model: {response.text}")

    return response.text


if __name__ == "__main__":
    interview(0.2, 'initialkubetest', 'us-central1')