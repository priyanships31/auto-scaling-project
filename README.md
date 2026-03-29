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
   http://<VM-IP>:5000/load

## Result
When CPU usage exceeds 75%, new instances are automatically created in GCP.

## Architecture Diagram


A[Local VM<br>Ubuntu 22.04] --> B[Flask App (app.py)<br>Generates CPU Load]

B --> C[Prometheus<br>Collects Metrics]

C --> D[monitor.py Script<br>
Reads CPU using psutil<br>
Scale UP if CPU > 75%<br>
Scale DOWN if CPU < 30%<br>
Uses gcloud CLI]

C --> E[Grafana<br>Visualizes Metrics]

D --> F[Google Cloud (GCP)<br>Managed Instance Group]

F --> G[Auto Scaling<br>Add/Remove e2-micro Instances]

## Author
Priyanshi
