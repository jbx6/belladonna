import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data.csv')

# Convert the 'date' and 'time' columns to a single datetime column
data['datetime'] = pd.to_datetime(data['date'] + ' ' + data['time'])

# Set the datetime column as the index
data.set_index('datetime', inplace=True)

# Specify the datetime for the event (e.g., '2024-05-25 06:10:32')
event_datetime = pd.to_datetime('2024-05-27 16:22:12')
event_datetime_2 = pd.to_datetime('2024-05-25 07:02:37')
event_datetime_3 = pd.to_datetime('2024-05-25 07:21:59')
event_datetime_4 = pd.to_datetime('2024-05-25 08:09:00')

# Create a figure and axis for plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot temperature
ax1.plot(data.index, data['temperature'], 'r-', label='Temperature (°C)')
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature (°C)', color='r')
ax1.tick_params(axis='y', labelcolor='r')

# Create a second y-axis for humidity
ax2 = ax1.twinx()
ax2.plot(data.index, data['humidity'], 'b-', label='Humidity (%)')
ax2.set_ylabel('Humidity (%)', color='b')
ax2.tick_params(axis='y', labelcolor='b')

# Create a third y-axis for pressure
ax3 = ax1.twinx()
# Offset the right spine of ax3. The ticks and label have already been placed on the right by twinx above.
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(data.index, data['pressure'], 'g-', label='Pressure (hPa)')
ax3.set_ylabel('Pressure (hPa)', color='g')
ax3.tick_params(axis='y', labelcolor='g')

# Add the event line
# ax1.axvline(event_datetime, color='k', linestyle='--', label='WiFi dropped')
# ax1.text(event_datetime, ax1.get_ylim()[1], 'WiFi dropped', rotation=90, verticalalignment='center', color='k')

# Add legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1,0.9))

# Format the x-axis for better readability
plt.xticks(rotation=45)
plt.title('Temperature, Humidity, and Pressure Over Time')

plt.tight_layout()
plt.show()
