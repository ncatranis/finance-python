import environ
import os

env = environ.Env(
    # set casting, default value
    IEX_API_KEY=(str, ""),
)
environ.Env.read_env()

IEX_API_KEY = env("IEX_API_KEY")
IEX_BASE_URL = "https://cloud.iexapis.com/stable"