import tensorflow as tf
import tensorflowjs as tfjs

try:
    print("Loading model...")
    model = tf.keras.models.load_model('Keras_Hatespeech_model.h5')
    print("Model loaded successfully!")
    tfjs.converters.save_keras_model(model, 'tfjs_model')
    print("Conversion successful! tfjs_model folder created.")
except Exception as e:
    print(f"Error during conversion: {e}")