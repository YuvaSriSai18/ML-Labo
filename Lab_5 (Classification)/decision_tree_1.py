# -*- coding: utf-8 -*-
"""Decision_Tree_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rZyNo2xzIl_JQPeXdI9ArGAxr7r0rEuw

Import libraries
"""

import pandas as pd
import numpy as np

"""Load the dataset"""

dataset = pd.read_csv('play_tennis.csv')
dataset.head()
dataset.shape

"""calculating the entropy"""

def entropy(dataset):
    target_col = dataset.iloc[:, -1]
    target_count = target_col.value_counts()
    entropy_value = 0
    for val in target_count.keys():
        prob = target_count[val] / sum(target_count)
        entropy_value -= prob * np.log2(prob)
    return entropy_value

"""function for calculating information Gain"""

#Creating a function for calculating information Gain
def info_gain(dataset, feature):
    initial_entropy = entropy(dataset)
    feature_values = dataset[feature].unique()
    feature_counts = dataset[feature].value_counts()
    cond_entropy = []

    for val in feature_values:
        subset = dataset[dataset[feature] == val]
        subset_entropy = 0
        for res in dataset.iloc[:, -1].unique():
            try:
                prob_res = subset.iloc[:, -1].value_counts()[res] / len(subset)
                subset_entropy -= prob_res * np.log2(prob_res)
            except:
                subset_entropy = 0
        cond_entropy.append(subset_entropy)

    for i in range(len(feature_values)):
        initial_entropy -= feature_counts[feature_values[i]] * cond_entropy[i] / sum(feature_counts)

    return initial_entropy

class Node():
    def _init_(self, feature_name=None, feature_values=None):
        self.feature_name = feature_name
        self.feature_values = feature_values

    def _str_(self):
        return self.feature_name

def choose_best_feature(dataset, used_features):
    node = Node()
    highest_info_gain = 0
    best_feature = None
    available_features = [feat for feat in dataset.columns[:-1] if feat not in used_features]  # Ensure target column is excluded

    if available_features:
        for feat in available_features:
            gain = info_gain(dataset, feat)
            if gain > highest_info_gain:
                highest_info_gain = gain
                best_feature = feat

        if best_feature:
            used_features.append(best_feature)
            node.feature_name = best_feature
            node.feature_values = dataset[best_feature].unique()
            return node
        else:
            return None

    return None

def build_tree(dataset, used_features):
    root = choose_best_feature(dataset, used_features)
    tree = {}

    # If root is found, continue building the tree
    if root is not None:
        branches = []
        for val in root.feature_values:
            subset = dataset[dataset[root.feature_name] == val]
            if entropy(subset) == 0:  # If pure subset, it's a decision (leaf node)
                branches.append((val, subset.iloc[:, -1].unique()[0]))
            else:
                subtree = build_tree(subset, used_features)
                branches.append((val, subtree))

        tree[root.feature_name] = branches

    return tree

#Function to print the tree
def display_tree(tree, depth=0):
    if isinstance(tree, dict):
        for feature, branches in tree.items():
            print(f"{'|   ' * depth}{feature}")  # Print the feature name
            if isinstance(branches, list):
                for branch in branches:
                    print(f"{'|   ' * (depth + 1)}{branch[0]} ->", end=" ")
                    if isinstance(branch[1], dict):
                        print()
                        display_tree(branch[1], depth + 2)  # Recursive call for further splits
                    else:
                        print(f"Decision: {branch[1]}")  # Print the decision
    else:
        print(tree)

# Build the ID3 decision tree
used_features_list = []
id3_tree = build_tree(dataset, used_features_list)

# Print the ID3 decision tree with features and decisions
print("Final ID3 Decision Tree:")
display_tree(id3_tree)