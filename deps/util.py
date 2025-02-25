import cv2


def resize(image, width=None, height=None):
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized


def downscale(orig_im, downscaled_height):
    scale = orig_im.shape[0] / downscaled_height
    im = resize(orig_im, height=int(downscaled_height))
    return im, scale
