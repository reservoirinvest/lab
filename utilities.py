from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import IPython

# Function to print python code in Jupyter
def display_py(code):
    """Displays python file code in Jupyter

    Arg: (string from py file) code

    Output: code formatted for jupyter

    Usage:
    with open(myfile) as f:
         code = f.read()

    display_py(code)
    """
    formatter = HtmlFormatter()

    html_code = highlight(code, PythonLexer(), HtmlFormatter())
    styled_html = '<style type="text/css">{}</style>{}'.format(formatter.get_style_defs('.highlight'), html_code)
    ipython_code = IPython.display.HTML(styled_html)

    return ipython_code

