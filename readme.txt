ReadMe File

I created this repositoty as part of my Bioinformatics masters at the University of Bristol.
The basic premise set towards us was the creation of a simulation similair to that of 'game of life'.
We would create a simulation of trees. The trees could be in one of three states: alive, on fire, or burnt. Trees could spread fire to those next to them. Lightning could strike a tree and set it on fire, even when it was not next to a burning tree. New trees could grow in the place of dead ones.
The purpose of the project was to reach a steady state between all three conditions.
Please read the tree_report file for more detail, as well as my findings.

This file contains the following items:

animation.py - a python file containing the code needed to animate the tree simulation. Must be taken and run in console

data_analysis_of_trees - a python file containing the code needed to analyse the tree simulation. The first part of the code must be run in console, then the printed data taken and saved into tree_data(see below). Then run the second part of the code.

tree_report - a report on the tree_simulation project.

tree_simulation - The code used to run the tree simulation

tree_lumberjack - the code used to run the the tree simulation, with the added lumberjack rule(before fire and lightning). see tree_report

tree_mercy - the code used to run the tree simulation, with the added mercy rule. see tree_report

tree_data - a dataset used to analyse the tree_simulation.


To run the tree simulation

use code in command line:
python tree_simulation.py

then open animation.py and run that code in python console.

for further information, open tree_report.
