

#***      Function to print python code in Jupyter   ****
#________________________________________________________

def display_py(code):
    """Displays python file code in Jupyter

    Arg: (string from py file) code

    Output: code formatted for jupyter

    Usage:
    with open(myfile) as f:
         code = f.read()

    display_py(code)
    """
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import HtmlFormatter
    import IPython
    
    formatter = HtmlFormatter()

    html_code = highlight(code, PythonLexer(), HtmlFormatter())
    styled_html = '<style type="text/css">{}</style>{}'.format(formatter.get_style_defs('.highlight'), html_code)
    ipython_code = IPython.display.HTML(styled_html)

    return ipython_code

#***      Function to get historical data     *****
#___________________________________________________
def get_hist(contract, duration):
    '''Gets 1-day bars of contracts for the duration specified
    Args:
        (contract): contract as obj
        (duration): history days as int
    Returns: dataframe of symbol, date, ohlc, avg and volume 
    '''
    
    import pandas as pd
    
    # Prepare the duration
    strduration = str(duration) + ' D'
    
    # Extract the history
    hist = ib.reqHistoricalData(contract=contract, endDateTime='', 
                                    durationStr=strduration, barSizeSetting='1 day',  
                                                whatToShow='Trades', useRTH=True)

    # Make the dataframe
    cols=['ibSymbol', 'D', 'O', 'H', 'L', 'C', 'Avg', 'Vol']
    df = pd.DataFrame([(contract.symbol, h.date, h.open, h.high, h.low,h.close, h.average, h.volume) 
                      for h in hist], columns=cols)
    return df
