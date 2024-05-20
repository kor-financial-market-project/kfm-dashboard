# 한국 금융시장과 소비에 대한 이해

본 레포지토리는 **'데이터 웨어하우스를 이용한 대시보드 구성'** 을 주제로 진행된 팀 프로젝트의 결과물을 담은 레포지토리입니다.
- extract directory : 데이터 수집/적재 관련 코드를 위한 저장소
- auto directory : 데이터 수집/적재 자동화 관련 코드를 위한 저장소

## 프로젝트 주제

한국 은행의 데이터를 활용해서 우리나라의 여러 금융 요소들을 살펴보고, 어떤 요소에 영향을 받는지 알아보는 대시보드를 만들었습니다.<br/>
각 챕터별로 대시보드를 만들었고, 환율과 소비량에 따른 물가의 관계, 부동산, 경제 심리 지수 각각에 대한 데이터 수집, 적재, 분석을 진행했습니다.

## 활용 언어, 기술 및 프레임워크

- 프로그래밍 언어 : Python, SQL
- 데이터 수집 : OpenAPI
- 데이터베이스 : AWS S3, AWS Redshift Serverless
- 스케줄링(자동화): AWS EventBridge, AWS Lambda, Boto3
- 네트워크/보안 : AWS IAM, AWS VPC

## 활용 데이터

[한국은행 Open API 서비스](https://ecos.bok.or.kr/api/#/)

## 대시보드

![kor-financial-market-2024-05-19T23-48-21 630Z](https://github.com/kor-financial-market-project/kfm-dashboard/assets/64184518/9d54313e-9d14-4092-b8ca-18d6ba1bafc3)
![project_screenshot](https://github.com/kor-financial-market-project/kfm-dashboard/assets/64184518/703e4268-b439-42ab-90e1-7f07e51b0a24)

## 시스템 구조도

![extract_automation_diagram drawio (2) (1)](https://github.com/kor-financial-market-project/kfm-dashboard/assets/64184518/2cbae295-32ff-4b3e-8853-2753a92967de)

## 참여자 정보/역할

1. 이정화 : 물가지수,환율 관련 데이터 수십 및 ETL, 대시보드 개발
2. 이하영 
3. 정승현 : 소비지출 관련 데이터 수집 및 ETL, 자동화 인프라 구축, 대시보드 개발
4. 최은희 : 경제심리지수 관련 데이터 수집 및 ETL, 대시보드 개발


## 프로젝트 상세 정보

- [보고서](https://cyclic-river-4c1.notion.site/2-2-2-43af810df24340879a80b9b46e95b4c3?pvs=4)
