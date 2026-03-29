# Auto Scaling Project

## Objective
To monitor resource usage on a local VM and automatically scale instances in Google Cloud when CPU usage exceeds 75%.

## Components
- Flask App (app.py): Generates CPU load
- Monitor Script (monitor.py): Monitors CPU and triggers scaling
- Prometheus: Collects metrics
- Grafana: Visualizes metrics
- GCP Managed Instance Group: Handles scaling

## How to Run

1. Start node exporter:
   ./node_exporter &

2. Start Prometheus:
   ./prometheus --web.listen-address="0.0.0.0:9090" &

3. Start Grafana:
   sudo systemctl start grafana-server

4. Run application and monitoring:
   python3 app.py & sleep 2 && python3 monitor.py

5. Trigger load:
   http://VM-IP:5000/load

## Result
When CPU usage exceeds 75%, new instances are automatically created in GCP.

## Architecture Diagram


+---------------------------+
|   User / Browser          |
|   (/load endpoint)        |
+------------+--------------+
             |
             v
+---------------------------+
|   Flask Application       |
|   (Generates CPU Load)    |
+------------+--------------+
             |
             v
+---------------------------+
|   Metrics Export          |
| (Node Exporter + App)     |
+------------+--------------+
             |
             v
+---------------------------+
|   Prometheus              |
|   (Metrics Collection)    |
+------------+--------------+
             |
             v
+---------------------------+
|   Grafana                 |
|   (Visualization)         |
+------------+--------------+
             |
             v
+---------------------------+
|   monitor.py              |
|   (Scaling Decision)      |
+------------+--------------+
             |
             v
+---------------------------+
|   Google Cloud Platform   |
|   Managed Instance Group  |
+------------+--------------+
             |
             v
+---------------------------+
|   Auto Scaling            |
|   (New VMs Created)       |
+---------------------------+
