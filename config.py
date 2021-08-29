HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ

    API_ID = int(environ["7159058"])
    API_HASH = environ["52f7d0b91e980d80f6c84ed609097c45"]
    SESSION_STRING = environ["BACK-dQ26ji8d2d4WNNsQMipfpTMivfD5ZdZChws-A9IwlKQ4aedvTZyTDPCASimTvfsdXtO2ZZBStkRYM2junKpfTRqJeKOyT9hVgDP3yvTwVWjzbt45YXN2Sc9a0un9_j0xS3S0kW4xYngtBCYf3fyFlm501ZTVCbmYJl9mO6MIeBRf66_68pmoBNp9dohTJO9c174DwEJB38hkEDYJSG7oEl7pe2XB_OLvWfpunEuX4CxviviLy3ttEEwvsIQyZ75vu_w-sFk0PJfQNsZS_Z-IQE7inqmJDLVMbx8ns-pwKCGNCo_zVFaPHAgxZZac2v7SmsSNMUkWXJ-6difl-JbddZ6QQA"]  # Check Readme for session
    ARQ_API_KEY = environ["RUEIYU-ODVAEG-TBUHMX-YMQHTQ-ARQ"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
