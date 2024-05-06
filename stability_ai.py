import io
import os
import warnings
import random

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from dotenv import load_dotenv

load_dotenv()
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

seed = random.randint(0, 1000000000)

# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.getenv("STABILITY_KEY"),
    verbose=True, # Print debug messages.
    engine="stable-diffusion-xl-1024-v1-0", # Set the engine to use for generation.
    # Check out the following link for a list of available engines: https://platform.stability.ai/docs/features/api-parameters#engine
)

def text_to_image(prompt):
    # Set up our initial generation parameters.
    answers = stability_api.generate(
        prompt=prompt,
        seed=seed,
        steps=30,
        cfg_scale=8.0,

        width=1024,
        height=1024,
        sampler=generation.SAMPLER_K_DPMPP_2M )

    # Set up our warning to print to the console if the adult content classifier is tripped.
    # If adult content classifier is not tripped, display generated image.
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                global img
                img = Image.open(io.BytesIO(artifact.binary))
                return img 

def edit_image(input_image_path, prompt, output_image_name):
    img = Image.open(input_image_path)

    # Set up our initial generation parameters.
    answers = stability_api.generate(
        prompt=prompt,
        init_image=img,
        start_schedule=0.6,
        seed=123463446,
        steps=50,
        cfg_scale=8.0,
        width=512,
        height=512,
        sampler=generation.SAMPLER_K_DPMPP_2M
    )

    # Set up our warning to print to the console if the adult content classifier is tripped.
    # If adult content classifier is not tripped, save generated image.
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                global img2
                img2 = Image.open(io.BytesIO(artifact.binary))
                img2.save(output_image_name + ".png") # Save our generated image with its seed number as the filename and the img2img suffix so that we know this is our transformed image.
