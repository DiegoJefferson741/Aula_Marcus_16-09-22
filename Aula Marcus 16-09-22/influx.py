import argparse
import pandas as pd

from influxdb import DataFrameClient


def main(host='localhost', port=8086):
    """Instantiate the connection to the InfluxDB client."""
    '''Usuário e senha'''
    user = 'admin'
    password = '123'
    '''Informar nome do banco'''
    dbname = 'iot2' 
    protocol = 'line'

    client = DataFrameClient(host, port, user, password, dbname)

    print("Create pandas DataFrame")
    df = pd.DataFrame(data=list(range(30)),
                      index=pd.date_range(start='2014-11-16',
                                          periods=30, freq='H'), columns=['0'])

    print("Criando base de dados: " + dbname)
    client.create_database(dbname)

    print("Escrevendo DataFrame")
    #client.write_points(df, 'exemplo', protocol=protocol)

    #print("Escrevendo DataFrame com as tags")
    client.write_points(df, 'exemplo',
                        {'k1': 'v1', 'k2': 'v2'}, protocol=protocol)

    print("Lendo DataFrame")
    
    result=client.query("select * from exemplo")
    print(result)
    

def parse_args():
    """Parse the args from main."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    host='localhost'
    port=8086
    main()
