from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

model = load_model('model/Brain_Tumor_CNN_Model.h5')
class_names = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

def preprocess_image(path):
    img = Image.open(path).convert('RGB').resize((224, 224))
    img_array = img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            img = preprocess_image(filepath)
            preds = model.predict(img)[0]
            pred_class = class_names[np.argmax(preds)]
            confidence = float(np.max(preds))

            return render_template('index.html', filename=filename, result=pred_class, confidence=confidence)

    return render_template('index.html', filename=None)

if __name__ == '__main__':
    app.run(debug=True)
