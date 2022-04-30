import csv
import pandas as pd

# Reading from csv and turn data into dictionary
reader = csv.reader(open('library.csv'))

result = {}
for row in reader:
    key = row[0]
    if key in result:
        # implement your duplicate row handling here
        pass
    result[key] = row[1:]
print(result)
print(result['BOOK2'][0])

    # with open('library_out.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows(lines)
        
# with open('library_out.csv', 'w', newline='') as csv_file:  
#     writer = csv.writer(csv_file)
#     writer.writerow(result.keys())
#     writer.writerows(zip(*result.values()))
#     # for key, value in result.items():
#     #    writer.writerow([key, value])

df = pd.DataFrame({key: pd.Series(value) for key, value in result.items()})
df2 = df.T
df2.to_csv('library_out.csv', encoding='utf-8', index=True)
