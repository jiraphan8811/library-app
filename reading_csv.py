import pandas
df = pandas.read_csv('library.csv')
print(df)


# # print(type(df['Book name'][0]))
# import csv

# with open('library.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(row)
#             # print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(row)
#             line_count += 1
#     print(f'Processed {line_count} lines.')
#     print(type(csv_reader))