# federer-detector
Detect Roger Federer by Tensorflow Object Detection API through Google Cloud

# Detailed Steps
## Data Acquisition
Because Tensorflow Object Detection API already has pre-trained models for transfer learning, instead of thousands of diversified images as training data (or more), I downloaded 200 images (including training and test data) of Roger Federer from Google image search using [Fatkun Batch Download Image](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en). The images are selected with diversity in mind, on scale, pose, lighting, etc.

## PreProcessing
### Resize Images
If images are too large, there is a out-of-memory risk during training. Made a script to resize images up to a max width:

```
python ./train/preprocess/resize_image.py --image_dir=$DIR --max_width=600
```

### Train/Test Split
The 200 images are split into training (160) and test (40).
> NOTE: This needs to be done before labeling the image, because the XML file generated by LabelImg annotates the image file location, so any moving of the image files needs to be done before labeling.

### Label Images
Images are labeled by [LabelImg](https://github.com/tzutalin/labelImg).
> TIP: Select "View -> Auto Saving" and "View -> Single Class Mode".

### Convert to TFRecord format
The PASCAL VOC format generated by LabelImg is converted into TFRecord format:

```
python ./train/preprocess/pascal_voc_to_tf_records.py --output_path=train.record --images_dir=$TRAIN_IMAGE --labels_dir=$TRAIN_LABEL
python ./train/preprocess/pascal_voc_to_tf_records.py --output_path=test.record --images_dir=$TEST_IMAGE --labels_dir=$TEST_LABEL
```

## Training

## Serving
