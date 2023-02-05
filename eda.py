from ydata_profiling import ProfileReport
import pandas as pd
df = pd.read_csv('data.csv')
profile = ProfileReport(df, minimal=True)
profile.to_file("bankruptcy_report.html")