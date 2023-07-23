import os
import random
import base64
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
import io

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return "No image provided", 400
    
    file = request.files['image']
    original_image = Image.open(file)
    transformed_image = random_color_transform(original_image)

    _, original_image_buf = io.BytesIO(), io.BytesIO()
    original_image.save(original_image_buf, format='PNG')
    _, transformed_image_buf = io.BytesIO(), io.BytesIO()
    transformed_image.save(transformed_image_buf, format='PNG')

    original_image_base64 = base64.b64encode(original_image_buf.getvalue()).decode('utf-8')
    transformed_image_base64 = base64.b64encode(transformed_image_buf.getvalue()).decode('utf-8')

    return jsonify({
        'original_image': original_image_base64,
        'transformed_image': transformed_image_base64,
    })

def random_color_transform(image):
    r_shift, g_shift, b_shift = random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)
    
    def shift(pixel):
        r, g, b = pixel
        r = max(min(r + r_shift, 255), 0)
        g = max(min(g + g_shift, 255), 0)
        b = max(min(b + b_shift, 255), 0)
        return r, g, b

    return Image.new('RGB', (image.width, image.height), (0, 0, 0)).map(shift, image)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
