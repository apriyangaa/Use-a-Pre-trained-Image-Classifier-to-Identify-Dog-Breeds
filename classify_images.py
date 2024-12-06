#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Priyangaa
# DATE CREATED: 06/12/2024                                 
# LAST MODIFIED: 06/12/2024
# PURPOSE: Define the function get_pet_labels that extracts pet labels from 
#          image filenames. This function processes the filenames in a given 
#          image folder to create and return a dictionary containing pet labels 
#          for each image. The dictionary maps the image filename to a list 
#          where the first item is the pet label (string).
# 
#          The function accepts the image directory as input, processes each 
#          image file, and generates a pet label by extracting and formatting 
#          the breed name from the filename. If duplicate files are found, 
#          a warning message is displayed.
#

# Import necessary Python modules
from os import listdir

# Function to create pet labels from image filenames
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based on the image filenames in a 
    specified directory. The filenames of the images are assumed to contain 
    the true identity of the pet. The labels are formatted to be in lowercase 
    and have leading/trailing whitespace removed.
    
    Parameters:
     image_dir - The path to the folder containing the images (string)
     
    Returns:
      results_dic - A dictionary where:
                    'key' is the image filename,
                    'value' is a list with the pet label at index 0
    """
    # Get the list of files in the specified directory
    in_files = listdir(image_dir)
    results_dic = dict()

    for idx in range(0, len(in_files), 1):
       
       # Skip files that start with a dot (e.g., system files)
       if in_files[idx][0] != ".":

           # Process the filename to extract the pet breed name
           low_pet_image = in_files[idx].lower()
           word_list_pet_image = low_pet_image.split("_")
           pet_name = ""
           for word in word_list_pet_image:
               if word.isalpha():
                   pet_name += word + " "
           pet_name = pet_name.strip()
           
           # Store the pet label in the dictionary, ensuring no duplicates
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_name]
           else:
               print("** Warning: Duplicate file found:", in_files[idx])

    # Return the results dictionary
    return results_dic
