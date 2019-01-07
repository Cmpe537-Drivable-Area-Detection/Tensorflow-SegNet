#!/bin/bash

# for training
#python main.py --log_dir="/content/drive/My Drive/logs/segnet_logs" --image_dir="nopeTrain.txt" --val_dir="nopeVal.txt" --batch_size=5

# for finetune from saved ckpt
# python main.py --finetune=/tmp3/first350/TensorFlow/Logs/model.ckpt-1000  --log_dir=/tmp3/first350/TensorFlow/Logs/ --image_dir=/tmp3/first350/SegNet-Tutorial/CamVid/train.txt --val_dir=/tmp3/first350/SegNet-Tutorial/CamVid/val.txt --batch_size=5

#for testing
python main.py --testing="/content/drive/My Drive/logs/segnet_logs/model.ckpt-19999"  --log_dir="/content/drive/My Drive/logs/segnet_logs" --test_dir="nopeTest.txt" --batch_size=1 --save_image=True
