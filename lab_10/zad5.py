import pandas as pd


def convert_date_format(file_name, date_column_index, source_format, target_format):
    try:
        df = pd.read_csv(file_name, sep=',')

        df.iloc[:, date_column_index] = pd.to_datetime(df.iloc[:, date_column_index], format=source_format).dt.strftime(
            target_format)

        new_file_name = f"converted_{file_name}"
        df.to_csv(new_file_name, index=False)

        print(f"Plik {new_file_name} został pomyślnie zapisany.")
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
    except Exception as e:
        print(f"Wystąpił błąd: {str(e)}")


convert_date_format("merge_txt.csv", 2, "%Y%m%d", "%Y-%m-%d")
