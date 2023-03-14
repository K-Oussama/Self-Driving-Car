# Self-Driving-Car
project that simulates an autonomous car driving in the popular video game Grand Theft Auto (GTA) using neural networks.
## Description
The "Self-Driving Car" repository is a project that simulates an autonomous car driving in the popular video game Grand Theft Auto (GTA) using neural networks. The purpose of this project is to demonstrate the capabilities of machine learning in the field of autonomous driving.

The repository includes code for training a deep neural network using a dataset of labeled images of the game environment. The trained model is then used to control the car in the game, making decisions based on its perception of the environment.

The code includes various modules for image processing, feature extraction, and decision-making. The image processing module preprocesses the raw game images, converting them into a format that is suitable for input into the neural network. The feature extraction module uses the neural network to extract relevant features from the processed images. The decision-making module uses the extracted features to make decisions about the car's speed, steering, and braking.

The repository also includes a set of sample images and trained model weights, allowing users to quickly get started with the project. Additionally, the code includes extensive documentation and comments to help users understand the various modules and how they work together.

Overall, the "Self-Driving Car" repository provides an exciting and accessible demonstration of the potential of neural networks in the field of autonomous driving.

## Requirements

Before running the project, you will need to download and install the following:

- Grand Theft Auto: San Andreas from this [link](https://www.downloadcomputergames.net/p/download.html#https://up.downloadcomputergames.net/2020/09/download-gta-san-andreas/GTA-San-Andreas.zip)
- Multi Theft Auto (MTA) from the official website
- Python 3.x and pip

## Setup

To set up the project, follow these steps:

1. Create a Python environment and activate it (optional).
2. Install the required packages by running the following command:

```
pip install -r requirements.txt
```


## Usage

To use the project, follow these steps:

1. Open the game with MTA and set the dimension to 800x400. Position the window to the left and host a game locally to start a new empty world to test it.
2. Record key inputs by running the following command in the terminal:

```
python KeyRecord.py
```

Drive the car for 2-3 minutes.

3. Train the model by running either of the following commands:

```
python train.py
```
Or :
```
jupyter notebook train.ipynb
```


4. After the model is trained, open MTA game, set the player in a vehicle, and then run the following command in the terminal:

```
python drive.py
```

5. Enjoy the self-driving car experience!

## Credits

This is a school project realized by :

**Oussama KORCHI** and **Adil Ghazi**,

Supervised by **Mme Ibtissam TOUAHRI**.


## License

This project is licensed under the MIT License - see the LICENSE file for details.