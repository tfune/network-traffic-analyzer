# Network Traffic Performance Analyzer

This project simulates network traffic, records latency and packet loss in a SQLite database, and analyzes the results using Python.

## Features
- Simulates 1000 network packets with random latency
- Random 5% packet loss
- Stores packet telemetry in SQLite database
- Calculates average latency and packet loss
- Visualizes latency distribution with histogram

## Usage
1. Run `network_simulation.py` to generate database.
2. Run `analyze_packets.py` to analyze and plot results.

## Example Latency Distribution
[Latency Distribution](screenshots/latency_histogram.png)