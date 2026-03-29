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


<img width="983" height="1506" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/58e33777-5d74-45f5-9b23-0882b4bfc5b9" />


## Author
Priyanshi
