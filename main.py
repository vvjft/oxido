import requests
from openai import OpenAI

def generate_image(prompt, index):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    
    img_response = requests.get(image_url)
    image_path = f"image_{index}.jpg"
    with open(image_path, 'wb') as img_file:
        img_file.write(img_response.content)
    return image_path

client = OpenAI()
with open("Zadanie dla JJunior AI Developera - tresc artykulu.txt", "r", encoding="utf-8") as file:
    text = file.read()

messages=[
    {"role": "system", "content": "You are an assistant that can convert text into HTML documents."},
    {
        "role": "user", 
        "content": f"""
        Please convert the the attached text into an HTML document with the following requirements:
        Detect headers for longer parts of the text (which can have more than one pargraph). Split fragments of the text into <section> tags with a `class=hidden`. 
        Mind the footnotes and add them at the end of the article.

        Within each section wrap text into <div> with a class <text-content> and <image-content> for images. Wrap both text and images into <div> with a class <content-wrapper>.
        Add <img> tags with atribute `src=\"image_placeholder.jpg\"` in those places. 
        Add attribute `alt` to each image with a prompt instruction which we can later use to generate those graphics. For example: \"IMAGE 1: Generate an image of a voice assistant\".
        Use <br>, and <em> tags for caption of the images (avoid simple statements: "Ilustration of..."). Scale the images to 512x512.

        Return only the code between <body> and </body> tags (do not include <body> tags as well). 

        Create one image per section.

        Do not use any CSS or JavaScript in the document.

        The attached text is the following: \n\n{text}
        """
    }
]
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

html_code = completion.choices[0].message.content.replace("```html", "").replace("```", "").strip()
output_html_path = "artykul.html"
with open(output_html_path, 'w') as html_file:
    html_file.write(html_code)
print(f"Initial {output_html_path} saved with placeholders.")

prompts = []
while True:
    prompt = input("Enter a prompt (or press Enter to finish) >>> ")
    if not prompt:
        break
    prompts.append(prompt)
for index, prompt in enumerate(prompts):
    image_path = generate_image(prompt, index)
    html_code = html_code.replace(f'src="image_placeholder.jpg"', f'src="{image_path}"', 1)

with open(output_html_path, 'w') as html_file:
    html_file.write(html_code)
print(f"{output_html_path} saved.")