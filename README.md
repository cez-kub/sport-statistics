# Tennis Match Prediction Project  

## AI ethics manifesto:

All logic and code in this repository is human mind sourced, and written by author.  

Author of this repository supports the **controlled development** and **deployment** of AI in a way that benefits society, aligns with human values, and avoids monopolistic control by corporations.  

To limit AI models' access to online content for the purposes of **data integrity, privacy**, and to **prevent exploitative AI deployments**, All readmes, code comments and texts were rephrased using ```OPEN AI Chat GPT 4o```, with the prompt:

```
Hey I am working on portfolio project showcasing my senior level skills in data engineering, analytics engineering, data architecture and business analyst skills. I have text:

„…Text…”


Rewrite it, so it is seen as a work of generative AI model.
```

PLEASE SUPPORT effort to:  

- **Protect human creativity** by ensuring that AI isn't freely exploiting human-created content for profit without proper compensation or control.  
- Promote **transparent and fair use** of AI, preventing its misuse by corporations solely for profit.  
- Encourage **sustainable AI practices**, where AI models are developed with respect to human rights, data privacy, and intellectual property.
- Advocate for **responsible data sourcing** or **AI governance**.  
 
## <span style="color:red">Legal and Ethical Disclaimer:</span>

This project is created for **educational purposes only** and serves as a demonstration of data analytics and machine learning techniques. The analysis presented in this project is focused on **sports data** and is intended solely for the purpose of enhancing technical skills in **data acquisition**, **exploration**, and **predictive modeling**.

**No part of this project** is designed, intended, or endorsed for use in sports betting or any form of gambling. The creators of this project acknowledge that sports betting may be subject to legal restrictions and ethical concerns in various jurisdictions. It is the responsibility of the user to ensure that they comply with all applicable **laws** and **regulations** in their region.

The data and techniques utilized in this project should not be interpreted as promoting or supporting gambling in any form. The **primary objective** of this project is to develop a portfolio of technical skills in data science and to explore **statistical modeling** in the context of sports performance.

By interacting with this project, users acknowledge that they are doing so for **educational purposes** only, and the creators of this project take no responsibility for any misuse of the data or methods demonstrated herein.

## Project Goal:
This project aims to build a machine learning model to predict the outcome of professional tennis matches using historical data and player statistics.

## Project Phases:  

**Phase 1: Data Acquisition and Exploration**

* **Data Sources:**
    * ATP & WTA Official Websites: Match results, player rankings, basic player information.
    * Tennis Abstract: Elo ratings, potentially match charting data.
    * Jeff Sackmann's GitHub: Detailed match statistics, point-by-point data.
    * FiveThirtyEight: Tennis Elo ratings.
* **Data Acquisition:**
    * Develop scripts to download or scrape data from each source (see `src/extractors`).
    * Store raw data in `data/raw`.
* **Data Cleaning and Preprocessing:**
    * Clean and standardize data formats.
    * Handle missing values.
    * Merge data from different sources.
    * Store processed data in `data/processed`.
* **Exploratory Data Analysis (EDA):**
    * Analyze data distributions and relationships.
    * Visualize data to identify patterns and insights.


<!--
**Phase 2: Feature Engineering and Model Building (Future)**

* **Feature Engineering:** 
    * Create new features from existing data to improve model performance (e.g., past performance metrics, surface-specific stats).
* **Model Selection:**
    * Choose appropriate machine learning models for prediction (e.g., Logistic Regression, Random Forest).
* **Model Training and Evaluation:**
    * Train and evaluate models using suitable metrics.

**Phase 3: Real-Life Prediction and Monitoring (Future)**

* **Integrate Real-Time Data:** 
    * Explore Open Tennis Data API and Flashscore for live scores and odds.
* **Generate Real-Life Predictions:**
    * Use the trained model to predict upcoming match outcomes.
* **Track and Monitor Performance:**
    * Continuously evaluate prediction accuracy and refine the model. 
-->
## Project Structure:  

`tennis_prediction/`  
├── `data/` # Raw and processed data  
├   ├── `raw/` # Downloaded raw data from sources  
├   └── `processed/` # Cleaned and merged data  
├── `src/` # Source code for data acquisition, cleaning, EDA  
├   ├── `extractors/` # Scripts to extract data from each source  
├   ├── `data_acquisition.py`  
├   ├── `data_cleaning.py`  
├   ├── `data_exploration.py`  
├   └── ...  
├── `notebooks/` # Jupyter notebooks for exploration and analysis  
├── `tests/` # Unit tests for your code  
├── `docs/` # Project journals with decisions rationals  
├── `requirements.txt` # List of project dependencies  
├── `README.md` # Project description and instructions  
├── `setup_project.sh` # Project structure setup  and rationales for data extracted from those sources  
└── `.gitignore` # Files and folders to ignore  

## Getting Started:  

1. Clone the repository.
2. Create a conda environment (see instructions below).
3. Install dependencies: `pip install -r requirements.txt`
4. Run the data acquisition scripts in `src/extractors`. 
5. Explore the data using the Jupyter notebooks in `notebooks`.

**Creating a Conda Environment:**

```bash
conda create -n tennis_env python=3.11 
conda activate tennis_env