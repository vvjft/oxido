# HTML document genrator with OpenAI API

This project converts a text document into an HTML document with specific formatting and generates images based on user prompts using OpenAI's DALL-E model.

## Requirements

- Python 3.x
- `requests` library
- `openai` library

## Code overview

**main.py:**

Initial HTML file is created with suggested prompts for image generation. User can enter prompts which are sent to the dall-e-3 model to generate images. The default attributes of the images are then replaced with the generated ones. The raw artykul.html can be viewed in the browser or copied into podglad.html.

**style.css:**

 Contains styles for the HTML document, including general styles for body, headings, and paragraphs. It also includes specific styles for .content-wrapper, .text-content, and .image-content classes to ensure proper formatting and alignment of text and images. Sections with the .hidden class are initially hidden.

**script.js:**

Adds interactivity to the HTML document. It includes a function to toggle the visibility of sections with the .hidden class and event listeners for interactive elements to trigger this function. It also handles dynamic image loading if needed.


## Setup

1. Install the required libraries:
    ```sh
    pip install requests openai
    ```
2. Ensure you have the OpenAI API key set up in your environment.

## Usage

1. Place the text file into a working directory.

2. Follow the prompts to to generate images in the article.

3. The generated HTML will be saved to `artykul.html`.

## Example

1. Run the script:
    ```sh
    python main.py
    ```

2. Enter prompts when asked (you can use suggestions attached in html file:
    ```
    Enter a prompt (or press Enter to finish) >>> Generate an image representing AI technlogy
    Enter a prompt (or press Enter to finish) >>> Generate an image illustrating ethical challenges in AI
    Enter a prompt (or press Enter to finish) >>> Generate an image depicting the future of work and automation
    ```

3. The `artykul.html` file will be generated with the specified formatting and images.

4. Additionally, you can paste the content of the created html file into `podglad.html` in order to display the article in predefined template.
    
https://github.com/user-attachments/assets/ce146a55-11cd-4ede-9c15-14ddda51d82e

