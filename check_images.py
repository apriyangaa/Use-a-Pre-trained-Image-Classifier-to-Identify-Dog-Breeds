#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
# 
# PROGRAMMER: Priyangaa
# DATE CREATED: December 6, 2024
# REVISED DATE: December 6, 2024
# PURPOSE: This function calculates statistics based on the classification results 
#          and stores the statistics in a dictionary, `results_stats_dic`, 
#          for further analysis and comparison of model performance.

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using the classifier's 
    model architecture to classify pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) for further analysis.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index) idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    
    Returns:
     results_stats_dic - Dictionary containing results statistics (counts & percentages):
             n_images - total number of images
             n_dogs_img - number of dog images
             n_notdogs_img - number of NON-dog images
             n_match - number of matches between pet & classifier labels
             n_correct_dogs - number of correctly classified dog images
             n_correct_notdogs - number of correctly classified NON-dog images
             n_correct_breed - number of correctly classified dog breeds
             pct_match - percentage of correct matches
             pct_correct_dogs - percentage of correctly classified dogs
             pct_correct_breed - percentage of correctly classified dog breeds
             pct_correct_notdogs - percentage of correctly classified NON-dogs
    """
    # Initialize results stats dictionary
    results_stats_dic = {
        'n_images': 0,
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0,
        'pct_match': 0.0,
        'pct_correct_dogs': 0.0,
        'pct_correct_breed': 0.0,
        'pct_correct_notdogs': 0.0,
    }

    # Debugging: Validate input
    print("DEBUG: Checking input results_dic structure:")
    for key, value in results_dic.items():
        print(f"{key}: {value}")

    # Process results_dic to calculate statistics
    for key, value in results_dic.items():
        results_stats_dic['n_images'] += 1
        
        # Check for match
        if value[2] == 1:
            results_stats_dic['n_match'] += 1

        # Check if pet image is a dog
        if value[3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            # Check if the classifier correctly identified it as a dog
            if value[4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
            # Check if the breed is correctly identified
            if value[2] == 1:
                results_stats_dic['n_correct_breed'] += 1
        else:
            # Image is NOT a dog
            if value[4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculate number of non-dog images
    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']

    # Calculate percentages
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0

    # Debugging: Display calculated statistics
    print("DEBUG: Final results statistics:")
    for stat, value in results_stats_dic.items():
        print(f"{stat}: {value}")

    return results_stats_dic
