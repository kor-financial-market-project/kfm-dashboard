import json
import os
import psycopg2

def lambda_handler(event, context):
    db_host = os.environ['REDSHIFT_HOST']
    db_port = os.environ['REDSHIFT_PORT']
    db_user = os.environ['REDSHIFT_USER']
    db_password = os.environ['REDSHIFT_PASSWORD']
    db_name = os.environ['REDSHIFT_DBNAME']
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(bucket)
    print(key)
   
    conn_string = f"dbname='{db_name}' user='{db_user}' host='{db_host}' " \
                  f"port='{db_port}' password='{db_password}'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    # try:
    #     s3_path = f"s3://{bucket}/{key}"
    #     copy_query = f"""
    #     COPY your_table_name
    #     FROM '{s3_path}'
    #     IAM_ROLE 'arn:aws:iam::851725544098:role/redshift.read.s3'
    #     FORMAT AS CSV;
    #     """
        
    #     cursor.execute(copy_query)
    #     conn.commit()
    #     print("Data loaded successfully from S3 to Redshift.")
    # except Exception as e:
    #     print(f"Error loading data from S3 to Redshift: {str(e)}")
    # finally:
    cursor.close()
    conn.close()
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
