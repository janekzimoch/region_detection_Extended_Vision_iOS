# region_detection_Extended_Vision_iOS
.pb model to be converted into .tflite model

There are several approaches i tried, none of which was fully succesful (at some point i had either problem with some errors, or software compatability...)

1) https://medium.com/tensorflow/training-and-serving-a-realtime-mobile-object-detector-in-30-minutes-with-cloud-tpus-b78971cf1193
* i managed to convert a model into a "tflite_graph.pb" which you can find in "exported_model_directory/" folder in this repo
* i think the problem here was with setting up bazel
I couldn't get this part of code to run 

```
bazel run -c opt tensorflow/lite/toco:toco -- \
--input_file=C:/tensorflow1/models/research/object_detection/inference_graph_region_detection/exported_model_directory/tflite_graph.pb \
--output_file=C:/tensorflow1/models/research/object_detection/inference_graph_region_detection/exported_model_directory/detect.tflite \
--input_shapes=1,300,300,3 \
--input_arrays=normalized_input_image_tensor \
--output_arrays='TFLite_Detection_PostProcess','TFLite_Detection_PostProcess:1','TFLite_Detection_PostProcess:2','TFLite_Detection_PostProcess:3'  \
--inference_type=QUANTIZED_UINT8 \
--mean_values=128 \
--std_values=128 \
--change_concat_input_ranges=false \
--allow_custom_ops
```

2) https://www.tensorflow.org/lite/convert/python_api
* i tried several approaches from here - using tensorflow 1.2. -> tf.contrib.lite.TocoConverter
* then i decided to update to "TensorFlow nightly release" and convert - but also unsuccesfully

ISSUE RESOLVED: 

To generate .tflite file:

export OUTPUT_DIR='path/to/tflite_graph.pb' \\
cd tensorflow \\
make convert 

This will save detect.tflite file in OUTPUT_DIR. Also, this assumes that tflite_graph.pb is stored in OUTPUT_DIR.