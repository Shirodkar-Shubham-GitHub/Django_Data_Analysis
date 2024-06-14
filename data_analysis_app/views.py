import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
from django.shortcuts import render
import io
import base64
from .forms import UploadFileForm

def analyze_csv(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                uploaded_file = form.save()
                df = pd.read_csv(uploaded_file.csv_file)
                
                first_few_rows = df.head()
                
                mean = df.mean()
                median = df.median()
                std = df.std()
                
                missing_values = df.isnull().sum()

                numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
                plot_data = {}
                for column in numerical_columns:
                    plt.figure()
                    df[column].hist(edgecolor='black', log=True)
                    plt.title(f'Histogram of {column}')
                    plt.xlabel(column)
                    plt.ylabel('Frequency')

                    buffer = io.BytesIO()
                    plt.savefig(buffer, format='png')
                    buffer.seek(0)
                    plot_data[column] = base64.b64encode(buffer.read()).decode('utf-8')
                    plt.close()
                
                return render(request, 'analysis_results.html', {
                    'first_few_rows': first_few_rows,
                    'mean': mean,
                    'median':median,
                    'std':std,
                    'missing_values': missing_values,
                    'plot_data':plot_data
                })
            except Exception:
                return render(request, 'error.html')
        
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})
