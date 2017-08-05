# Rank Face

## Installation

```
pip install numpy scipy csv
pip install tensorflow keras
pip install opencv
git clone https://github.com/Entropy-xcy/RankFace
cd ./RankFace
wget http://entropy-xcy.bid/faceRank.h5
```

## Demo
```
cd ./RankFace
python main.py girls.jpg
```

## Training
Dataset Not uploaded yet.

## Model Summary:
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 128, 128, 32)      896       
_________________________________________________________________
activation_1 (Activation)    (None, 128, 128, 32)      0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 126, 126, 32)      9248      
_________________________________________________________________
activation_2 (Activation)    (None, 126, 126, 32)      0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 63, 63, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 63, 63, 32)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 127008)            0         
_________________________________________________________________
dense_1 (Dense)              (None, 128)               16257152  
_________________________________________________________________
activation_3 (Activation)    (None, 128)               0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 128)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 129       
=================================================================
Total params: 16,267,425
Trainable params: 16,267,425
Non-trainable params: 0
_________________________________________________________________
```
