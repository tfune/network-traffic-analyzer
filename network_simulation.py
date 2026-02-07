import sqlite3
import random
import time

# Create Database
conn = sqlite3.connect("network_data.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS packets (
        packet_id INTEGER PRIMARY KEY,
        send_time REAL,
        receive_time REAL,
        latency REAL,
        dropped INTEGER
    )
""")

conn.commit()

# Simulate Network Packets
NUM_PACKETS = 1000

for i in range(NUM_PACKETS):
    send_time = time.time()

    dropped = 1 if random.random() < 0.05 else 0

    if dropped:
        receive_time = None
        latency = None

    else:
        latency = random.gauss(mu=25, sigma=5)
        receive_time = send_time + latency / 1000

    cursor.execute("""
        INSERT INTO packets (send_time, receive_time, latency, dropped)
        VALUES (?, ?, ?, ?)
    """, (send_time, receive_time, latency, dropped))

conn.commit()
conn.close()

print("Network simulation complete!")