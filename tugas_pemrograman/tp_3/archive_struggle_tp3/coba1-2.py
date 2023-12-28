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
        contents = line.strip().split(delimiter)                                           # Get the list of string from the separated coma

        if line_count == 1:                                                                # The first line is guaranteed to be a header
          col_names = contents                                                             # Get the column (header) name for the 2nd element of tuple
          col_types = ['str'] * len(contents)                                              # The number of columns == len of header, a list of string 'str'

        else:
          if len(contents) != len(col_names):                                              # If the data's len ain't the same with the num of columns
            raise Exception(
              f"Banyaknya kolom pada baris {line_count + 1} tidak konsisten.")
          if not contents:                                                                 # If the line doesn't contain any value (blank)
            raise Exception(f"Tabel pada baris {line_count + 1} tidak boleh kosong.")
            
          for i, content in enumerate(contents):                                           # Check each value type in the line 
            col_type = get_type(content)                                                     # by calling functions defined beforehand

            if col_type == "int":                                                          # Determine the value for the 3rd element of tuple                                       
              col_types[i] = "int"
            elif col_type == "float":       
              col_types[i] = "float"
            elif col_type == "str":
              col_types[i] = "str"

          data.append(contents)  
    print(data)                                                          # Get the data for the 1st element of tuple

    if line_count == 0:                                                                    # In case the program can't find any line from the beginning
      raise Exception("Tabel tidak boleh kosong.")

    return data, col_names, col_types                                                      # Return the tuple

  except Exception as e:                                                                   # Handle exception in opening the file                                                           
    raise e
  
file_name = 'abalone.csv'
sukses = read_csv(file_name) 
print(sukses[0]) # keseluruhan data kaya ['M', '0.35', '0.265', '0.09', '0.197', '0.073', '0.0365', '0.077', '7']
print(sukses[1]) # keseluruhan data + ['Sex', 'Length', 'Diameter', 'Height', 'Whole_weight', 'Shucked_weight', 'Viscera_weight', 'Shell_weight', 'Rings']
print(sukses[2]) # keseluruhan data + ['str', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'int']