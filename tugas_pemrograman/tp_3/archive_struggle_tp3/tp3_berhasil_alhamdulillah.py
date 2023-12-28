import matplotlib.pyplot as plt
def get_type(a_str):
  """
    Fungsi ini akan mengembalikan tipe dari literal
    string a_str.

    return (string): "int", "float", atau "str"

  """
  try:
    int(a_str)
    return "int"
  except ValueError:
    try:
      float(a_str)
      return "float"
    except:
      return "str"
    
def read_csv(file_name, delimiter = ','):
  """
  Fungsi ini bertugas untuk membaca sebuah file comma
  separated value, melakukan parsing, dan mengembalikan
  dataframe yang berupa 3-tuple.

  return (list, list, list): (data, list nama kolom, list tipe data)
  
  """
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

    return (list): list of lists of items

  """
  return dataframe[0]

def get_column_names(dataframe):
  """
    Dataframe[1] adalah berisi list of column names. Gunakan fungsi ini
    kedepannya jika ada keperluan untuk akses daftar nama kolom pada
    sebuah dataframe.

    return (list): list of column names
    
  """
  return dataframe[1]
  
def get_column_types(dataframe):
  """
    Dataframe[2] adalah berisi daftar tipe data dari
    setiap kolom tabel. Hanya ada tiga jenis tipe data,
    yaitu "str", "int", dan "float"

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

    return (string): representasi string dari penampilan tabel.
    
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
    Mengembalikan float berupa rata-rata nilai pada kolom 'col_name' di dataframe

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
    parameter:
    x (list): list of numerical values, tidak boleh string
    y (list): list of numerical values, tidak boleh string
    x_label (string): label pada sumbu x
    y_label (string): label pada sumbu y
    
    return None, namun fungsi ini akan menampilkan scatter
    plot dari nilai pada x dan y.
    
  """
  plt.scatter(x, y)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()

def scatter(dataframe, col_name_x, col_name_y):
    """
    fungsi ini akan menampilkan scatter plot antara kolom col_name_x
    dan col_name_y pada dataframe

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

dataframe = read_csv("abalone.csv")
# print(head(dataframe, top_n = 10))
# print(info(dataframe))
# new_dataframe = select_rows(dataframe, "Length", ">", 0.49)
# print(head(new_dataframe, top_n = 5))
# new_dataframe = select_rows(select_rows(dataframe, "Length",">", 0.49), "Sex", "==", "M")
# print(head(new_dataframe, top_n = 5))
# new_dataframe = select_cols(dataframe, ["Sex", "Length","Diameter", "Rings"])
# print(head(new_dataframe, top_n = 5))
# print(mean_col(dataframe, "Length"))
# print(count(dataframe, "Sex"))
# scatter(dataframe, "Length", "Diameter")