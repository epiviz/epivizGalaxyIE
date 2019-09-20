#!/usr/bin/python
from epivizfileserver import setup_app, create_fileHandler, MeasurementManager, parser
import os
import numpy
import pickle
import sys
ff = parser.BigWig("/Users/hyeyunchae/galaxy-19.05/database/files/000/dataset_61.dat")
res, _ = ff.getRange("chrII", 717184, 747184)
print(res)
