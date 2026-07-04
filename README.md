# Avvo - Aircraft Intelligence Platform

Avvo is an aircraft intelligence platform developed for CoralComp. The system stores aviation datasets in AWS S3, processes them using Python ETL scripts, loads cleaned records into PostgreSQL, exposes the data through a Django REST API, and displays search and analytics through a React dashboard.

## Current Status

- AWS S3 bucket structure configured
- FAA dataset loaded into PostgreSQL
- Boeing datasets loaded into PostgreSQL
- Airbus datasets loaded into PostgreSQL
- OpenSky datasets loaded into PostgreSQL
- Django REST API working
- React dashboard working
- Universal aircraft search working
- Analytics endpoint working
- Aircraft detail endpoint working

## System Architecture

```text
FAA / Boeing / Airbus / OpenSky datasets
        ↓
AWS S3
        ↓
Python ETL
        ↓
PostgreSQL
        ↓
Django REST API
        ↓
React + D3 Dashboard
