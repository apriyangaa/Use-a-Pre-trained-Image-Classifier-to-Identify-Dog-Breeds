#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Priyangaa
# DATE CREATED: 06/12/2024                       
# LAST MODIFIED: 06/12/2024
# PURPOSE: Define a function that retrieves three command-line arguments from
#          the user using the argparse module. If any argument is missing, 
#          default values are used. The command-line arguments are:
#     1. Image Folder path as --dir with a default value of 'pet_images'
#     2. CNN Model Type as --arch with a default value of 'vgg'
#     3. File containing Dog Names as --dogfile with a default value of 'dognames.txt'
#

# Import necessary Python modules
import argparse

# Function to retrieve command-line arguments
def get_input_args():
    """
    Retrieves and parses the 3 command-line arguments provided by the user when
    executing the program from a terminal. This function uses Python's argparse 
    module to define and process the 3 arguments. If any of the arguments are not 
    provided by the user, default values are used instead.
    
    Command-Line Arguments:
      1. Image Folder path as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File containing Dog Names as --dogfile with default value 'dognames.txt'

    Returns:
      parsed arguments as an ArgumentParser object.
    """
    # Initialize the ArgumentParser object
    parser = argparse.ArgumentParser()
    
    # Define the 3 command-line arguments with default values
    parser.add_argument('--dir', type=str, default='pet_images', help='Path to the image folder')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture to use')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='Text file with dog names')

    # Return the parsed arguments as an object
    return parser.parse_args()

