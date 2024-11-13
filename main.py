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
        "content": f"""Please convert the following text into an HTML document:\n\n{text}. 
        Return only the code between <body> and </body> tags (do not innclude <body> tags as well). 
        Try to find appropriate places for images in the text and add <img> tags with atribute `src=\"image_placeholder.jpg\"` in those places. 
        Add attribute `alt` to each image with a prompt instruction which we can later use to generate those graphics. For example: \"IMAGE 1: Generate an image of a voice assistant\".
        Use <br>, <center> and <em> tags for caption of the images (avoid simple statements: "Ilustration of..."). Center the images as well. Scale the images to 512x512.
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