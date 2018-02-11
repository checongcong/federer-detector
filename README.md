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

### Label Images

### Train/Test Split

### Convert to TFRecord format

## Training

## Serving
