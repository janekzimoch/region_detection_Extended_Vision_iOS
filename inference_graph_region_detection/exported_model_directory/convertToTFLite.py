import tensorflow as tf 

# This directory 

export_dir = ''

'''
converter = tf.lite.TFLiteConverter.from_saved_model(export_dir, input_shapes={"image_tensor":[1,300,300,3]})
tflite_model = converter.convert() 
open('converted_model.tflite', 'wb').write(tflite_model)
'''
model = tf.keras.applications.MobileNetV2(
    weights="imagenet", input_shape=(224, 224, 3))
tf.saved_model.save(model, export_dir)
model = tf.saved_model.load(export_dir)
concrete_func = model.signatures[tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY]

concrete_func.inputs[0].set_shape([1,224,224,3])

# Convert the model 
converter = tf.lite.TFLiteConverter.from_concrete_function(concrete_func)
tflite_model = converter.convert()

