# CSE6242
This is a project about restaurants in Atlanta.

## Restaurant type clustering Readme:
### input data: 
* business_data.json: the keys are restaurant ids. The data is from Yelp API.
* retaurant_type.csv: matching original restaurant types to a higher level category, which is defined manually.
* reviews_of_100_restaurants.csv: scratched from Yelp, covering 71432 reviews and 97 restaurants.
### code: 
6242 group project_Jinyu.ipynb
### output data:
* restaurant_atl.json: a new key-value pair is added to each individual restaurant in business_data.json, which indicates the type of the restaurant. The types are based on the self defined categories. There are 24 restaurant types in total.
* restaurant_reviews.csv: a merged dataframe from reviews_of_100_restaurants.csv and restaurant_atl.json, which includes features of reviews and features of restaurants.

## Random forest Readme:
### Part 1: filter out reviews generated on fake dates
### input data: 
* fakedate.csv: presenting suspicious dates with high volume of reviews generated
* reviews_of_100_restaurants.csv: mentioned above.
* code: 
randomForestData.py 
### output data:
* data.csv: include the reviews generated in suspicious days, which is the whole dataset for carrying out random forest analysis.
### Part 2: predict fair ratings
### input data:
* data.csv: generated and described in part 1
* code: 
RandomForest_Jinyu.ipynb
### output data:
* restaurant_ratings.csv: 95 entries in total with 5 columns. ‘biz_id’ shows the unique identification codes of restaurants. ‘all’ shows the original ratings calculated based on data.csv. ‘elite’ shows the ratings calculated based on the data.csv, where the ‘elite’ variable is valued 1. ‘elite_hat’ shows the ratings calculated based on the data.csv, where predicted elite value is 1, the column of which is named ‘elite_hat’. ‘diff’ is calculated by the ‘all’-’elite_hat’.

## Feature Reduction Readme:
### Part 1: User rating feature regressor
### input data: 
* reviews_of_100_restaurants.csv: scratched from Yelp, covering 71432 reviews and 97 restaurants.
### code: 
* review_clean.py
* fakeDay.py 
* user_rating_regression.py
### output data:
* fakedate.csv: presenting suspicious dates with high volume of reviews generated
* review_100.csv: user review data group by “biz_id” which means restaurant_id, showing review user features and rating deviation from restaurant’s rating_mean.
* review_100_rf.csv:data prepared for random forest regressor
* review_100_fakeclean.csv: merge review_100.csv with fakedate.csv then remove rows containing fake dates
user_rating_importance.png
desicion_tree.png

### Part 2: Restaurant feature recommendation
### input data: 
* restaurant_atl.json: restaurant data including coordinates, rating, category, and other features
### code: 
* json_csv.py: change restaurant_atl.json into csv format
* review_clean.py
* restaurant_feature_regression.py
### output data:
* restaurant_feature.csv: restaurants’ features prepared for random forest regressor
restaurant_feature_importance.png

### Data from yelp
### Part 1: Get Reviews through web crawler
### input data: 
https://www.yelp.com/search?find_desc=Restaurants&find_loc=Atlanta%2C+GA%2C+United+States&ns=1
The url link to search all restaurants in Atlanta.
### code: 
Yelp_dataset.ipynb
### output data:
reviews.csv: reviews of restaurants. Includes both user’s information and review information.
### Part 2: Get Restaurants’ features from Yelp API
### input data: 
* API_Key of yelp: jsBO_6tz-I_xVBQGEaeqKB8QOjL7god2tLnWEgR091pdwNjFTFx8-smrjsN5a4XMSzX7f88VQ_HP4PW2sV7OH6qOCn-AT3rXBWqjdh2zwCDrXMs7cjfCKZaUcPOAXnYx
code: 
* Yelp_api.py
* output data:
* business_data.json: features of restaurants


## PNPoly:
### code:
* python restaurants_data.pnpoly.py -n cities.json -r restaurant_atl.json -no neighborhood.json -ro restaurant_atl_neighborhood.json
input:
* cities.json: neighborhood data including coordinates of each vertex (stored in three dimensional array)
* restaurant_atl.json: all restaurant data including coordinates, rating, category, and other features
output:
* neighborhood.json: neighborhood data with new features, including restaurant count, top restaurant category, average restaurant rating
restaurant_atl_neighborhood.json: restaurant data with new classified neighborhood attribute


## Visualization:
This is an easy part. You can just use it! Open the map.html or introduction.html can start using this website. Users can click neighborhoods and circles on the map. Users can also click the bars in bar chart,  click ‘coins’ buttons and drag sliders to filter the data.
More details for programmers:
* images folder: stores image we use for the website.
* lib folder: stores d3.js library. You can download from d3.js website. Beautiful tools!
* cities.js: stores neighborhoods data. My geography is not good….
* restaurants.js: stores restaurants data.
* map.js: js for main plot. It based on Google Map API.
* subplot.js: js for sub plot. It based on d3.js.
