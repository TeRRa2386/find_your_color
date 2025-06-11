from flask import Flask, render_template, redirect, url_for, flash, request
from PIL import Image
from dotenv import load_dotenv
import collections
import uuid
import os


load_dotenv()

app = Flask(__name__)
app.jinja_env.cache = {}


UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def simplify_color(rgb, factor=16):
    return tuple((v // factor) * factor for v in rgb)


def top_colors_hex(image_):

    img = Image.open(image_)
    img = img.convert('RGB')
    pixeles = list(img.getdata())
    simplified_pixels = [simplify_color(rgb) for rgb in pixeles]
    counter = collections.Counter(simplified_pixels)
    colors = counter.most_common(10)

    # total_pixeles = len(simplified_pixels)
    rgbs = [rgb for rgb, count in colors]
    hex_codes = [rgb_to_hex(rgb) for rgb in rgbs]
    # percentages = [f'{round(count/total_pixeles*100, 1)}%' for rgb, count in colors]

    return hex_codes


@app.route('/', methods=['GET', 'POST'])
def index():


    if request.method == 'POST':


        if 'image' not in request.files:
            return 'No file part'

        file = request.files['image']

        if file.filename == '':
            return 'No selected file'

        if file:
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            image_url = url_for('static', filename=f'uploads/{filename}')

            hex_codes= top_colors_hex(filepath)
            print(hex_codes)

            return render_template('index.html', image_url=image_url, hex_codes=hex_codes)

    return render_template('index.html')

#
# if __name__ == '__main__':
#     app.run(debug=True)