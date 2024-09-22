# 2024-09-22

## Changing from tennis to baseball


# Sources and extractors

## WTA Extractor:

This module is responsible for extracting data from the WTA Tour website (www.wtatennis.com).

**Data to be extracted:**

* Match results: 
    * Date and time of match
    * Tournament name
    * Surface type
    * Player names
    * Match score
    * Match statistics (e.g., aces, double faults, serve percentages)
* Player rankings: 
    * Current and historical singles rankings.
* Player profiles:
    * Basic biographical information (e.g., age, nationality, playing hand).  

## ATP Extractor:

This module is responsible for extracting data from the ATP Tour website (www.atptour.com). 

**Data to be extracted:**

* Match results: 
    * Date and time of match
    * Tournament name
    * Surface type
    * Player names
    * Match score
    * Match statistics (e.g., aces, double faults, serve percentages)
* Player rankings: 
    * Current and historical singles and doubles rankings.
* Player profiles:
    * Basic biographical information (e.g., age, nationality, playing hand).

## FiveThirtyEight Extractor

This module is responsible for extracting data from FiveThirtyEight's tennis Elo ratings (projects.fivethirtyeight.com/tennis-projections/).

**Data to be extracted:**

* Elo ratings: 
    * FiveThirtyEight's Elo ratings with a focus on forecasting.
* Match predictions:
    * Probabilistic predictions for upcoming match outcomes.  

## Jeff Sackmann Extractor

This module is responsible for extracting data from Jeff Sackmann's GitHub repository (github.com/JeffSackmann/tennis_atp).

**Data to be extracted:**

* Detailed match statistics:
    * Serve stats (aces, double faults, first serve %, etc.)
    * Return stats
    * Break points saved/converted
    * Total points won
* Point-by-point data: 
    * For many matches, information on how each point was played. 

## Tennis Abstract Extractor

This module is responsible for extracting data from the Tennis Abstract website (www.tennisabstract.com).

**Data to be extracted:**

* Elo ratings: 
    * Player Elo ratings for both singles and doubles.
* Match charting data: 
    * Detailed shot-by-shot data for selected matches (if available).
