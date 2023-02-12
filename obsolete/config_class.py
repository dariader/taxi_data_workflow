class Config:
    def __init__(self, params):
        self.user = params.get('user', ValueError('No param in config!'))  # 'user name for postgres'
        self.root = params.get('root', ValueError('No param in config!')) # 'password for postgres'
        self.host = params.get('host', ValueError('No param in config!')) # 'host for postgres'
        self.port = params.get('port', ValueError('No param in config!')) # 'port for postgres'
        self.db = params.get('db', ValueError('No param in config!'))  # 'database name for postgres'
        self.table_name = params.get('taxi_data', ValueError('No param in config!')) # 'name of the table where we will write the results to'
        self.url = params.get('url', ValueError('No param in config!')) # 'url of the csv file'