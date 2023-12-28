import matplotlib.pyplot as plt

def get_type(a_str):
    try:
        int(a_str)
        return "int"
    except:
        try:
            float(a_str)
            return "float"
        except:
            return "str"

def read_csv(file_name, delimiter=','):
    data = []
    column_names = []
    column_types = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        

        # Extract column names
        column_names = lines[0].strip().split(delimiter)

        # Extract data and infer column types
        for line_num, line in enumerate(lines[1:], start=2):
            values = line.strip().split(delimiter)

            # Exception 1: Cek jumlah kolom konsisten
            if len(values) != len(column_names):
                raise Exception(f"Banyaknya kolom pada baris {line_num} tidak konsisten.")

            data.append(values)

            if not column_types:
                column_types = [get_type(value) for value in values]
        
        # Exception 2: Cek tabel kosong
        if not lines:
            raise Exception("Tabel tidak boleh kosong.")

    # Infer column types
    for col_index, col_type in enumerate(column_types):
        for row in data:
            cell_value = row[col_index]
            cell_type = get_type(cell_value)

            if col_type == "str":
                column_types[col_index] = "str"
            elif col_type == "int" and cell_type == "float":
                column_types[col_index] = "float"
            elif col_type == "int" and cell_type == "str":
                column_types[col_index] = "str"
            elif col_type == "float" and cell_type == "str":
                column_types[col_index] = "str"

    return (data, column_names, column_types)

def to_list(dataframe):
    return dataframe[0]

def get_column_names(dataframe):
    return dataframe[1]

def get_column_types(dataframe):
    return dataframe[2]

def head(dataframe, top_n=10):
    cols = get_column_names(dataframe)
    out_str = ""
    out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
    out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
    for row in to_list(dataframe)[:top_n]:
        out_str += "|".join([f"{col:>15}" for col in row]) + "\n"
    return out_str

def info(dataframe):
    col_names = get_column_names(dataframe)
    col_types = get_column_types(dataframe)

    out_str = f"Total Baris = {len(to_list(dataframe))} baris\n\n"
    out_str += "Kolom          Tipe\n"
    out_str += "---------------------\n"

    for col_name, col_type in zip(col_names, col_types):
        out_str += f"{col_name:<15} {col_type}\n"

    return out_str

def satisfy_cond(value1, condition, value2):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    value1 (tipe apapun yang comparable): nilai pertama
    condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    value2 (tipe apapun yang comparable): nilai kedua
    
    return (boolean): hasil perbandingan value1 dan value2
    
  """
  if condition == "<":
    return value1 < value2
  elif condition == "<=":
    return value1 <= value2
  elif condition == ">":
    return value1 > value2
  elif condition == ">=":
    return value1 >= value2
  elif condition == "!=":
    return value1 != value2
  elif condition == "==":
    return value1 == value2
  else:
    raise Exception(f"Operator {condition} tidak dikenal.")

def select_rows(dataframe, col_name, condition, value):
    """
    Mengembalikan dataframe baru dimana baris-baris sudah
    dipilih hanya yang nilai col_name memenuhi 'condition'
    terkait 'value' tertentu.
  
    Gunakan/Call fungsi satisfy_cond(value1, condition, value2) yang
    sudah didefinisikan sebelumnya!
  
    contoh:
    select_rows(dataframe, "umur", "<=", 50) akan mengembalikan
    dataframe baru dengan setiap baris memenuhi syarat merupakan
    item dengan kolom umur <= 50 tahun.
    
    Exceptions:
    1. jika col_name tidak ditemukan,
    
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
        
    2. jika condition bukan salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    
        raise Exception(f"Operator {condition} tidak dikenal.")
  
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom sebagai basis untuk selection
    condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    value (tipe apapun): nilai untuk basis perbandingan pada col_name
  
    return (list, list, list): dataframe baru hasil selection atau filtering
  
    """
    # Mengecek apakah col_name ada dalam dataframe
    if col_name not in get_column_names(dataframe):
        raise Exception(f"Kolom {col_name} tidak ditemukan.")

   
    
    selected_rows = []
    col_index = get_column_names(dataframe).index(col_name)
    for row in to_list(dataframe):
        if satisfy_cond(row[col_index], condition, value):
            selected_rows.append(row)
    return (selected_rows, get_column_names(dataframe), get_column_types(dataframe))

    # Mengecek apakah condition valid
    valid_conditions = ["<", "<=", "==", ">", ">=", "!="]
    if condition not in valid_conditions:
        raise Exception(f"Operator {condition} tidak dikenal.")


def select_cols(dataframe, selected_cols):
    """
    Mengembalikan dataframe baru dimana kolom-kolom sudah
    dipilih hanya yang terdapat pada 'selected_cols' saja.
    
    contoh:
    select_cols(dataframe, ["umur", "nama"]) akan mengembalikan
    dataframe baru yang hanya terdiri dari kolom "umur" dan "nama".
    
    Exceptions:
      1. jika ada nama kolom pada selected_cols yang tidak
         ditemukan, 
         
           raise Exception(f"Kolom {selected_col} tidak ditemukan.")
           
      2. jika select_cols adalah list kosong [],
      
           raise Exception("Parameter selected_cols tidak boleh kosong.")
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    selected_cols (list): list of strings, atau list yang berisi
                          daftar nama kolom
                          
    return (list, list, list): dataframe baru hasil selection pada
                               kolom, yaitu hanya mengandung kolom-
                               kolom pada selected_cols saja.
    
    """
   

    # Mengecek apakah setiap nama kolom pada selected_cols ada dalam dataframe
    for selected_col in selected_cols:
        if selected_col not in get_column_names(dataframe):
            raise Exception(f"Kolom {selected_col} tidak ditemukan.")

    selected_cols_indices = [get_column_names(dataframe).index(col) for col in selected_cols]
    selected_data = [[row[i] for i in selected_cols_indices] for row in to_list(dataframe)]
    return (selected_data, selected_cols, [get_column_types(dataframe)[i] for i in selected_cols_indices])

    # Mengecek apakah selected_cols adalah list kosong
    if not selected_cols:
        raise Exception(f"Parameter {selected_cols} tidak boleh kosong.")


def count(dataframe, col_name):
    """
    mengembalikan dictionary yang berisi frequency count dari
    setiap nilai unik pada kolom col_name.
    
    Tipe nilai pada col_name harus string !
    
    Exceptions:
      1. jika col_name tidak ditemukan,
      
           raise Exception(f"Kolom {col_name} tidak ditemukan.")
      
      2. jika tipe data col_name adalah numerik (int atau float),
      
           raise Exception(f"Kolom {col_name} harus bertipe string.")      
      
      3. jika tabel kosong, alias banyaknya baris = 0,
           
           raise Exception("Tabel kosong.")

    Peserta bisa menggunakan Set untuk mengerjakan fungsi ini.
           
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya
    
    return (dict): dictionary yang berisi informasi frequency count
                   dari setiap nilai unik.
    """
    # Mengecek apakah col_name ditemukan dalam dataframe
    if col_name not in get_column_names(dataframe):
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    
    col_index = get_column_names(dataframe).index(col_name)
    col_type = get_column_types(dataframe)[col_index]

    # Mengecek apakah tipe data col_name adalah string
    if col_type != 'str':
        raise Exception(f"Kolom {col_name} harus bertipe string.")

    # Mengecek apakah tabel kosong
    if not to_list(dataframe):
        raise Exception("Tabel kosong.")

    value_counts = {}
    for row in to_list(dataframe):
        value = row[col_index]
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    return value_counts


def mean_col(dataframe, col_name):
    """
    Mengembalikan nilai rata-rata nilai pada kolom 'col_name'
    di dataframe.
    
    Exceptions:
      1. jika col_name tidak ditemukan,
      
           raise Exception(f"Kolom {col_name} tidak ditemukan.")
      
      2. jika tipe data col_name adalah string,
      
           raise Exception(f"Kolom {col_name} bukan bertipe numerik.")      
      
      3. jika tabel kosong, alias banyaknya baris = 0,
           
           raise Exception("Tabel kosong.")
           
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya
    
    return (float): nilai rataan
    """
    # Mengecek apakah col_name ditemukan dalam dataframe
    if col_name not in get_column_names(dataframe):
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    
    col_index = get_column_names(dataframe).index(col_name)
    col_type = get_column_types(dataframe)[col_index]

    # Mengecek apakah tipe data col_name adalah string
    if col_type == 'str':
        raise Exception(f"Kolom {col_name} bukan bertipe numerik.")

    # Mengecek apakah tabel kosong
    if not to_list(dataframe):
        raise Exception("Tabel kosong.")

    values = [float(row[col_index]) for row in to_list(dataframe) if get_type(row[col_index]) != 'str']
    
    # Mengecek apakah nilai pada kolom dapat diubah menjadi angka
    if not values:
        raise Exception(f"Tidak ada nilai yang dapat diubah menjadi angka pada kolom {col_name}.")

    return sum(values) / len(values)


def show_scatter_plot(x, y, x_label, y_label):
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def scatter(dataframe, col_name_x, col_name_y):
    """
    fungsi ini akan menampilkan scatter plot antara kolom col_name_x
    dan col_name_y pada dataframe.
    
    pastikan nilai-nilai pada col_name_x dan col_name_y adalah angka!
    
    Exceptions:
      1. jika col_name_x tidak ditemukan,
      
           raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
           
      2. jika col_name_y tidak ditemukan,
      
           raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
           
      3. jika col_name_x BUKAN numerical,
      
           raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
           
      4. jika col_name_y BUKAN numerical,
      
           raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name_x (string): nama kolom yang nilai-nilainya diplot pada axis x
    col_name_y (string): nama kolom yang nilai-nilainya diplot pada axis y
    
    Call fungsi show_scatter_plot(x, y) ketika mendefinisikan fungsi
    ini!
    
    return None
    """
    # Mengecek apakah col_name_x ditemukan dalam dataframe
    if col_name_x not in get_column_names(dataframe):
        raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
    
    # Mengecek apakah col_name_y ditemukan dalam dataframe
    if col_name_y not in get_column_names(dataframe):
        raise Exception(f"Kolom {col_name_y} tidak ditemukan.")

    x_index = get_column_names(dataframe).index(col_name_x)
    
    # Mengecek apakah col_name_x bertipe numerik
    if get_column_types(dataframe)[x_index] == 'str':
        raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")

    y_index = get_column_names(dataframe).index(col_name_y)

    # Mengecek apakah col_name_y bertipe numerik
    if get_column_types(dataframe)[y_index] == 'str':
        raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")

    x_values = [float(row[x_index]) for row in to_list(dataframe) if get_type(row[x_index]) != 'str']
    y_values = [float(row[y_index]) for row in to_list(dataframe) if get_type(row[y_index]) != 'str']

    show_scatter_plot(x_values, y_values, col_name_x, col_name_y)

def total_rings_per_sex(dataframe):
    """
    Menghitung total 'rings' untuk setiap 'sex' yang ada dalam dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    
    return (dict): dictionary yang berisi informasi total 'rings' untuk setiap 'sex'
    """
    sex_index = get_column_names(dataframe).index("Sex")
    rings_index = get_column_names(dataframe).index("Rings")

    total_rings_per_sex_dict = {}

    for row in to_list(dataframe):
        sex = row[sex_index]
        rings = int(row[rings_index]) if get_type(row[rings_index]) == 'int' else 0

        if sex in total_rings_per_sex_dict:
            total_rings_per_sex_dict[sex] += rings
        else:
            total_rings_per_sex_dict[sex] = rings

    return total_rings_per_sex_dict

if __name__ == "__main__":
    # Baca file CSV Abalone
    file_name_abalone = "abalone.csv"
  
    dataframe = read_csv("abalone.csv")

    print("\n>>> Print the first 10 lines\n")
    print(head(dataframe, top_n=10))

    print("\n>>> Print dataframe information\n")
    print(info(dataframe))

    new_dataframe = select_rows(dataframe, "Length", ">", "0.49")
    print("\n>>> Return a new dataframe, with column Length > 0.49\n")
    print(head(new_dataframe, top_n=5))

    new_2nd_dataframe = select_rows(select_rows(dataframe, "Length", ">", "0.49"), "Sex", "==", "M")
    print("\n>>> Return a new dataframe, where Sex == 'M' AND Length > 0.49\n")
    print(head(new_2nd_dataframe, top_n=5))

    new_3rd_dataframe = select_cols(dataframe, ["Sex", "Length", "Diameter", "Rings"])
    print("\n>>> Return a new dataframe, only the Sex, Length, Diameter, and Rings columns\n")
    print(head(new_3rd_dataframe, top_n=5))

    print("\n>>> Calculate the mean in the Length column (in the original dataframe)\n")
    print(mean_col(dataframe, "Length"))

    print("\n>>> Unique values in the Sex column, and the frequency of their occurrence (in the original dataframe)\n")
    print(count(dataframe, "Sex"))

    print("\n>>> Display 'Height' and 'Diameter' column's scatter plot\n")
    scatter(dataframe, "Height", "Diameter")

    print("\n>>> Calculate total 'rings' for each 'sex' in the original dataframe\n")
    total_rings_result = total_rings_per_sex(dataframe)
    for sex, total_rings in total_rings_result.items():
        print(f"Sex '{sex}' memiliki total {total_rings} 'rings'")

