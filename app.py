from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import img_to_array

# Load the cancer prediction model
model = tf.keras.models.load_model('model.h5')

app = Flask(__name__)

# Home page route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('home.html', message='No file selected')
        
        file = request.files['file']
        
        # Check if the file is an image
        if file.filename == '':
            return render_template('home.html', message='No file selected')
        if file:
            # Save the file to a temporary folder
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Open and preprocess the image
            # img = Image.open(file_path)
            img = tf.keras.utils.load_img(file_path, target_size = (150,150))
            image_array = img_to_array(img)
            image_array = tf.expand_dims(image_array, axis = 0)
            # Use the model to predict
            prediction = model.predict(image_array)
            
            # Determine the class label
            if prediction == 0:
                class_label = 'Positive'
            else:
                class_label = 'Negative'
            
            # Display the result
            return render_template('result.html', class_label=class_label, file_path=file_path)
        
        else:
            return render_template('home.html', message='Invalid file type')
    
    else:
        return render_template('home.html')

# Result page route
@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = '.'
    app.run(debug=True)
