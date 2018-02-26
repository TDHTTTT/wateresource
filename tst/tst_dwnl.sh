#!/bin/bash

#wget "http://rapid-hub.org/data/angles_UCI_CS.csv"
#wget "http://rapid-hub.org/data/angles_UCI_CS_out.csv"

curl -fsS -o angles_UCI_CS.csv "http://rapid-hub.org/data/angles_UCI_CS.csv"
curl -fsS -o angles_UCI_CS_out.csv "http://rapid-hub.org/data/angles_UCI_CS_out.csv"
