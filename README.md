# OnDemand/Passenger: Flask example app

This is a [Flask](http://flask.pocoo.org/) hello world example app for [the Passenger application server](https://www.phusionpassenger.com/) that has been modified to work with [OnDemand](https://openondemand.org/).

## Setup

To boot this application one must run `./setup.sh` to setup the app's virtual environment and install
all the dependencies.

Though you must take caution in terms of _where_ you issue `./setup.sh` from. You must match
the python environment of the OnDemand webserver because when the app boots it'll boot under
the OnDemand webserver's python environmet which may differ from the environment you used when
you issued `./setup.sh`.
