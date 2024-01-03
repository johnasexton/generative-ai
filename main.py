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
    blob_uri = f"gs://{bucket_name}/{blob_name}"
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
