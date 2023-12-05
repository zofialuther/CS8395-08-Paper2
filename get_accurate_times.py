import os
import subprocess
import time
import csv
from datetime import datetime

def run_python_script(file_path):
    """Run a Python script and return the start and end times."""
    start_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]  # Format: HH:MM:SS.milliseconds
    subprocess.run(['python3', file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]
    return start_time, end_time

def main():
    samples_dir = 'slow_samples'  # Path to the 'slow_samples' directory
    output_csv = 'execution_times.csv'  # Output CSV file name

    with open(output_csv, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['File Name', 'Start Time', 'End Time'])

        for task in os.listdir(samples_dir):
            task_path = os.path.join(samples_dir, task)

            for file in os.listdir(task_path):
                if file.endswith('.py'):
                    file_path = os.path.join(task_path, file)
                    print(f"Running {file_path}...")
                    
                    start_time, end_time = run_python_script(file_path)
                    csv_writer.writerow([file_path, start_time, end_time])

                    print(f"Finished {file_path}. Sleeping for 4 seconds...")
                    time.sleep(4)

if __name__ == "__main__":
    main()
