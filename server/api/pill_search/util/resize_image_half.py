def resize_image_half(image):
    num = 0.3
    if image.height < 300:
        return image

    if image.height > 1000:
        num = 0.7

    height = int(image.height * num)
    aspect_ratio = float(height) / image.height

    image_resize = image.resize((int(image.width * aspect_ratio), int(height)))
    return image_resize
