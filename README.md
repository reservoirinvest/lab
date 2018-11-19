# Objectives

Make self-sufficient programs for US and Indian options.

# NSE
1. Get a list of active NSE options
2. Extract the option chains
3. Get the underlying's details
4. Store historical ohlc for standard deviation
5. Get the margins
6. Prepare dataframe with option chain, PoP (from standard deviation), RoM (from margin)
7. Make a target list of option orders
8. Place the orders
9. Extract existing positions
10. Make closing trades

## Structure

Each of the above steps have individual programs. The programs are numbered 01, 02, ...

There are 'helper' functions that are individually tested to build the programs. These functions begin with the letter *f*.

A sub-folder called *zdata* contains datasets - either in csv, pickle or hdf. The files in *z_data* are used to pass data from one program to another.

### 1. Get a list of active NSE equity option

STATUS: Manually done

Data from https://www.nseindia.com/products/content/derivatives/equities/fo_underlying_home.htm in the following steps:
1. Copy and paste to spreadsheet
2. Copy the 'Symbol' column to notepad++. The first row should be 'Symbol'
3. Delete index symbols
4. Store the file as *raw_equity.csv*

### 2. NSE option chain extraction

STATUS: Completed

This program extracts the expiries and option chain info from NSE website, based on *zdata/_raw_equity.csv*

The dataframe generated is pickled into *zdata/nse_options.pkl*.

Good equity and index symbols are stored in *zdata/nse_idx_symbols.csv* and *zdata/nse_eq_symbols.csv*

### 3. Get underlying's details

STATUS: Completed

This program extracts the underlying's details and pickles them in *zdata/underlying_df.pkl*

### 4. Store historical data for computing standard deviation

STATUS: In-progress

This program extracts OHLC by date for underlyings and pickles them in *zdata/ohlc.pkl*



