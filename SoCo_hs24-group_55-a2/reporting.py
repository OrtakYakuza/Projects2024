import csv
from datetime import datetime

def reporting_all(file_path):
    data = {}

    with open(file_path, 'r') as f:
        reader = csv.reader(f) #shows file in csv form for the row based format we need in our tracing
        start_times = {}

        for row in reader:
            id, timestamp, function_name, event_type = row
            timestamp_ms = int(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f').timestamp() * 1000)
            #datetime.strptime coverts string of timestamp to datetime obejct with requested format, timestamp coverts this to second and * 1000 to ms used ai + python library to figure this out

            if function_name not in data:
                data[function_name] = {"calls": 0, "total_time": 0.0}

            if event_type == "start":
                start_times[id] = timestamp_ms
            elif event_type == "stop":
                start_time = start_times.pop(id)
                if start_time:
                    duration = timestamp_ms - start_time
                    data[function_name]["total_time"] += duration
                    data[function_name]["calls"] += 1

    
    report_data = []
    for function_name, call_time in data.items():
        calls = call_time["calls"]
        total_time = call_time["total_time"]
        if 0 < calls:
            average_time = total_time / calls
        else:
            average_time = 0
        report_data.append((function_name, calls, total_time, average_time))

    return report_data
    

def display_report(report_data):
    header = "| Function Name | Num. of calls | Total Time (ms) | Average Time (ms) |"
    separator = "-" * len(header)
    print(header)
    print(separator)

    for entry in report_data:
        function_name, calls, total_time, average_time = entry
        #print() the result here not finished

    print(separator)