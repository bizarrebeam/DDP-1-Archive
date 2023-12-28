import matplotlib.pyplot as plt

def get_type(a_str):
  """
    Fungsi ini akan mengembalikan tipe dari literal
    string a_str.
    
    get_type("0.5") -> "float"
    get_type("5.") -> "float"
    get_type("5") -> "int"
    get_type("5.a") -> "str"
    
    parameter:
    a_str (string): string literal dari sebuah nilai
    
    return (string): "int", "float", atau "str"
  """
  try:
    int(a_str)
    return "int"
  except:
    try:
      float(a_str)
      return "float"
    except:
      return "str"
    
def read_csv(file_name, delimiter = ','):
  data = []
  line_count = 0

  try:
    with open(file_name, "r") as file:
      col_names = None
      col_types = None
      for line_count, line in enumerate(file, start=1):
        contents = line.strip().split(delimiter)

        if line_count == 1:  # header line
          if not contents:
              raise Exception(f"Header pada baris {line_count} tidak boleh kosong.")
          
          col_names = contents
          col_types = ['str'] * len(contents)  # header is all str

        else:
          if len(contents) != len(col_names):
            raise Exception(f"Banyaknya kolom pada baris {line_count} tidak konsisten.")

            # updating column types
          for i, content in enumerate(contents):
            col_type = get_type(content)

            if col_type == "int":
              col_types[i] = "int"
            elif col_type == "float" and (col_types[i] != "int" and col_types[i] != "float"):
              col_types[i] = "float"
            elif col_type == "str" and col_types[i] != "int" and col_types[i] != "float":
              col_types[i] = "str"

          data.append(contents)

    if line_count == 0:
      raise Exception("Tabel tidak boleh kosong.")

    return data, col_names, col_types

  except FileNotFoundError:
    raise Exception(f"File {file_name} tidak ditemukan.")
  except Exception as e:
    raise e
  
def to_list(dataframe):
  """
    Mengembalikan bagian list of lists of items atau tabel data
    pada dataframe. Gunakan fungsi ini kedepannya jika ada keperluan
    untuk akses bagian data/tabel pada dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of lists of items
  """
  return dataframe[0]

def get_column_names(dataframe):
  """
    Dataframe[1] adalah berisi list of column names. Gunakan fungsi ini
    kedepannya jika ada keperluan untuk akses daftar nama kolom pada
    sebuah dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of column names
  """
  return dataframe[1]
  
def get_column_types(dataframe):
  """
    Dataframe[2] adalah berisi daftar tipe data dari
    setiap kolom tabel. Hanya ada tiga jenis tipe data,
    yaitu "str", "int", dan "float"
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of type names
  """
  return dataframe[2]

def head(dataframe, top_n = 10):
  """
    top_n baris pertama pada tabel!
  
    Mengembalikan string yang merupakan representasi tabel
    (top_n baris pertama) dengan format:
    
     kolom_1|     kolom_2|     kolom_3|     ...
    ------------------------------------------- 
    value_11|    value_12|    value_13|     ...
    value_21|    value_22|    value_23|     ...
    ...         ...         ...
    
    Space setiap kolom dibatasi hanya 15 karakter dan right-justified.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    top_n (int): n, untuk penampilan top-n baris saja
    
    return (string): representasi string dari penampilan tabel.
    
    Jangan pakai print()! tetapi return string!
  """
  cols = get_column_names(dataframe)
  out_str = ""
  out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
  out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"

  for row in to_list(dataframe)[:top_n]:
    out_str += "|".join([f"{col:>15}" for col in row]) + "\n"
  return out_str
  
def info(dataframe):
  """
    Mengembalikan string yang merupakan representasi informasi
    dataframe dalam format:
    
    Total Baris = xxxxx baris
    
    Kolom          Tipe
    ------------------------------
    kolom_1        tipe_1
    kolom_2        tipe_2
    ...
    
    Space untuk kolom dan tipe adalah 15 karakter, left-justified
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    
    return (string): representasi string dari info dataframe    
  """
  total_rows = len(to_list(dataframe))
  col_names = get_column_names(dataframe)
  col_types = get_column_types(dataframe)

  str_info = f"Total Baris = {total_rows} baris\n\n"
  str_info += f"{'Kolom': <15}{'Tipe': <15}\n"
  str_info += "-" *30 + "\n"

  for col_name, col_type in zip(col_names, col_types):
    str_info += f"{col_name: <15}{col_type: <15}\n"
  
  return str_info

def satisfy_cond(value1, condition, value2):
  """
    parameter:
    value1 (tipe apapun yang comparable): nilai pertama
    condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    value2 (tipe apapun yang comparable): nilai kedua
    
    return (boolean): hasil perbandingan value1 dan value2
    
  """
  value1 = type(value2)(value1)

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
  if col_name not in dataframe[1]:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  conditions = ["<", "<=", "==", ">", ">=", "!="]
  if condition not in conditions:
    raise Exception(f"Operator {condition} tidak dikenal.")
  
  index_col = dataframe[1].index(col_name)
  selected_rows = [row for row in to_list(dataframe) if satisfy_cond(row[index_col], condition, value)]
  new_dataframe = (selected_rows, dataframe[1], dataframe[2])

  return new_dataframe

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
  if not selected_cols:
    raise Exception("Parameter selected_cols tidak boleh kosong.")
  
  col_names = get_column_names(dataframe)

  for selected_col in selected_cols:
    if selected_col not in col_names:
      raise Exception(f"Kolom {selected_col} tidak ditemukan.")

  selected_index = [col_names.index(col) for col in selected_cols]
  new_data = [[row[i] for i in selected_index] for row in to_list(dataframe)]

  new_columns = [col_names[i] for i in selected_index]
  new_types = [get_column_types(dataframe)[i] for i in selected_index]

  return (new_data, new_columns, new_types)


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
  if col_name not in get_column_names(dataframe):
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  if "str" not in get_column_types(dataframe)[get_column_names(dataframe).index(col_name)]:
    raise Exception(f"Kolom {col_name} harus bertipe string.")
  
  if len(to_list(dataframe)) == 0:
    raise Exception("Tabel kosong.")
  
  unique_values = set(row[get_column_names(dataframe).index(col_name)] for row in to_list(dataframe))
  frequency_count = {value: 0 for value in unique_values}

  for row in to_list(dataframe):
    value = row[get_column_names(dataframe).index(col_name)]
    frequency_count[value] += 1
  
  return frequency_count

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
  if col_name not in get_column_names(dataframe):
    raise Exception(f"Kolom {col_name} tidak ditemukan.")

  col_type = get_column_types(dataframe)[get_column_names(dataframe).index(col_name)]
    
  if col_type != "int" and col_type != "float":
    raise Exception(f"Kolom {col_name} bukan bertipe numerik.")

  if len(to_list(dataframe)) == 0:
    raise Exception("Tabel kosong.")

  index_col = get_column_names(dataframe).index(col_name)
  values = [float(row[index_col]) for row in to_list(dataframe)]

  return sum(values) / len(values)

  
def show_scatter_plot(x, y, x_label, y_label):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    x (list): list of numerical values, tidak boleh string
    y (list): list of numerical values, tidak boleh string
    x_label (string): label pada sumbu x
    y_label (string): label pada sumbu y
    
    return None, namun fungsi ini akan menampilkan scatter
    plot dari nilai pada x dan y.
    
    Apa itu scatter plot?
    https://chartio.com/learn/charts/what-is-a-scatter-plot/
  """
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
  if col_name_x not in get_column_names(dataframe):
    raise Exception(f"Kolom {col_name_x} tidak ditemukan.")

  if col_name_y not in get_column_names(dataframe):
    raise Exception(f"Kolom {col_name_y} tidak ditemukan.")

  col_type_x = get_column_types(dataframe)[get_column_names(dataframe).index(col_name_x)]
  col_type_y = get_column_types(dataframe)[get_column_names(dataframe).index(col_name_y)]

  if col_type_x not in ["int", "float"]:
    raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")

  if col_type_y not in ["int", "float"]:
    raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")

  x_index = get_column_names(dataframe).index(col_name_x)
  y_index = get_column_names(dataframe).index(col_name_y)

  x_values = [float(row[x_index]) for row in to_list(dataframe)]
  y_values = [float(row[y_index]) for row in to_list(dataframe)]

  x_label = col_name_x
  y_label = col_name_y

  show_scatter_plot(x_values, y_values, x_label, y_label)

if __name__ == "__main__":
  file_name = "abalone.csv"

  # Load data from CSV file
  dataframe, col_names, col_types = read_csv(file_name)

  # Display information about the dataframe
  print(info((to_list(dataframe), col_names, col_types)))

  # Display the first 10 rows of the dataframe
  print(head((to_list(dataframe), col_names, col_types)))

  # Create a scatter plot
  scatter(dataframe, "Length", "Diameter")

  # Example of selecting rows based on a condition
  selected_dataframe = select_rows(dataframe, "Length", ">", 10)
  print(head(selected_dataframe))

  # Example of selecting specific columns
  selected_cols_dataframe = select_cols(dataframe, ["Length", "Diameter"])
  print(head(selected_cols_dataframe))

  # Example of counting unique values in a column
  count_result = count(dataframe, "Type")
  print(count_result)

  # Example of calculating the mean of a numerical column
  mean_value = mean_col(dataframe, "Length")
  print(mean_value)
  