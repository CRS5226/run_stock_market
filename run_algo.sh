#!/bin/bash
# /root/start.sh

echo "🚀 Starting Stock Market System..."

# Go to project folder
cd /root/chitraksh/stock_market_breakout_7 || exit

# Activate virtual environment
source stock_market_env/bin/activate

# Run the main wrapper
python run_stock_algo.py
