# Painters_Classification_Project
📌Project Goal

The objective of this project is to determine whether two given artworks were created by the same artist. This is achieved by building a model capable of comparing visual features in paintings using a Siamese Neural Network.

🗂️Dataset

    The dataset used is from Kaggle’s Painter by Numbers challenge. It contains images of paintings by various artists.
    Training and Validation Sets:
        Total of 17,997 images from 1,208 artists.
        The training set includes 772 artists, and the validation set includes 190 different artists.
        Artists with fewer than two images were excluded.
    Test Set:
      Contains 2,936 images from 91 unique artists, all with at least two artworks.
      

Artists in the training, validation, and test sets were completely disjoint to evaluate the model’s ability to generalize to unseen artists.


For each artist, up to 10 images were selected. If fewer were available, all were included. From these, 30,000 triplets (anchor, positive, negative) were generated per epoch for training, and 6,000 triplets for validation and testing.
This dynamic generation helped prevent overfitting.


Note: The original image sizes were large, so all images were center-cropped to a fixed size of 224x224.

🧪 Preprocessing

    A custom script (creating_csv.py) was used to prepare CSV files.
    Image preprocessing (cropping) was done using a script (pick_and_crop.py) in PyCharm, and saved in .zip format for efficiency.

🧠 Model Architecture – Siamese Network

    The Siamese network leverages a pre-trained ResNet-18 with modifications:
        Removed the last two layers (AvgPool and FC).
        Applied dropout (25%) for regularization.
        Added a fully connected layer: 25,088 → 256.
        Applied another dropout (30%).
        Final output layer: 256 → 64.
Triplet Loss was used to ensure the anchor is closer to the positive than to the negative by at least a defined margin.


🛠️ Hyperparameters

    Optimizer: Adam
    Learning Rate: 1e-5
    Weight Decay: 0.001
    Batch Size: 200
    Triplet Loss Margin: 5

📊 Results

     Test Accuracy: 81.78%
     Overfitting observed after epoch 12
     Model trained on ~30,000 triplets per epoch using 224x224 center-cropped images

Train & Validation Loss


![Train   Validation Loss](https://github.com/user-attachments/assets/ae511c5f-39c5-429f-992d-85ff5b28018d)

Train & Test Accuracy

![Train Accuracy](https://github.com/user-attachments/assets/6d70f3dc-5328-40b0-9924-ec741aa8b274)



![Test Accuracy](https://github.com/user-attachments/assets/e364a7c5-330c-4a7d-a4b3-0811f596faed)


