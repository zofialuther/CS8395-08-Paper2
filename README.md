# Energy Consumption Analysis of Python Code Samples

This repository contains data and code for a project analyzing the energy consumption of Python code samples. The primary focus is to evaluate and compare the energy consumption of various Python scripts using the Mx Power Gadget for logging and Large Language Models (LLMs) for predictions.

## Repository Contents

- `PwrData_2023_11_30_at_11_12_27.csv`: This file contains the logging information collected from Mx Power Gadget, detailing the energy consumption of Python code samples during execution.
- `execution_times.csv`: Output of the `get_accurate_times.py` script. This file documents the start and end times for the execution of all programs included in the study.
- `README.md`: The file you are currently reading, providing an overview of the repository.
- `experiments.ipynb`: The main Jupyter notebook containing the experiments conducted in this study. It includes data analysis, visualization, and interpretation of results.
- `energy_comparison_results.csv`: Contains model prediction information comparing the energy consumption of two non-equivalent pieces of code.
- `get_accurate_times.py`: A Python script used to capture timestamp information for all program executions, aiding in accurate energy consumption measurement.
- `energy_comparison_results_paired.csv`: Includes model prediction information for comparisons between two functionally equivalent pieces of code.
- `slow_samples/`: A folder containing all the Python code samples that were analyzed in this project.

## Project Overview

The project aims to explore the energy consumption characteristics of Python code samples, utilizing both empirical data from Mx Power Gadget and predictive analysis using LLMs. The goal is to understand the energy efficiency of different coding implementations and to assess the LLMs' ability to predict energy consumption accurately.

## How to Use This Repository

To replicate the analysis or to conduct further research based on this work, follow these steps:

1. **Clone the Repository**:
   Clone this repository to your local machine to get started with the analysis.

2. **Install Dependencies**:
   Ensure you have Jupyter notebooks and other required Python libraries installed. You can do this by running `pip install jupyter pandas matplotlib` in your terminal.

3. **Explore the Data**:
   The `PwrData_2023_11_30_at_11_12_27.csv` and `execution_times.csv` files contain raw data about the energy consumption and execution times of the code samples.

4. **Run the Experiments**:
   Open `experiments.ipynb` in Jupyter Notebook or Jupyter Lab to view and run the experiments and analyses conducted in this study.

5. **Analyze the Results**:
   Review the results in `energy_comparison_results.csv` and `energy_comparison_results_paired.csv` for insights into the energy efficiency of different code samples and the accuracy of LLM predictions.

## Contributing

Contributions to this project are welcome. Please follow the standard procedures for contributing to open-source projects:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

## License

This project is open-sourced under the [MIT License](LICENSE).

## Contact

For any queries regarding this project, please open an issue in this repository.

---
*This README is subject to updates and changes as the project evolves.*
