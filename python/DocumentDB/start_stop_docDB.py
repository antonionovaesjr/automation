import boto3
import os
import sys

import boto3

def lambda_handler(event, context):


    client = boto3.client('docdb')


    try:
        if os.environ.get('DOCDB_NAME') is None:
            documentdb_name = event['DOCDB_NAME']
        else:
            documentdb_name = os.environ.get('DOCDB_NAME')
        
        if os.environ.get('DOCDB_NAME') is None:
            action_desired = event['DOCDB_ACTION']
        else:  
            action_desired = os.environ.get('DOCDB_ACTION')
    except Exception as e:
        print("não foi possível obter o valor da variável DOCDB_ACTION ou DOCDB_NAME")
        sys.exit(1)



    if action_desired == "start":
        try: 
            response = client.start_db_cluster(
            DBClusterIdentifier=documentdb_name
            )
            print(response)
            print("######################")
            print("######################")
            print("#########INFO#########")
            print("O Cluster {} foi iniciado".format(documentdb_name))
        except Exception as e:
            print("não foi possível iniciar o cluster {}".format(documentdb_name))
            print(e)
            sys.exit(1)
        
    elif action_desired == "stop":
        try:
            response = client.stop_db_cluster(
            DBClusterIdentifier=documentdb_name
            )
            print(response)
            print("######################")
            print("######################")
            print("#########INFO#########")
            print("O Cluster {} foi parado".format(documentdb_name))
        except Exception as e:
            print("não foi possível para o cluster {}".format(documentdb_name))
            print(e)
            sys.exit(1)
            
    elif action_desired is None:
        print("Nenhuma ação possível foi especificada, valores possíveis: start ou stop")
        
    else:
        print("Ação {} não é reconhecida, valores possíveis: start ou stop".format(action_desired))


if __name__ == "__main__":
    #event = {"DOCDB_NAME":"labdevops-test","DOCDB_ACTION":"start"}
    event = ""
    lambda_handler(event,"")
