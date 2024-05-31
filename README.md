# Belladonna

## Overview

Belladonna is a project designed to visualize weather data. This README will guide you through the steps needed to run the `visualise.py` script, which plots temperature, humidity, and pressure data from a CSV file.

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- Python 3.6 or later
- `pandas` library
- `matplotlib` library

If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

## Installation

To install the necessary Python libraries, follow these steps:

1. Open your terminal or command prompt.
2. Install the required libraries by running the following commands:

```sh
pip install pandas matplotlib
```

## Running the Script

Once you have the prerequisites installed, follow these steps to run the `visualise.py` script:

1. Ensure your data file (`data.csv`) is in the same directory as `visualise.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory containing `visualise.py` and `data.csv`.
4. Run the script by executing the following command:

```sh
python visualise.py
```

This will generate a plot displaying temperature, humidity, and pressure data over time.

## Script Explanation

The `visualise.py` script performs the following steps:

1. **Load the Data**: Reads the weather data from `data.csv` using `pandas`.
2. **Preprocess the Data**: Combines the `date` and `time` columns into a single `datetime` column and sets it as the index.
3. **Plot the Data**: Creates a plot with three y-axes to display temperature, humidity, and pressure. Important events can be marked on the plot for reference.
4. **Display the Plot**: Shows the plot with proper labels, legends, and formatting.

### Example Data Format

Ensure your `data.csv` file follows this format:

| date       | time     | temperature | humidity | pressure |
|------------|----------|-------------|----------|----------|
| 2024-05-25 | 06:00:00 | 22.5        | 60       | 1012     |
| 2024-05-25 | 06:10:00 | 22.8        | 59       | 1012     |
| ...        | ...      | ...         | ...      | ...      |

The `date` and `time` columns should be in `YYYY-MM-DD` and `HH:MM:SS` format, respectively.

## Customizing the Script

You can customize the script to highlight specific events by adjusting the `event_datetime` variables. Uncomment and modify the `axvline` and `text` lines in the script to add vertical lines and labels at the specified event times.

```python
event_datetime = pd.to_datetime('2024-05-27 16:22:12')
# ax1.axvline(event_datetime, color='k', linestyle='--', label='Event 1')
# ax1.text(event_datetime, ax1.get_ylim()[1], 'Event 1', rotation=90, verticalalignment='center', color='k')
```

## Conclusion

By following these instructions, you should be able to visualize your weather data using the `visualise.py` script. Feel free to customize the script to suit your needs and explore the data further.