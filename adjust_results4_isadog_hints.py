#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog_hints.py
#                                                                             
# PROGRAMMER: Priyangaa
# DATE CREATED: December 6, 2024
# REVISED DATE: December 6, 2024
# PURPOSE: This function adjusts the results dictionary to indicate whether 
#          or not the pet image label is of-a-dog and to indicate whether 
#          or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. This function checks each label
#          to determine if it matches a known dog name.

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images as 'a dog' or 'not a dog', even when the classifier 
    gets the breed wrong. 

    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a list. 
                    Where the list will contain:
                      index 0 = pet image label (string)
                      index 1 = classifier label (string)
                      index 2 = 1/0 (int) where 1 = match, 0 = no match between labels
                      index 3 = 1/0 (int) where 1 = pet image 'is-a' dog, 0 = 'is-NOT-a' dog
                      index 4 = 1/0 (int) where 1 = classifier image 'is-a' dog, 0 = 'is-NOT-a' dog
      dogfile - A text file containing names of all dogs, one per line. Dog names are lowercase.
      
    Returns:
           None - results_dic is mutable, no return needed.
    """           
    
    # Creates dognames dictionary for quick matching to results_dic labels
    dognames_dic = dict()

    # Reads in dog names from the file and populates dognames_dic
    with open(dogfile, "r") as infile:
        line = infile.readline()
        
        while line != "":
            line = line.strip().lower()  # Remove newline and ensure lowercase
            
            # Add dog name to dictionary if it's not already there
            if line and line not in dognames_dic:
                dognames_dic[line] = 1

            line = infile.readline()

    # Adjust results_dic based on whether labels are dogs or not
    for key in results_dic:
        pet_label = results_dic[key][0].lower()  # Ensure case-insensitive comparison
        classifier_label = results_dic[key][1].lower()

        # Check if pet label is a dog
        if pet_label in dognames_dic:
            # Check if classifier label is a dog
            if classifier_label in dognames_dic:
                results_dic[key].extend((1, 1))  # Both pet and classifier labels are dogs
            else:
                results_dic[key].extend((1, 0))  # Pet is a dog, classifier is not

        # Pet image is not a dog
        else:
            # Check if classifier label is a dog
            if classifier_label in dognames_dic:
                results_dic[key].extend((0, 1))  # Pet is not a dog, classifier is
            else:
                results_dic[key].extend((0, 0))  # Neither pet nor classifier is a dog
