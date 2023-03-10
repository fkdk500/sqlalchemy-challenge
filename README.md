# sqlalchemy-challenge
Analyze and Explore the Climate Data using Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically,use SQLAlchemy ORM queries, Pandas, and Matplotlib. 

The provided data are files (climate_starter.ipynb and hawaii.sqlite) to complete your climate analysis and data exploration.

The aims of the exercise  are
1. Use the SQLAlchemy create_engine() function to connect to your SQLite database.

2. Use the SQLAlchemy automap_base() function to reflect on tables into classes, and then save references to the classes named station and measurement.

3. Link Python to the database by creating a SQLAlchemy session.
4 Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections

Part 1: Analyze and Explore the Climate Data

    Precipitation Analysis includes
-Find the most recent date in the dataset.

-Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

-Select only the "date" and "prcp" values.

-Load the query results into a Pandas DataFrame, and set the index to the "date" column.

-Sort the DataFrame values by "date".

-Plot the results by using the DataFrame plot method
-Use Pandas to print the summary statistics for the precipitation data.

    Station Analysis includes
-Design a query to calculate the total number of stations in the dataset.

-Design a query to find the most-active stations (that is, the stations that have the most rows). 
    -List the stations and observation counts in descending order.
    -Answer the following question: which station id has the greatest number of observations?

-Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
-Design a query to get the previous 12 months of temperature observation (TOBS) data. 

Part 2: Design Your Climate App

Design a Flask API based on the queries that is just developed. To do so, use Flask to create your routes as follows:
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"