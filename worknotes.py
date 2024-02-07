import functions_framework
import os

from google.cloud import storage
from google.cloud import speech_v1p1beta1 as speech


@functions_framework.cloud_event
  def transcribe_gcs(cloud_event):
    """Background Cloud Function to be triggered by Cloud Storage when a file is
    changed.
    Args:
        cloud_event (dict):  The event payload.
    """
    # The "data" field contains a description of the event in the Cloud Storage
    # object that triggered the function. At the end of this method you can
    # use it to construct a Google Cloud Storage client object.
    data = cloud_event["data"]

    # Get the file's bucket and name from the Cloud Storage event.
    bucket_name = data["chirp2text"]
    blob_name = data["audio_file"]

    # Construct a Google Cloud Storage client object.
    storage_client = storage.Client()

    # Get the contents of the file from the bucket.
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob_uri = "gs://{bucket_name}/{blob_name}"
    blob_content = blob.download_as_bytes()

    # Construct a Google Cloud Speech client object.
    client = speech.SpeechClient()

    # Configure request to enable multiple channels
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code="en-US",
        audio_channel_count=2,
        enable_separate_recognition_per_channel=True,
    )

    # Perform the transcription request on the remote file.
    audio = speech.RecognitionAudio(uri=blob_uri)
    response = client.recognize(config=config, audio=audio)

    # Print the results.
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print("First alternative of result {}".format(i))
        print("Transcript: {}".format(alternative.transcript))
        print("Channel Tag: {}".format(result.channel_tag))

XXX

from google.api_core.client_options import ClientOptions
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech


def transcribe_chirp(
    project_id: initialkubetest,
    audio_file: audio_file,
) -> cloud_speech.RecognizeResponse:
    """Transcribe an audio file using Chirp."""
    # Instantiates a client
    client = SpeechClient(
        client_options=ClientOptions(
            api_endpoint="us-central1-speech.googleapis.com",
        )
    )

    # Reads a file as bytes
    with open(audio_file, "rb") as f:
        content = f.read()

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        language_codes=["en-US"],
        model="chirp",
    )

    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{project_id}/locations/us-central1/recognizers/_",
        config=config,
        content=content,
    )

    # Transcribes the audio into text
    response = client.recognize(request=request)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

    return response
