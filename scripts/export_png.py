import matplotlib.pyplot as plt
import numpy as np

# Data
clients = [10, 50, 100, 250, 500]
pgbouncer_tps = [13338, 64094, 84693, 87775, 80141]
pgbouncer_latency = [0.739, 0.724, 1.020, 2.522, 4.576]
pgcat_tps = [17575, 66189, 91645, 90213, 105941]
pgcat_latency = [0.558, 0.691, 0.912, 1.974, 2.941]

# Create figure and axis objects with subplots()
fig, ax1 = plt.subplots(figsize=(12,8))
ax2 = ax1.twinx()

# Plot TPS data on the first y-axis
ax1.plot(clients, pgbouncer_tps, color='blue', marker='o', linestyle='-', label='PgBouncer TPS')
ax1.plot(clients, pgcat_tps, color='green', marker='s', linestyle='-', label='PgCat TPS')
ax1.set_xlabel('Number of Clients')
ax1.set_ylabel('Transactions per Second (TPS)')
ax1.tick_params(axis='y', labelcolor='black')

# Plot Latency data on the second y-axis
ax2.plot(clients, pgbouncer_latency, color='red', marker='^', linestyle='--', label='PgBouncer Latency')
ax2.plot(clients, pgcat_latency, color='orange', marker='d', linestyle='--', label='PgCat Latency')
ax2.set_ylabel('Latency (ms)')
ax2.tick_params(axis='y', labelcolor='black')

# Set x-axis to logarithmic scale for better visualization
ax1.set_xscale('log')
ax1.set_xticks(clients)
ax1.get_xaxis().set_major_formatter(plt.ScalarFormatter())

# Add legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Add title
plt.title('PgBouncer vs PgCat: TPS and Latency Comparison', fontsize=16)

# Add grid for better readability
ax1.grid(True, which="both", ls="-", alpha=0.2)

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('pooler_comparison_chart_03.png', dpi=300, bbox_inches='tight')
plt.close()

print("Chart has been saved as 'pooler_comparison_chart_03.png'")
