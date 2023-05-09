import tensorflow as tf
import numpy as np
import io

def get_model():
    model_path = './models/my_model'
    model = tf.keras.models.load_model(model_path, compile=False)
    return model

def make_prediction(model, file_obj):
    img = tf.keras.utils.load_img(io.BytesIO(file_obj), target_size=(224, 224))
    img = tf.keras.utils.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.vgg16.preprocess_input(img)
    predictions = model.predict(img)
    labels = tf.keras.applications.vgg16.decode_predictions(predictions)
    class_name = labels[0][0][1]
    class_score = labels[0][0][2]
    return (str(class_name), str(class_score))