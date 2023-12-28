import matplotlib.pyplot as plt

def get_type(a_str):                                                                                    
  """
    (Defined) Fungsi ini akan mengembalikan tipe dari literal
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
  data = []                                                                                # The first element of tuple is a list of list
  line_count = 0                                                                           # Track each line of the file

  try:
    with open(file_name, "r") as file:
      col_names = None                                                                     # Track the second element of the tuple
      col_types = None                                                                     # Track the third element of the tuple

      for line_count, line in enumerate(file, start=1):                                    # Start tracking from line 1
        contents = line.strip().split(delimiter)                                           # Get the value from the separated coma

        if line_count == 1:                                                                # The first line is guaranteed to be a header
          col_names = contents                                                             # Get the column (header) name for the 2nd element of tuple
          col_types = ['str'] * len(contents)                                              # The number of columns == len of header are a string

        else:
          if len(contents) != len(col_names):                                              # If the data's len ain't the same with the num of columns
            raise Exception(
              f"Banyaknya kolom pada baris {line_count} tidak konsisten.")
          if not contents:                                                                 # If the line doesn't contain any value (blank)
            raise Exception(f"Tabel pada baris {line_count} tidak boleh kosong.")
            
          for i, content in enumerate(contents):                                           # Check each value type in the line 
            col_type = get_type(content)                                                     # by calling functions defined beforehand

            if col_type == "int":                                                          # Determine the value for the 3rd element of tuple                                       
              col_types[i] = "int"
            elif col_type == "float":       
              col_types[i] = "float"
            elif col_type == "str":
              col_types[i] = "str"

          data.append(contents)                                                            # Get the data for the 1st element of tuple

    if line_count == 0:                                                                    # In case the program can't find any line from the beginning
      raise Exception("Tabel tidak boleh kosong.")

    return data, col_names, col_types                                                      # Return the tup le

  except Exception as e:                                                                   # Handle exception in opening the file                                                           
    raise e
  
def to_list(dataframe):
  """
    (Defined) Mengembalikan bagian list of lists of items atau tabel data
    pada dataframe. Gunakan fungsi ini kedepannya jika ada keperluan
    untuk akses bagian data/tabel pada dataframe.

    return (list): list of lists of items

  """
  return dataframe[0]

def get_column_names(dataframe):
  """
    (Defined) Dataframe[1] adalah berisi list of column names. Gunakan fungsi ini
    kedepannya jika ada keperluan untuk akses daftar nama kolom pada
    sebuah dataframe.

    return (list): list of column names
    
  """
  return dataframe[1]
  
def get_column_types(dataframe):
  """
    (Defined)Dataframe[2] adalah berisi daftar tipe data dari
    setiap kolom tabel. Hanya ada tiga jenis tipe data,
    yaitu "str", "int", dan "float"

    return (list): list of type names
    
  """
  return dataframe[2]

def head(dataframe, top_n = 10):
  """
    (Defined) top_n baris pertama pada tabel!
  
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
  total_rows = len(to_list(dataframe))                                                   # Total row is the same len as the 1st element of tuple
  col_names = get_column_names(dataframe)                                                # Get the 2nd element of tuple
  col_types = get_column_types(dataframe)                                                # Get the 3rd element of tuple

  str_info = f"Total Baris = {total_rows} baris\n\n"                                     # First line info                    
  str_info += f"{'Kolom': <15}{'Tipe': <15}\n"                                           # Header configuration
  str_info += "-" *30 + "\n"

  for col_name, col_type in zip(col_names, col_types):                                   # Iterate over two list and paired it correspondingly
    str_info += f"{col_name: <15}{col_type: <15}\n"                                      # Each line configuration
  
  return str_info


def satisfy_cond(value1, condition, value2):
  """
    (Defined) parameter:
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
  if col_name not in dataframe[1]:                                                          # Proceed only existing data
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  conditions = ["<", "<=", "==", ">", ">=", "!="]                                           # Proceed only valid operators
  if condition not in conditions:
    raise Exception(f"Operator {condition} tidak dikenal.")
  
  index_col = dataframe[1].index(col_name)                                                  # Check the particular data of desired row
  selected_rows = [
     row for row in to_list(dataframe) if satisfy_cond(row[index_col], condition, value)    # Perform matching operations
     ] 
  new_dataframe = (selected_rows, dataframe[1], dataframe[2])                            

  return new_dataframe                                                                      # Return a new tuple with selected 1st element of tuple

def select_rows_advanced(dataframe, conditions, order_by=None, ascending=True):
    """
    (Extra) Mengembalikan dataframe baru dimana baris-baris sudah
    dipilih berdasarkan beberapa kondisi yang diberikan.
    
    Parameters:
    - dataframe (tuple): DataFrame yang ingin difilter.
    - conditions (list of dict): List berisi kondisi-kondisi untuk filtering.
    - order_by (str or list): Nama kolom atau list nama kolom untuk sorting.
    - ascending (bool): True jika ascending, False jika descending.
    
    return (list, list, list): DataFrame baru hasil seleksi atau filtering.
    """
    for condition in conditions:                                                         # Get the value from the dict key given as argument
        col_name = condition.get("col_name")
        operator = condition.get("operator")
        value = condition.get("value")

        if col_name not in dataframe[1]:                                                 # Proceed only existing col_name
            raise Exception(f"Kolom {col_name} tidak ditemukan.")

        conditions_list = ["<", "<=", "==", ">", ">=", "!="]                             # Proceed only valid operator
        if operator not in conditions_list:
            raise Exception(f"Operator {operator} tidak dikenal.")

    selected_rows = []                                                                   # Initialize list for the 1st element of the dataframe tuple

    for row in to_list(dataframe):
        criteria = all(                                                                  
            satisfy_cond(row[dataframe[1].index(cond["col_name"])], cond["operator"], cond["value"])
            for cond in conditions
        )

        if criteria:                                                                     # Select specific criteria passed as an argument
            selected_rows.append(row)

    for col_name in order_by:
        index_order_by = dataframe[1].index(col_name)
        selected_rows.sort(key=lambda x: x[index_order_by], reverse=not ascending)       # Perform sorting (key, reverse). Set reverse in contrast with argument

    new_dataframe = (selected_rows, dataframe[1], dataframe[2])                          # Update the 1st element of the tuple
    return new_dataframe

def select_cols(dataframe, selected_cols):
  """
  Mengembalikan dataframe baru dimana kolom-kolom sudah
  dipilih hanya yang terdapat pada 'selected_cols' saja.
                        
  return (list, list, list): dataframe baru hasil selection pada
                            kolom, yaitu hanya mengandung kolom-
                            kolom pada selected_cols saja.
  
"""
  if not selected_cols:                                                                 # If select_cols is an empty list
    raise Exception("Parameter selected_cols tidak boleh kosong.")
  
  col_names = get_column_names(dataframe)                                               # Get the 2nd element of the tuple

  for selected_col in selected_cols:                                                    # If the element of selected cols aren't exist
    if selected_col not in col_names:
      raise Exception(f"Kolom {selected_col} tidak ditemukan.")

  selected_index = [col_names.index(col) for col in selected_cols]                      # Get the index of each selected colls in the list
  new_data = [[row[i] for i in selected_index] for row in to_list(dataframe)]           # Get the data from the selected colls

  new_columns = [col_names[i] for i in selected_index]                                  # Get the column names (2nd element of tuple)
  new_types = [get_column_types(dataframe)[i] for i in selected_index]                    # for the new selected colls

  return (new_data, new_columns, new_types)

def count(dataframe, col_name):
  """
    mengembalikan dictionary yang berisi frequency count dari
    setiap nilai unik pada kolom col_name.
    
    return (dict): dictionary yang berisi informasi frequency count
                   dari setiap nilai unik.

  """
  if col_name not in get_column_names(dataframe):                                      # Proceed only existing column name (2nd element of tuple)
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  if "str" not in get_column_types(dataframe)[get_column_names(dataframe).index(col_name)]: # Proceed only str datatype
    raise Exception(f"Kolom {col_name} harus bertipe string.")
  
  if len(to_list(dataframe)) == 0:                                                      # Proceed only line that contain value
    raise Exception("Tabel kosong.")
  
  unique_values = set(row[get_column_names(dataframe).index(col_name)] for row in to_list(dataframe)) # Get the unique array from data 
  frequency_count = {value: 0 for value in unique_values}                               # Initialize the dictionary--col_name as key, value is the count

  for row in to_list(dataframe):
    value = row[get_column_names(dataframe).index(col_name)]                            # Get the col_name value
    frequency_count[value] += 1                                                         # Increment the count for value matched
  
  return frequency_count

def mean_col(dataframe, col_name):
    """
    Mengembalikan float berupa rata-rata nilai pada kolom 'col_name' di dataframe

    return (float): nilai rataan

    """
    if col_name not in get_column_names(dataframe):                                    # If the col_name can't be found
        raise Exception(f"Kolom {col_name} tidak ditemukan.")

    col_type = get_column_types(dataframe)[get_column_names(dataframe).index(col_name)] # Get the type for the specific value of col_name
    
    if col_type != "int" and col_type != "float":                                      # If the type isn't a numeric
        raise Exception(f"Kolom {col_name} bukan bertipe numerik.")

    if len(to_list(dataframe)) == 0:                                                   # If len of the lines == 0
        raise Exception("Tabel kosong.")

    index_col = get_column_names(dataframe).index(col_name)                            # Get the values of specific col_name to calculate             
    values = [float(row[index_col]) for row in to_list(dataframe)]                      # convert it into float                 

    return sum(values) / len(values)                                                   # Return the mean calculation

def show_scatter_plot(x, y, x_label, y_label):
  """
    (Defined) parameter:
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
  
    if col_name_x not in get_column_names(dataframe):                                 # If the col_name can't be found
        raise Exception(f"Kolom {col_name_x} tidak ditemukan.")

    if col_name_y not in get_column_names(dataframe):                                 # If the col_name can't be found
        raise Exception(f"Kolom {col_name_y} tidak ditemukan.")

    col_type_x = get_column_types(dataframe)[get_column_names(dataframe).index(col_name_x)] # Get the specific type
    col_type_y = get_column_types(dataframe)[get_column_names(dataframe).index(col_name_y)] # Get the specific type

    if col_type_x not in ["int", "float"]:                                            # Works only on numerical value
        raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")

    if col_type_y not in ["int", "float"]:                                            # Works only on numerical value
        raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")

    x_index = get_column_names(dataframe).index(col_name_x)                           # Get the specific value from the 1st element of tuple
    y_index = get_column_names(dataframe).index(col_name_y)                           # Get the specific value from the 1st element of tuple

    x_values = [float(row[x_index]) for row in to_list(dataframe)]                    # Convert it into float for plotting
    y_values = [float(row[y_index]) for row in to_list(dataframe)]                    # Convert it into float for plotting

    x_label = col_name_x                                                              # Use col_name_x that has been validated
    y_label = col_name_y                                                              # Use col_name_y that has been validated

    show_scatter_plot(x_values, y_values, x_label, y_label) 


if __name__ == "__main__":
    
    dataframe = read_csv("abalone.csv")

    print("\n>>> Print the first 10 lines\n")
    print(head(dataframe, top_n=10))

    print("\n>>> Print dataframe information\n")
    print(info(dataframe))

    new_dataframe = select_rows(dataframe, "Length", ">", 0.49)
    print("\n>>> Return a new dataframe, with column Length > 0.49\n")
    print(head(new_dataframe, top_n=5))

    new_2nd_dataframe = select_rows(select_rows(dataframe, "Length", ">", 0.49), "Sex", "==", "M")
    print("\n>>> Return a new dataframe, where Sex == 'M' AND Length > 0.49\n")
    print(head(new_2nd_dataframe, top_n=5))

    new_3rd_dataframe = select_cols(dataframe, ["Sex", "Length", "Diameter", "Rings"])
    print("\n>>> Return a new dataframe, only the Sex, Length, Diameter, and Rings columns\n")
    print(head(new_3rd_dataframe, top_n=5))

    conditions = [
    {"col_name": "Length", "operator": ">", "value": 0.45},
    {"col_name": "Sex", "operator": "==", "value": "I"},
    {"col_name": "Diameter", "operator": "<=", "value": 0.75}
    ]
   
    new_4th_dataframe = select_rows_advanced(dataframe, conditions, order_by = ["Length", "Diameter", "Viscera_weight"], ascending=False)
    print("\n>>> Return a new dataframe with multiple conditions for Length, Sex, and Diameter, and in descending order\n")
    print(head(new_4th_dataframe, top_n=7))

    print("\n>>> Calculate the mean in the Length column (in the original dataframe)\n")
    print(mean_col(dataframe, "Length"))

    print("\n>>> Unique values in the Sex column, and the frequency of their occurrence (in the original dataframe)\n")
    print(count(dataframe, "Sex"))

    print("\n>>> Display 'Height' and 'Diameter' column's scatter plot\n")
    scatter(dataframe,"Length", "Diameter")

