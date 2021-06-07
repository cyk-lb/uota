from PIL import Image, ImageTk

FOLDER_ICON_PATH = 'icons\\folder_icon_blue.png'
FUNCTION_ICON_PATH = 'icons\\function_icon.png'
CLASS_ICON_PATH = 'icons\\class_icon.png'


def _get_icon(path, width=16, height=16):
    img = Image.open(path)
    img = img.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def get_folder_icon():
    return _get_icon(FOLDER_ICON_PATH, 23, 16)

def get_function_icon():
    return _get_icon(FUNCTION_ICON_PATH)

def get_class_icon():
    return _get_icon(CLASS_ICON_PATH)