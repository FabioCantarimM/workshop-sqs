import json
import boto3
import pandas as pd
from io import StringIO
from datetime import datetime

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # O evento recebido é um evento S3
    for record in event['Records']:
        s3_bucket = record['s3']['bucket']['name']
        s3_key = record['s3']['object']['key']
        
        print(s3_bucket)
        print(s3_key)
        
        # Baixar o arquivo do S3
        s3_object = s3_client.get_object(Bucket=s3_bucket, Key='raw/Pan.csv')
        file_content = s3_object['Body'].read().decode('utf-8')

        # Transformar o conteúdo do arquivo em um DataFrame
        df = pd.read_csv(StringIO(file_content))

        # Adicionar as colunas 'nome do arquivo' e 'data'
        df['nome do arquivo'] = s3_key
        df['data'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Aqui você pode fazer o que precisa com o DataFrame
        # Por exemplo, salvar o DataFrame atualizado de volta no S3 ou em outro lugar
        
        print(df)
        
        # Exemplo de salvando de volta no S3
        output_buffer = StringIO()
        df.to_csv(output_buffer, index=False)
        output_content = output_buffer.getvalue()
        
        output_key = f"processed/{s3_key}"
        s3_client.put_object(Bucket=s3_bucket, Key=output_key, Body=output_content)

    return {
        'statusCode': 200,
        'body': json.dumps('Arquivo processado com sucesso!')
    }
