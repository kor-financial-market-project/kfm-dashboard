import json
import requests
from datetime import datetime, timedelta
import csv
from io import StringIO
import boto3
import os


def lambda_handler(event, context):
    apikey = os.environ['KOREA_BANK_API_KEY']
    stat_code = '731Y001/D'
    item_code = '0000001'
    service_name = 'StatisticSearch'
    start_date = (datetime.now() - timedelta(days=7)).strftime('%Y%m%d')
    end_date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
    print(f'{start_date} - {end_date}')
    
    api_url = f'https://ecos.bok.or.kr/api/{service_name}/{apikey}/json/kr/1/10000/{stat_code}/{start_date}/{end_date}/{item_code}/'
    response = requests.get(api_url)
    data = response.json()
    rows = result['StatisticSearch']['row']
    
    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer)
    
    headers = rows[0].keys()  
    csv_writer.writerow(headers)
    
    for item in rows:
        csv_writer.writerow(item.values())
    
    s3 = boto3.client('s3')
    bucket_name = "kor-financial-market"
    file_name = f"ELT/won_us_trading_base_rate/extractedAt_{datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=csv_buffer.getvalue()
    )

    return {
        'statusCode': 200,
        'body': f"CSV data successfully stored in {bucket_name}/{file_name}"
    }


