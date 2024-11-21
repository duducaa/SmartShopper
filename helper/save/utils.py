def b64image(path):
    image = open(os.getcwd() + path, 'rb')
    return base64.b64encode(image.read()).decode("utf-8")
