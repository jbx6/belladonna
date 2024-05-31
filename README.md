# Belladonna

## Overview

Belladonna is a project designed to collect weather data (...more in the future). This README will guide you through the steps needed to run the `visualise.py` script, which plots temperature, humidity, and pressure data from a CSV file.

>I am specifically using a CSV file because I do not yet understand how to interact with a database, though I am trying. In my opinion, learning to write-to, and read-from a CSV might be a good 'stepping-stone' on my way to learning databases. When I say 'database', I am referring to something like MongoDB, which I frequently-note being used, discussed, referenced, etc. 

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- Python 3.6 or later
- `pandas` library
- `matplotlib` library

If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

## Installation

### Clone the Repository

1. Open your terminal or command prompt.
2. Clone the repository from GitHub:

```sh
git clone https://github.com/jbx6/belladonna.git
```

3. Navigate to the cloned repository directory:

```sh
cd belladonna
```

### Install Dependencies

To install the necessary Python libraries, run the following command:

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
python3 visualise.py
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

This README was written by [ChatGPT](https://openai.com/chatgpt/) (with some specific prompting)...