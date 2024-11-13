import requests
from openai import OpenAI

def generate_image(prompt, index):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        n=1,
        size="512x512"
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
        Return only the code between <body> and </body> tags (exlusive). With use of <img> tags with an atribute `src=\"image_placeholder.jpg\"`. 
        Add attribute `alt` to each image with a prompt instruction which we can later use to generate those graphics. For example: \"IMAGE 1: Generate an image of a voice assistant\".
        Try to signify that is the <alt> tag with a prompt and not a part of the text.
        Use <br>, <center> and <em> tags for caption of the images. Center the images as well.
        """
    }
]
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

html_code = completion.choices[0].message.content.replace("```html", "").replace("```", "").strip()

prompts = []
while True:
    prompt = input("Enter a prompt (or press Enter to finish)>> ")
    if not prompt:
        break
    prompts.append(prompt)
for index, prompt in enumerate(prompts):
    image_path = generate_image(prompt, index)
    html_code = html_code.replace(f'src="image_placeholder.jpg"', f'src="{image_path}"', 1)

for index, prompt in enumerate(prompts):
    image_path = generate_image(prompt, index)
    html_code = html_code.replace(f'src="image_placeholder.jpg"', f'src="{image_path}"', 1)

output_html_path = "artykul.html" 
with open(output_html_path, 'w') as html_file:
    html_file.write(html_code)
print(f"{output_html_path} saved.")