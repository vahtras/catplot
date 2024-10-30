import os
from .main import main as catplot_main

def main():
    os.environ['plot_type'] = 'box'
    catplot_main()
