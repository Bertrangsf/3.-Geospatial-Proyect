![portada](https://ep01.epimg.net/elpais/imagenes/2018/05/04/seres_urbanos/1525448946_820849_1525688731_noticia_normal.jpg)

# GeoSpatial Data Project

## Overview

under the hypothesis that I have recently created a new company in the `WEB design` with the following scheme:

- 10 Designers
- 2 UI/UX Engineers
- 5 Frontend Developers
- 7 Data Engineers
- 7 Backend Developers
- 10 Account Managers
- 1 Maintenance 
- 6 Executives

As a data engineer, I have asked all the employees to show their preferences on where to place the new office. My goal is to place the **new company offices** in the best place for the company to grow. I had to find a place that more or less covers all the following requirements (note that **it's impossible to cover all requirements**, so I had to prioritize at my glance):

- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do web design.
- 90% of the company staff have at least 2 children. There must be some nearby schools (primary, middle, and high).
- Developers & Executives like Starbucks A LOT. Ensure there's a Starbucks not too far.

## Table of Contents
1. [General Info](#general-info)
2. [Data treatment](#Data-treatment)
3. [Libraries](#Libraries)
4. [Technology](#Technology)
5. [Methodology](#Methodology)

## General Info

On this project, I have generated maps that display the important things the employees of my new company cares about. I've used a database (dbd) with some companies all over the world to make a preliminary selection and comprobations. After I have made calls to foursquare API ('https://api.foursquare.com/v2/venues/explore') to find the important places from my employee's preferences.

## Data treatment

The realization of the project is divided into up to 3 parts: 

1. Comprobations in MongoDB (find companies under some criteria). (Analysis)
2. Requesting four square-API locations and mapping them. (Analysis)
3. Visualization (for my employees to vote under some criteria). (Analysis)

## Libraries

```
pandas 
requests
json
dotenv 
os
operator
functools (reduce)
folium
```

## Technology: 

A list of technologies used within the project:

1. [Jupyter Notebook](https://jupyter.org/) : Version 6.1.4
2. [Python](https://www.python.org/): Version 3.8
3. [Visual Studio Code](https://code.visualstudio.com)
4. [MongoDB](https://www.mongodb.com)

## Methodology: 

The realization of the project is divided in 2 parts: 

### 1. Analysis:

#### 1.1 Mongo_queries & Geocode_df:

* Mongo consulting: 

       - Web companies in Madrid, Miami and CapeTown with 10-100 employees founded before 2005.

* Requesting geocode API (https://geocode.xyz) and creating a df ([.src.functions1.df_final]).   

#### 1.2 Api_calls & Mapping:

* API requesting the under the parametres ([.src.functions2.data]):

      - Places considerated to be: "Starbucks", "High School", "Middle School", "Preschool".
      
      - With less than 10km away from the given distance of each city by "geocode" (assuming this is the center of the best area to open my company in each city).

* Df cleaning ([.src.functions2.clean]):

      - Cleaning the dictionary obtanined from API request.
 
* Converting dictionary to df ([.src.functions2.to_df]):

      - Filtering and cleaning the dictionary.
      
      - Create a df with the relevant information (name, category, latitude, and longitude).

* Maping with markers ([.src.functions2.mapping]):

      - Creating a map with folium for each city marking the places by their category ("Starbucks", "High School", "Middle School", "Preschool").

#### 1.3 Visualization and ELECTIONS:

* After importing the maps of each city and checking the feasibility of moving my new company there, I want my employees to decide city. The office will be situated in the better and cheapest place near the coordinates given by geocoding.
* I need to bring all employees to fill up the survey to decide the final city! ([.src.functions3.The_Final_City])

## Author

* **Bertrán Gil de Santivañes Finat** - *Initial work* - (https://github.com/Bertrangsf/3.-Geospatial-Proyect)
