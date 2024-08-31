import yfinance as yf
import ta  # if using the alternative for TA-Lib
import pandas as pd
import numpy as np
import plotly.express as px
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

print("All libraries imported successfully!")
