import openai

from terminal.components.system_messages import error_openai
from terminal.components.assistant_output import print_image


def generate_image(prompt):
    """
    Generate an image using OpenAI's image generation API.

    Parameters:
    prompt (str): The prompt for generating the image.

    Returns:
    None
    """
    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url",
        )
    except:
        error_openai()
        return

    print_image(response.data[0].url)
