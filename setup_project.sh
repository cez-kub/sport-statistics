#!/bin/bash

#################################
#                               #
# Make it executable:           #
# chmod +x setup_project.sh     #
# ./setup_project.sh            #
#                               #
#         OR                    #
# Run the script directly       #
# without making it executable: #
# bash setup_project.sh         #
#################################

# Create the main project directory
mkdir tennis_prediction

# Navigate into the project directory
cd tennis_prediction

# Create subfolders
mkdir data data/raw data/processed src src/extractors notebooks tests

# Create empty files (replace with actual file extensions as needed)
touch data/raw/.gitkeep
touch data/processed/.gitkeep
touch src/data_acquisition.py
touch src/data_cleaning.py
touch src/data_exploration.py
# Extractors module files
touch src/extractors/atp_extractor.py 
touch src/extractors/wta_extractor.py
touch src/extractors/tennis_abstract_extractor.py
touch src/extractors/jeff_sackmann_extractor.py
touch src/extractors/fivethirtyeight_extractor.py
touch notebooks/data_overview.ipynb
touch notebooks/feature_exploration.ipynb
touch tests/test_data_cleaning.py
touch requirements.txt
touch README.md
touch .gitignore 

# Print a success message
echo "Project directory structure with extractors module created successfully!" 

# Print a success message
echo "README.md files added to extractors module successfully!" 

# Navigate back to the project root
cd ../../.. 