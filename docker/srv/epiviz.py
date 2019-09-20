from epivizfileserver import setup_app, create_fileHandler, MeasurementManager
import os
import numpy
import pickle

if __name__ == "__main__":
    # create measurements manager
    mMgr = MeasurementManager()

    # create file handler
    mHandler = create_fileHandler()

    fmeasurements = mMgr.import_files(os.getcwd() + "/epiviz.json", mHandler)

    app = setup_app(mMgr)
    app.run(host="0.0.0.0", port=8000)
    