import csv
import zipfile
from io import TextIOWrapper


def merge_txt_from_zip_to_csv(zip_file_path, output_file):
    header_written = False

    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            for file_info in zip_file.infolist():
                if file_info.filename.endswith(".txt"):
                    with zip_file.open(file_info) as txt_file:
                        txt_file_wrapper = TextIOWrapper(txt_file, 'utf-8')
                        content = txt_file_wrapper.read().splitlines()

                        if not header_written:
                            writer.writerow(content[0].split(','))
                            header_written = True
                        for row in content[1:]:
                            row = row.split(',')
                            writer.writerow(row)

    print(f"Scalono pliki tekstowe z pliku ZIP do pliku CSV: {output_file}")


merge_txt_from_zip_to_csv("data_for_lab_10.zip", "merge_txt.csv")
