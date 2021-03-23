import sys
import csv
import scraper

if __name__ == "__main__":
    source_filename = sys.argv[1]
    destination_filename = sys.argv[2]
    word_column = int(sys.argv[3])
    definition_column = int(sys.argv[4])
    with open(source_filename, "r") as source_file:
        with open(destination_filename, "w") as destination_file:
            source = csv.reader(source_file, delimiter="\t")
            destination = csv.writer(destination_file, delimiter="\t")
            for row in source:
                row[definition_column] = scraper.generate_definition(row[word_column])
                print(row[word_column])
                destination.writerow(row)
