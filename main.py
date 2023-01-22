import openai

image = input('Descreva a imagem que você quer criar: ')
openai.api_key =  ''
response = openai.Image.create(
    #A text description of the desired image(s). The maximum length is 1000 characters
    prompt = image,
    #The number of images to generate. Must be between 1 and 10
    n = 1,
    #The size of the generated images. Must be one of 256x256, 512x512, or 1024x1024
    size = '1024x1024'
)

img_url = response['data'][0]['url']
print(f'link: {img_url}')