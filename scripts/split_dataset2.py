import os
import shutil
import random

def split_dataset(source_dir, train_dir, test_dir, split_ratio=0.8):
    for emotion in os.listdir(source_dir):
        emotion_path = os.path.join(source_dir, emotion)
        if not os.path.isdir(emotion_path):
            continue
        images = os.listdir(emotion_path)
        random.shuffle(images)
        split_point = int(len(images) * split_ratio)
        train_images = images[:split_point]
        test_images = images[split_point:]
        
        # Create directories for train and test splits
        os.makedirs(os.path.join(train_dir, emotion), exist_ok=True)
        os.makedirs(os.path.join(test_dir, emotion), exist_ok=True)
        
        # Copy images to the respective directories
        for img in train_images:
            src = os.path.join(emotion_path, img)
            dst = os.path.join(train_dir, emotion, img)
            shutil.copyfile(src, dst)
        for img in test_images:
            src = os.path.join(emotion_path, img)
            dst = os.path.join(test_dir, emotion, img)
            shutil.copyfile(src, dst)

# Define paths
source_dataset2_dir = 'Data/raw/2/'
train_dataset2_dir = 'Data/processed/dataset2/train/'
test_dataset2_dir = 'Data/processed/dataset2/test/'

# Split Dataset 2
split_dataset(source_dataset2_dir, train_dataset2_dir, test_dataset2_dir)
