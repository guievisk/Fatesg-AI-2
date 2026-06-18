# Cassandra Sensor Data Management

This project demonstrates the implementation of a sensor data management system using the Apache Cassandra database via DataStax Astra DB. The objective is to efficiently store and query sensor readings, utilizing a partition key structure to optimize performance for time-series data.

## Project Overview

The system is designed to handle telemetry data from multiple sensors. It employs a specific data model to ensure that readings for a particular sensor on a specific date are physically grouped, allowing for rapid retrieval and efficient storage management.

## Technical Stack

* Database: Apache Cassandra (DataStax Astra DB).
* Query Language: CQL (Cassandra Query Language).
* Integration: REST API.
* Programming Language: Python.

## Database Schema

The core table, leituras_sensor, is structured as follows:

| Column | Type |
| :--- | :--- |
| sensor_id | text |
| data_leitura | date |
| horario | timestamp |
| temperatura | decimal |
| umidade | decimal |
| status | text |

Primary Key: ((sensor_id, data_leitura), horario)
* Partition Key: (sensor_id, data_leitura)
* Clustering Column: horario (Ordered DESC)

This schema ensures that all readings for a unique sensor on a single day are co-located, and within each partition, data is sorted chronologically in descending order by timestamp.

## Implementation Details

### Data Ingestion
Records are inserted into the leituras_sensor table with specific identifiers, environmental metrics (temperature and humidity), and operational status.

### API Integration
The system interacts with the Astra DB REST API to perform data operations. Access is secured using a token-based authentication mechanism.

#### Connection Parameters
To connect to the database, the following credentials are required:
* Database ID: The unique identifier for the Astra DB instance.
* Region: The AWS region where the database is hosted.
* Token: A generated authentication token (AstraCS:...) that grants API access.

## Query Operations

To retrieve data for a specific sensor on a given date, the following CQL pattern is utilized:

```sql
SELECT * FROM leituras_sensor 
WHERE sensor_id = 'your_sensor_id' 
AND data_leitura = 'yyyy-mm-dd';

## Maintenance and Cleanup

The following commands are available for database management:

* Data Removal: TRUNCATE leituras_sensor; (Clears all records while keeping the table structure).
* Partition Deletion: DELETE FROM leituras_sensor WHERE sensor_id = '...' AND data_leitura = '...'; (Removes specific partitions).
* Table Removal: DROP TABLE leituras_sensor; (Permanently deletes the table schema).

## License

This project is intended for educational purposes and demonstrates standard practices for Cassandra database modeling and API integration.
