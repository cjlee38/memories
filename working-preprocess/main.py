import pandas as pd
import numpy as numpy
import os
import re
import sys

from config import *
from load import *

if __name__ == "__main__" :
    logger = get_logger()
    logger.info("start")
    
    # Parse Arguemnts
    ap = ArgumentParser()
    ap.parse(sys.argv)

    # loading & prep starts
    df = pd.read_csv("./bigtable.csv")
    logger.info("load dataframe")

    descriptions = df[df['DESC'].notna()]['DESC'].drop_duplicates()
    logger.info("description extracted")
    # loading & prep ends
    
    langClassifier = LangClassifier(Config.LANG_REGEX)
    langs = langClassifier.classify(descriptions, threshold = Config.LANG_THRESHOLD)

    searchClassifier = SearchClassifier(Config.SEARCH_REGEX)
    searches = searchClassifier.classify(langs['kor'])
    searchClassifier.describe()
    search_df = 

