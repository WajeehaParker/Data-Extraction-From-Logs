import pandas as pd
import Helpers

df = Helpers.process_log_file("./API Logs.log")
print(df)
