# Objectives

## NSE
1. Get a list of active NSE options
2. Extract the option chains
3. Prepare underlying's historical ohlc for standard deviation
4. Get the margins
5. Prepare dataframe with option chain, PoP (from standard deviation), RoM (from margin)
6. Make a target list of option orders

# Approach

Each of the above steps have individual programs. The programs are numbered 01, 02, ...

There are 'helper' functions that are individually tested to build the individual programs. These functions begin with the letter <i>f_</i>

