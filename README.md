# Objectives

Make self-sufficient programs for US and Indian options.

# NSE
1. Get a list of NSE options
2. Extract the option chains
3. Get the margins, lots and price for the underlyings 
4. Store historical ohlc for standard deviation of underlyings
5. Prepare dataframe with option chain, PoP (from standard deviation), RoM (from margin)
7. Make a target list of option orders
8. Place the orders
9. Extract existing positions
10. Make closing trades

## Structure

Each of the above steps have individual programs. The programs are numbered 01, 02, ...

There are 'helper' functions that are individually tested to build the programs. These functions begin with the letter *f*.

A sub-folder called *zdata* contains datasets - either in csv, pickle or hdf. The files in *z_data* are used to pass data from one program to another.

### 1. Get a list of active NSE equity option

STATUS: Complete

This program prepares dataframes for NSE equity and indexes and pickles them into:
*df_nse_eq_symbols.pkl* for Equity symbols
*df_nse_idx_symbols.pkl* for Index symbols

<b>*Note*</b>

1. Some Index symbols in IBKR is not available in NSE
2. To check availability of symbols in NSE websites, refer: https://www.nseindia.com/products/content/derivatives/equities/fo_underlying_home.htm

### 2. NSE option chain extraction

STATUS: Complete

This program extracts the expiries and option chain info from NSE website, based on:
   *zdata/df_nse_eq_symbols.pkl*
   *zdata/df_nse_idx_symbols.pkl*

The dataframe generated is pickled into *zdata/df_nse_options.pkl*.

### 3. Get underlying's Margins, Lots and Price

STATUS: Incomplete

To-do:
1. Separate equity and index underlying

This program extracts the underlying's details and pickles them in *zdata/df_underlying.pkl*

### 4. Store historical data for computing standard deviation

STATUS: In-progress

This program extracts OHLC by date for underlyings and pickles them in *zdata/ohlc.pkl*




## Appendix
The following programs have been archived. It has some good code for future reference or backup.
1. Get margins from NSE web-site data
2. Scrape from NSE the equity underlying details into a dataframe (good bs4 + json implementation)

