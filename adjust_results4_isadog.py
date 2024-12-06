#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Priyangaa
# DATE CREATED: 06/12/2024                                 
# LAST MODIFIED: 06/12/2024
# PURPOSE: Define a function adjust_results4_isadog to update the results 
#          dictionary to indicate whether the pet image label or classifier label 
#          is of-a-dog, based on dog names from a given dognames.txt file. 
#          The function checks both the pet image and classifier labels to determine 
#          whether they refer to a dog and adds corresponding values to the results dictionary.
#

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if the pet image label or 
    classifier label corresponds to a dog. It updates the results dictionary 
    by appending values indicating whether the pet image and classifier label 
    are of a dog (1 for dog, 0 for not a dog).

    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List containing the following:
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int) indicating match between pet and classifier labels
                ----- index 3 & 4 are added by this function -----
                 NEW - index 3 = 1/0 (int) where 1 = pet image is a dog, 0 = not a dog
                 NEW - index 4 = 1/0 (int) where 1 = classifier label is a dog, 0 = not a dog
      dogfile - Text file containing dog names, with one dog name per line, in lowercase.
                The dog names are used to check if the pet or classifier labels refer to a dog.

    Returns:
      None - The function modifies the results_dic dictionary in place.
    """
    # Create a dictionary of dog names
    dognames_dic = dict()
    
    with open(dogfile, "r") as infile:
        # Read dog names from the file
        for line in infile:
            line = line.rstrip()
            dognames_dic[line] = 1  # Store dog names with a value of 1

    # Check if results_dic labels correspond to dogs
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        # Check if pet label is a dog
        pet_is_dog = 1 if pet_label in dognames_dic else 0

        # Check if classifier label is a dog
        classifier_is_dog = 1 if classifier_label in dognames_dic else 0

        # Add dog information to results_dic
        results_dic[key].extend([pet_is_dog, classifier_is_dog])
    
    # No need to return anything as results_dic is modified in place
    return None
