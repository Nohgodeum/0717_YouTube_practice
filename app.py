import random
import io
import base64
from flask import Flask, request, send_file, render_template_string
import cv2
import numpy as np

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return 'No file uploaded', 400
#         file = request.files['file']
#         image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
#         resized_image = resize_image(image, 350, 450)
#         _, original_image_buf = cv2.imencode('.jpg', resized_image)
#         transformed_image = random_color_transform(resized_image)
#         resized_transformed_image = resize_image(transformed_image, 350, 450)
#         _, transformed_image_buf = cv2.imencode('.jpg', resized_transformed_image)

#         return render_template_string('''
#         <!doctype html>
#         <title>Images Comparison</title>
#         <h1>Images Comparison</h1>
#         <div style="display: flex;">
#           <div style="margin-right: 20px;">
#             <h2>Original Image</h2>
#             <img src="data:image/jpeg;base64,{{ original_image_base64 }}" alt="Original Image">
#           </div>
#           <div>
#             <h2>Transformed Image</h2>
#             <img src="data:image/jpeg;base64,{{ transformed_image_base64 }}" alt="Transformed Image">
#           </div>
#         </div>
#         ''', original_image_base64=base64.b64encode(original_image_buf).decode('utf-8'),
#              transformed_image_base64=base64.b64encode(transformed_image_buf).decode('utf-8'))
#     return '''
#     <!doctype html>
#     <title>Upload Image</title>
#     <h1>Upload Image</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''
@app.route('/')
def index():
    return "Hello, World!"


def random_color_transform(image):
    rows, cols, channels = image.shape
    for channel in range(channels):
        random_shift = random.randint(-100, 100)
        image[:, :, channel] = np.clip(image[:, :, channel] + random_shift, 0, 255)
    return image

def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
