# Melanoma Classification
### Introduction
"Skin cancer is the most prevalent type of cancer. Melanoma, specifically, is responsible for 75%
of skin cancer deaths, despite being the least common skin cancer. The American Cancer Society
estimates over 100,000 new melanoma cases will be diagnosed in 2020. It’s also expected that
almost 7,000 people will die from the disease. As with other cancers, early and accurate detection—potentially aided by data science—can make treatment more effective." -- [Kaggle SIIM-ISIC challange](https://www.kaggle.com/c/siim-isic-melanoma-classification/overview)  

This is a course project in CS324 Deep Learning. The project aims to classify the positive sample from a modified dataset in SIIM-ISIC challenge [[Project Description]](/Instruction_v2.pdf).

### Data Analysis and Preprocessing

##### Overview of data
- 748 JPEG images for training set.
- 186 JPEG images for validation set.
- One target 0 or 1 label, representing benign or malignant.
- Additional infomation for each image: sex, approximate age, anatom site general challenge.

##### Data Analysis
- The data with label 0 is of same size with those with label 1. This data is balanced.
- The images have different size.
- The numbers of image used to train our network is small.
- Data is comparatively clean.

##### Dataset Visualization
*(low figure quality due to the loss of original data)*

<img src="/fig/age.png" width="600"/>

The benign-malignant and its relation to Age and sex.

<img src="/fig/distribution.png" width="600"/>

The distribution of gender, scan part, age.

<img src="/fig/circle.png" width="300"/>

A big picture of sample distribution.

### Final Results

<img src="/fig/training.jpg" width="400"/>

The test acc during training.

<img src="/fig/roc.jpg" width="400"/>

ROC curve for final results.

### Team Member
##### Data preprocessing and training framework: 
Shengran Hu
##### Testing models and optimizing hyper-parameters: 
Jiangning Wu, Yichen Zhu, Xinhao Xiang
