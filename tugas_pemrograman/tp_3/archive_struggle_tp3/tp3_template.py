# Kita perlu import matplotlib untuk sebuah visualisasi
# Scatter Plot. 
#
# Apa itu Scatter plot?
#   https://chartio.com/learn/charts/what-is-a-scatter-plot/
#
# Jika Anda tidak bisa import matplotlib, ada kemungkinan 
# Anda belum install library matplotlib di local komputer 
# Anda. Silakan ikuti petunjuk pada
# https://matplotlib.org/stable/users/installing/index.html

import matplotlib.pyplot as plt

def get_type(a_str):
  """
    -- DIBUKA KE PESERTA --
    
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
  """
    Dataframe adalah sebuah abstraksi tabel data siap 
    proses yang dalam tugas kali ini direpresentasikan 
    sebagai 3-tuple:
    
      (data, list nama kolom, list tipe data)
    
    'data' merupakan list of lists yang menyimpan 
    nilai-nilai pada tabel dan mempunyai format:
    
    [[row_11, row_12, ..., row_1n],
     [row_21, row_22, ..., row_2n],
     ...
     [row_m1, row_m2, ..., row_mn]]
     
    Satu cell row_mn dapat bertipe string, integer,
    atau float. Jika semua cell pada kolom n berisi
    literal integer, maka ubah semuanya dalam tipe
    data integer; jika bukan integer, maka ada dua kemungkinan,
    yaitu float atau string; jika semua nilai pada
    kolom n berupa number dan ada satu yang float, maka
    jadikan semua tipe data pada kolom n tersebut sebagai
    float; jika cell-cell pada kolom n ada yang tidak 
    bisa dikonversikan ke integer maupun float, maka 
    tipe kolom n tersebut adalah string.
     
    Selain list of lists yang berisi tabel, informasi
    nama kolom juga disimpan dalam bentuk 
    'list nama kolom':
    
    [nama_kolom_1, nama_kolom_2, ..., nama_kolom_n]
    
    Elemen ketiga pada 3-tuple adalah 'list tipe data'
    pada setiap kolom. Ada tiga jenis tipe data dalam
    tugas kali ini = "str", "int", dan "float". Sebuah
    kolom bertipe "int" jika semua elemen pada kolom
    tersebut adalah literal integer; "float" jika semua
    elemen pada kolom adalah literal float (dan bukan
    literal integer); "str" jika selain kedua di atas.
    
    Fungsi ini bertugas untuk membaca sebuah file comma
    separated value, melakukan parsing, dan mengembalikan
    dataframe yang berupa 3-tuple.
    
    ASUMSI file csv:
      1. selalu ada header (nama kolom) pada baris pertama
      2. nama kolom yang diberikan sudah dijamin unik
      
    Daftar Exceptions:
      1. jika ada baris dengan jumlah kolom berbeda dari
         sebelumnya,
         
           raise Exception(f"Banyaknya kolom pada baris {x} tidak konsisten.")
           
           dengan x adalah nomor baris (1-based) yang kolomnya 
           berlebih pertama kali.
           
      2. jika tabel kosong,
            
            raise Exception("Tabel tidak boleh kosong.")
    
    parameter:
    file_name (string): nama file comma separated value
    delimiter (string): karakter pemisah antar kolom pada 
                        suatu baris.
                        
    return (list, list, list): (data, list nama kolom, list tipe data)
  """
  # TODO: Implement
  pass

def to_list(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
    
    mengembalikan bagian list of lists of items atau tabel data
    pada dataframe. Gunakan fungsi ini kedepannya jika ada keperluan
    untuk akses bagian data/tabel pada dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of lists of items
  """
  return dataframe[0]

def get_column_names(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
  
    dataframe[1] adalah berisi list of column names. Gunakan fungsi ini
    kedepannya jika ada keperluan untuk akses daftar nama kolom pada
    sebuah dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of column names
  """
  return dataframe[1]
  
def get_column_types(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
  
    dataframe[2] adalah berisi daftar tipe data dari
    setiap kolom tabel. Hanya ada tiga jenis tipe data,
    yaitu "str", "int", dan "float"
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of type names
  """
  return dataframe[2]

def head(dataframe, top_n = 10):
  """
  
    -- DIBUKA KE PESERTA --
  
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
  # TODO: Implement
  pass

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
  # TODO: Implement
  pass
  
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
  # TODO: Implement
  pass

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
  # TODO: Implement
  pass

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
  # TODO: Implement
  pass
  
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
  # TODO: Implement
  pass

if __name__ == "__main__":
  # TODO: Buat program yang memanfaatkan fungsi-fungsi di atas
  pass
  