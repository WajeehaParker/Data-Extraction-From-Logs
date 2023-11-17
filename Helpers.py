import pandas as pd

def process_log_file(file_path):
    date, time, sSitename, sComputername, sIp, csMethod, csUriStem, csUriQuery, sPort, csUsername, cIp = [], [], [], [], [], [], [], [], [], [], []
    csVersion, csUserAgent, csCookie, csReferer, csHost, scStatus, scSubstatus, scWin32Status, scBytes, csBytes, timeTaken = [], [], [], [], [], [], [], [], [], [], []
    data = []

    with open(file_path, "r") as file:
        for line in file:

            if line.startswith('#'):
                continue
            
            log_parts = line.split()

            data.append({
                'date': log_parts[0],
                'time': log_parts[1],
                'sSitename': log_parts[2],
                'sComputername': log_parts[3],
                'sIp': log_parts[4],
                'csMethod': log_parts[5],
                'csUriStem': log_parts[6],
                'csUriQuery': log_parts[7],
                'sPort': log_parts[8],
                'csUsername': log_parts[9],
                'cIp': log_parts[10],
                'csVersion': log_parts[11],
                'csUserAgent': log_parts[12],
                'csCookie': log_parts[13],
                'csReferer': log_parts[14],
                'csHost': log_parts[15],
                'scStatus': log_parts[16],
                'scSubstatus': log_parts[17],
                'scWin32Status': log_parts[18],
                'scBytes': log_parts[19],
                'csBytes': log_parts[20],
                'timeTaken': log_parts[21]
            })

    df = pd.DataFrame(data)
    
    return df
            