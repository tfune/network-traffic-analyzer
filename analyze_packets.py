import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("network_data.db")
cursor = conn.cursor()

# Calculate Average Latency of Successful Packets
cursor.execute("""
    SELECT AVG(latency)
    FROM packets
    WHERE dropped = 0
""")
avg_latency = cursor.fetchone()[0]

print("Average latency (ms):", avg_latency)

# Calculate Packet Loss Rate
cursor.execute("""
    SELECT COUNT(*)
    FROM packets
    WHERE dropped = 1
""")
dropped_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM packets")
total_count = cursor.fetchone()[0]

packet_loss_rate = dropped_count / total_count
print("Packet loss rate:", packet_loss_rate)

# Plot Latency Distribution
cursor.execute("""
    SELECT latency
    FROM packets
    WHERE dropped = 0
""")
latencies = [row[0] for row in cursor.fetchall()]

plt.hist(latencies, bins = 20, color='blue', edgecolor='black')
plt.title("Network Latency Distribution")
plt.xlabel("Latency (ms)")
plt.ylabel("Number of Packets")
plt.show()

conn.close()