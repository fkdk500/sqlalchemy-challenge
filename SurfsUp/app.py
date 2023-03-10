#importing numerical PY and datetime
import numpy as np
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 

from flask import Flask, jsonify  #initializing for flask 


# Database Setup/ create engine to hawaii.sqlite to connect to sqlite database
engine = create_engine("sqlite:///../Resources/hawaii.sqlite") 

# reflect an existing database into a new model
Base = automap_base() #to reflect tables into classses 

# reflect the tables
Base.prepare(engine, reflect=True)

#Save references  each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Flask route for all required routes 
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

#route for precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # linking the session from Python to the DB
    session = Session(engine)

    """Convert the query results to a dictionary using `date` as the key and `prcp` as the value"""
    # Query all Precipitation
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= '2016-08-23').\
    all()
    
    session.close()

    # Create a empty list as a variable to collect generating date and precipitation data
    all_prcp = []
    for date,prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp

        all_prcp.append(prcp_dict)
    return jsonify(all_prcp) #Return the list as a json file

#Route for stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    # Query the stations and generate stations dataset
    results = session.query(Station.station).all()
    session.close()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations) #Return a JSON list of stations from the dataset

#Route for tobs
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    """Return a JSON list of temperature observations (TOBS) for the previous year."""
    tobs_results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= "2016-08-23").\
        filter(Measurement.station == 'USC00519281').all()
    session.close()
    # Create a empty list as a variable to collect generating date and temprature of observation data
    all_tobs = []
    for date,tobs in tobs_results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)
    return jsonify(all_tobs)

#Route for start 
@app.route("/api/v1.0/<start>")
def start_tob(start):

      # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of temperature observations from starting date to most recent date."""
    # Query the tobs from starting date to most recent date of the dataset and calculate the Minimum, Average and Maximum temrature.
    results = (session.query(Measurement.date, func.min(Measurement.tobs),\
              func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
              filter((Measurement.date) >= start).group_by(Measurement.date).all())
    
    # close session
    session.close()

    # Create a empty list as a variable to collect generating date and temprature of observation data and create a dictionary for Min, Avg and Max
    start_tobs = []
    for date, min,max,avg in results:
        start_tob_dict = {}
        start_tob_dict["date"] = date
        start_tob_dict["min_tobs"] = min
        start_tob_dict["max_tobs"] = max
        start_tob_dict["avg_tobs"] = avg
        start_tobs.append(start_tob_dict)
 
    return jsonify(start_tobs)    #Return a JSON file

@app.route("/api/v1.0/<start>/<end>")
def start_end_tob(start,end):
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of temperature observations from the provided start date and end dates."""
    # Query the tobs for a given start and end dates and calculate the Minimum, Average and Maximum temrature.
    results = (session.query(Measurement.date, func.min(Measurement.tobs),\
              func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
              filter((Measurement.date) >= start, Measurement.date <= end).group_by(Measurement.date).all())
    
    # close session
    session.close()

    # Create a empty list as a variable to collect generating date and temprature of observation data and create a dictionary for Min, Avg and Max
    start_tobs = []
    for date, min,max,avg in results:
        start_end_tob_dict = {}
        start_end_tob_dict["date"] = date
        start_end_tob_dict["min_tobs"] = min
        start_end_tob_dict["max_tobs"] = max
        start_end_tob_dict["avg_tobs"] = avg
        start_tobs.append( start_end_tob_dict)
 
    return jsonify(start_tobs)    #Return a JSON file
     

if __name__ == '__main__':
    app.run(debug=True)