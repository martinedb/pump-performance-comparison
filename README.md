# Pump Performance Analysis Tool

This Python-based tool provides a comprehensive analysis of pump performance by comparing theoretical and experimental data across multiple key performance indicators. The tool generates detailed visualizations that help engineers and technicians evaluate pump performance characteristics.

## Overview

The tool consists of two Python scripts for analyzing pump performance:
- `theoretical-pump-performance.py`: Analyzes theoretical pump performance data using a single plot with multiple y-axes
- `pump-performance-comparison.py`: Compares theoretical and experimental data using a 2x2 grid of plots

## Key Performance Metrics Analyzed

### Theoretical Pump Performance Analysis
The `theoretical-pump-performance.py` script analyzes theoretical pump performance metrics:
1. Flow vs. Head (feet)
2. Flow vs. Bowl Power (bhp) at 1.0 specific gravity
3. Flow vs. NPSHR (feet)
4. Flow vs. Efficiency (%)

All metrics are plotted against flow rate in U.S. gallons per minute in a single plot with multiple y-axes.

### Experimental Data Comparison
The `pump-performance-comparison.py` script compares theoretical and experimental data for the same metrics using a 2x2 grid of plots.

## Data Sets

### Theoretical Data
- Flow range: 0-1424 U.S. gallons per minute
- Includes performance predictions for head, bowl power, NPSHR, and efficiency
- Data is structured in a pandas DataFrame for better analysis

### Experimental Data
- Contains actual measured performance data
- Used only in the pump-performance-comparison.py script

## Visualization

### Theoretical Pump Performance
The theoretical-pump-performance.py script generates a single plot with multiple y-axes, showing:
- Head (feet) in blue
- Bowl power (bhp) at 1.0 specific gravity in green
- NPSHR (feet) in red
- Efficiency (%) in yellow

Example visualization:

<img width="737" height="422" alt="image" src="https://github.com/user-attachments/assets/de993ac6-67f9-4a7a-913f-8e1cf92e51d1" />

### Experimental Data Comparison
The pump-performance-comparison.py script uses a 2x2 grid of plots to compare theoretical and experimental data:

<img width="1031" height="714" alt="image" src="https://github.com/user-attachments/assets/15fbb73e-908f-431d-9874-1a95d7be8652" />

Each plot includes:
- Blue markers and lines for theoretical data
- Red markers and lines for experimental data
- Grid lines for better readability
- Clear labels for axes and legends

## Requirements

To run this tool, you need:
- Python 3.x
- Matplotlib library (`matplotlib`)
- Pandas library (`pandas`) for the theoretical-pump-performance.py script

We recommend running this code in one of the following environments:
- Visual Studio Code with Python extension
- Windsurf IDE
- Anaconda distribution with Jupyter Notebook support

## Running the Code

1. Ensure you have Python 3.x installed on your system
2. Install the required dependency:
   ```bash
   pip install matplotlib
   ```
3. Run either of the Python files:
   ```bash
   python theoretical-pump-performance.py
   # or
   python pump-performance-comparison.py
   ```

## Notes About the Examples Shown With This Code

- The experimental data points show significantly higher flow rates than the theoretical data range
- Efficiency values in the experimental data are unusually high (over 100%), which may indicate potential data collection or measurement issues
- NPSHA values in the experimental data are negative, which is physically impossible and suggests potential measurement errors

## Disclaimer

This tool is intended for educational and analytical purposes. The experimental data can contain potential errors that should be investigated before making any engineering decisions based on these results.

