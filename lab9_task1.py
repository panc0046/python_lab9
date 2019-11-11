import csv

# Read first file and write all data in csv file
boys_file=open("2000_BoysNames.txt","r")
#create new csv file
csv_file_boy = open("Names_Boys.csv","w")
write_csv = csv.writer(csv_file_boy)
write_csv.writerow(('First Name', 'Count'))

for lines in boys_file.readlines():
    stripped = lines.strip()
    new_line = stripped.replace(" ", ",")
    write_csv.writerow(new_line.split(","))
csv_file_boy.close()

# Read second file and write all data in csv
girls_file = open("2000_GirlsNames.txt","r")
csv_file_girls = open("Names_Girls.csv","w")
write_csv = csv.writer(csv_file_girls)
write_csv.writerow(('First Name', 'Count'))

for lines in girls_file.readlines():
    stripped = lines.strip()
    new_line = stripped.replace(" ", ",")
    write_csv.writerow(new_line.split(","))
csv_file_girls.close()
print("Write Both file sucessfully")

