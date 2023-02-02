import csv  # to work with csv files

# reading a csv file
with open("names.csv", "r") as c_file:
    # creats an object with all the csv lines (note delimiter is a "," by default)
    csv_reader = csv.reader(c_file, delimiter=",")
    # csv_reader = csv.DictReader(c_file) # returns the lines as a dictionary

    # skips the first line in the csv (useless when using dictreader)
    next(csv_reader)

    for line in csv_reader:
        print(line)  # each line is a list with data
        # print(line["email"])  # gets all emails (if using dictReader)


with open("names.csv", "r") as c_file:
    csv_reader = csv.reader(c_file)  # creats an object with all the csv lines

    with open("new-name.csv", "w") as new_file:
        # allows us to write to the file and add custom delimiter
        csv_writer = csv.writer(new_file, delimiter="_")
        """
            The below code shows how to use the DictWriter instead:
            fieldnames = ["first_name", "last_name", "email"]
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="_")
            csv_writer.writeheader() # adds fieldnames to the top of the file
        """

        for line in csv_reader:
            # writes every line to the new file, but now uses a _ instead of , as delimiter
            csv_writer.writerow(line)
