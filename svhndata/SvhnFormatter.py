"""
Functions to format the SVHN data.
Contains:
    - Function to change dimensions for different frameworks requirements.
    - Function to change the amount of data used.
    - Function to one hot encode the labels.
"""
import numpy as np


def change_dim(x_data, framework="tensorflow"):

    # change image dimension to specified framework
    if framework == "pytorch":
        # [h, w, channel, num_images] --> [num_images,channel, h, w]
        x_new_data = x_data.transpose(3, 2, 0, 1)
    elif framework == "tensorflow" or framework == "keras":
        # [h, w, channel, num_images] --> [num_images, h, w, channel]
        x_new_data = x_data.transpose(3, 0, 1, 2)
    else:
        print("change_dim only takes pytorch, keras, or tensorflow")

    print('Image dimensions ready for ' + str(framework) + ': ' + str(x_new_data.shape))
    print('--' * 25)
    return x_new_data


def change_range(range_num, x_array, y_array):
    try:
        x_array_new = x_array[:range_num, ]
        y_array_new = y_array[:range_num, ]
        if range_num > len(x_array):
            print('Input range is larger than amount of data available\n')
        else:
            print('\nData range has been changed. New shape below')
            print('--' * 20)
            print("New shape for images " + str(x_array_new.shape))
            print('--' * 20)
            print("New shape for labels " + str(y_array_new.shape))
            print('**'*20)
        return x_array_new, y_array_new
    except ValueError:
        print('Please check Image Dimensions! Something is wrong there')


def onehot_encoder(y):
    y = y.flatten()
    y = (np.arange(10) == y[:, np.newaxis]).astype(np.float32)
    return y


def svhn_max_min(x):
    x = x/255
    return x


if __name__=='__main__':
    change_dim()
    change_range()
    onehot_encoder()
    svhn_max_min()
