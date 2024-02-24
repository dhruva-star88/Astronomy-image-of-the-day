import requests


def get_image():
    api_key = "nGkCgrdTCt8hO5IBDjwwi75tXLcznjrUJF8SNlug"
    url = "https://api.nasa.gov/planetary/apod" \
          f"?api_key={api_key}"

    response = requests.get(url)
    data = response.json()
    print(data)
    img_url = data["hdurl"]
    img_content = data["explanation"]

    image_response = requests.get(img_url)
    image_binary_data = image_response.content

    with open("image.jpg", "wb") as image:
        image.write(image_binary_data)

    return img_content


def get_title():
    api_key = "nGkCgrdTCt8hO5IBDjwwi75tXLcznjrUJF8SNlug"
    url = "https://api.nasa.gov/planetary/apod" \
          f"?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    img_title = data["title"]
    return img_title
