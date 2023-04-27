import random
import array
import datetime

# zapisanie tablicy do pliku oraz jej wczytanie
tab_of_floats = array.array('f', [random.random() for _ in range(1_000_000)])

start_time = datetime.datetime.now()
with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)

# wczytujemy ponownie dane do tablicy floatów
tab_of_floats_loaded = array.array('f')
file_arr  = open('floats_array.bin', 'rb')
tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
file_arr.close()
end_time = datetime.datetime.now()
print("Czas operacji zapisu i ładowania danych do tablicy: ", end_time - start_time)


# i analogiczna operacja dla listy
list_of_floats = [random.random() for _ in range(1_000_000)]
start_time = datetime.datetime.now()
with open('floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))

with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()

list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
end_time = datetime.datetime.now()
print("Czas operacji zapisu i ładowania danych do listy: ", end_time - start_time)