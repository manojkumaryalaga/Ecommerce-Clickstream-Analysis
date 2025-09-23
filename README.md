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
# AWS Data Pipeline Architecture

<img src="screenshots/sc%200.png" width="600">

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

---

### 🚀 How to Run

🔑 Prerequisites

AWS account with access to: Kinesis, S3, Glue, Athena, QuickSight, CloudWatch

<img src="screenshots/sc%201.png" width="400">

Python 3.8+

Install dependencies:

pip install boto3 faker

▶️ Run the Producer

python producer.py

<img src="screenshots/sc%202.png" width="400">

This generates synthetic JSON events and pushes them to Kinesis Firehose → S3 Raw bucket.

<img src="screenshots/sc%203.png" width="400">

---
📊 Query with Athena

Run SQL queries



---
📈 Visualize in QuickSight

Connect QuickSight to Athena dataset.

---
📊 CloudWatch Monitoring

   In this project, CloudWatch is configured to monitor the health of the ingestion and analytics pipeline:

1. Kinesis Firehose Metrics:

   Records successfully delivered to S3

   Failed delivery attempts

2. S3 Buckets (Raw & Processed):

   Object creation logs (new files landing in raw and processed buckets)

3. Athena Queries:

   Query execution times

   Query failures

   CloudWatch dashboards and alarms were set up to track these metrics, ensuring pipeline reliability.

---
