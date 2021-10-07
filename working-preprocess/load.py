import pandas as pd
from abc import *

class AbstractLoader(ABC) :
    
    @abstractmethod
    def load(self, sql: str) -> pd.DataFrame:
        pass

class SparkLoader(AbstractLoader) :

    def __init__(self, spark_session) :
        self._spark_session = spark_session

    def load(self, sql: str, raw = False) -> pd.DataFrame:
        df = self._spark_session.sql(sql)
        if raw  :
            return df
        return df.toPandas()

class CsvLoader(AbstractLoader) :

    def __init__(self, path) :
        self._path = path

    def load(self, sql: str = None) -> pd.DataFrame:
        df = pd.read_csv(self._path)
        if sql :
            pass # do something if sql 
        return df

class LoadController() :

    def __init__(self, config) :
        self._config = config
    
    def load(self) :
        loader = self.get_loader()
        sql = self.get_sql()
        
        return loader.load(sql)

    def get_loader(self) -> AbstractLoader:
        '''
        select data loader based on config
        '''
        source = self._config['source']
        if source == 'csv' :
            return self.create_csvLoader()
        elif source == 'spark' :
            return self.create_sparkLoader()
        raise Exception("source is undefined")

    def create_csvLoader(self) -> CsvLoader:
        path = self._config['path']
        loader = CsvLoader(path)
        return loader

    def create_sparkLoader(self) -> SparkLoader:
        # path = self._arguments['path'] # ?
        session = SparkSession \
                .builder \
                .appName('NEWWORD_EXTRACT') \
                .enableHiveSupport() \
                .config("spark.driver.extraClassPath", "hdfs://nameservice1/tmp/tibero6-jdbc.jar") \
                .getOrCreate()
        loader = SparkLoader(session)
        return loader

    # todo : fix this
    def get_sql(self) :
        '''
        return SQL from config.yml based on arguments
        '''
        return "select * from table"