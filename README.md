## 🛒 E-Commerce Clickstream Analytics on AWS

## 📌 Project Overview

This project demonstrates a real-time data ingestion and analytics pipeline for eCommerce clickstream data.
A Python producer script simulates user activity (clicks, views, add-to-cart, purchases, etc.) and streams it into AWS services for storage, querying, monitoring, and visualization.

---
## 📑 JSON Event Schema

Each JSON event has the following fields:

| Field       | Type   | Description                                  |
|-------------|--------|----------------------------------------------|
| user_id     | string | Unique identifier for the user               |
| session_id  | string | Unique session tracking ID                   |
| event_type  | string | Action type (view, click, add_to_cart, purchase) |
| page        | string | Page visited (home, product, checkout, etc.) |
| product_id  | string | Product identifier                           |
| timestamp   | string | Event timestamp (ISO 8601)                   |
| device_type | string | Device used (mobile, desktop, tablet)        |
| referrer_url| string | Source of traffic                            |
| location    | string | User’s region/country                        |
| browser     | string | Browser used                                 |
| user_type   | string | New vs returning customer                    |

---
## ⚙️ Components

1. Python Producer (producer.py)

   Simulates events and streams them to Kinesis Firehose.

   Produces ~1 event/sec (configurable).

2. Amazon Kinesis Firehose

   Ingests events and delivers them to S3 Raw bucket.

3. Amazon S3 (Raw & Processed Buckets)

   Raw JSON logs stored in one bucket.

   Processed data (query results, Parquet) stored in another bucket.

4. AWS Glue Data Catalog
 
   Provides schema + metadata for querying with Athena.

5. Amazon Athena

   Runs SQL queries on clickstream data.

6. Amazon QuickSight

   Dashboards for funnel analysis, product performance, user engagement.

7. Amazon CloudWatch

   Monitors ingestion pipeline health + Firehose delivery metrics.
