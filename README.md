# Korean-Tourist-Spot-Dataset
This repository contains the KTS(Korean Tourist Spot) dataset and code for load them.
You can check the documentation of the KTS dataset at 
[here]( http://ai.dongguk.edu/heterogeneous-dataset/ "Dongguk univ. AI Lab")
The KTS Dataset is consists of data on 10 labels related to tourist spots in Korea collected from the Instagram.
The dataset provides the following data:

* 10,000 images without sensitive information of users
* text like sentence consist of Korean and English
* multiple hashtags
* the number of likes for each image

The dataset divided into total version and split version. 
The total version contains all the data, and also the split version is provided in 7: 1: 2 ratio, divided by train, valid and test.

## Dataset class
The KTS dataset is designed as a two-level hierarchical structure. 
First, they divided into person-made tourist spots and nature scene tourist spots as coarse components of the upper level concept and each coarse label has 5 fine labels.

* Person-made
  * Amusement Park
  * Palace
  * Park
  * Tower
  * Restaurant
+ Nature-scene
  * Beach
  * Cave
  * Island
  * Lake
  * Mountain

## Load code
Pure Python:
 > [load_data.py](https://github.com/DGU-AI-LAB/Korean-Tourist-Spot-Dataset/blob/master/load_data.py)

Jupyter notebook:
 > [load_data.ipynb](https://github.com/DGU-AI-LAB/Korean-Tourist-Spot-Dataset/blob/master/load_data.ipynb)

## Copyrights
Copyright 2019, AI lab., Dongguk Univ. All rights reserved
