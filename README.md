🛒 E-Commerce Clickstream Analytics on AWS

📌 Project Overview

This project demonstrates a real-time data ingestion and analytics pipeline for eCommerce clickstream data.
A Python producer script simulates user activity (clicks, views, add-to-cart, purchases, etc.) and streams it into AWS services for storage, querying, monitoring, and visualization.

🗂️ Dataset (Clickstream Event Fields)

Each JSON event has the following fields:

Field	Type	Description
user_id	string	Unique identifier for the user
session_id	string	Unique session tracking ID
event_type	string	Action type (view, click, add_to_cart, purchase)
page	string	Page visited (home, product, checkout, etc.)
product_id	string	Product identifier
timestamp	string	Event timestamp (ISO 8601)
device_type	string	Device used (mobile, desktop, tablet)
referrer_url	string	Source of traffic
location	string	User’s region/country
browser	string	Browser used
user_type	string	New vs returning customer
