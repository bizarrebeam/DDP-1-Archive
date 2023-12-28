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
        for line in lines[1:]:
            values = line.strip().split(delimiter)
            data.append(values)
            if not column_types:
                column_types = [get_type(value) for value in values]

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
    selected_rows = []
    col_index = get_column_names(dataframe).index(col_name)
    for row in to_list(dataframe):
        if satisfy_cond(row[col_index], condition, value):
            selected_rows.append(row)
    return (selected_rows, get_column_names(dataframe), get_column_types(dataframe))

def select_cols(dataframe, selected_cols):
    selected_cols_indices = [get_column_names(dataframe).index(col) for col in selected_cols]
    selected_data = [[row[i] for i in selected_cols_indices] for row in to_list(dataframe)]
    return (selected_data, selected_cols, [get_column_types(dataframe)[i] for i in selected_cols_indices])

def count(dataframe, col_name):
    col_index = get_column_names(dataframe).index(col_name)
    col_type = get_column_types(dataframe)[col_index]

    if col_type != 'str':
        raise Exception(f"Kolom {col_name} harus bertipe string.")

    value_counts = {}
    for row in to_list(dataframe):
        value = row[col_index]
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    return value_counts

def mean_col(dataframe, col_name):
    col_index = get_column_names(dataframe).index(col_name)
    col_type = get_column_types(dataframe)[col_index]

    if col_type == 'str':
        raise Exception(f"Kolom {col_name} bukan bertipe numerik.")

    if not to_list(dataframe):
        raise Exception("Tabel kosong.")

    values = [float(row[col_index]) for row in to_list(dataframe)]
    return sum(values) / len(values)

def show_scatter_plot(x, y, x_label, y_label):
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def scatter(dataframe, col_name_x, col_name_y):
    x_index = get_column_names(dataframe).index(col_name_x)
    y_index = get_column_names(dataframe).index(col_name_y)

    x_values = [float(row[x_index]) for row in to_list(dataframe)]
    y_values = [float(row[y_index]) for row in to_list(dataframe)]

    show_scatter_plot(x_values, y_values, col_name_x, col_name_y)

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

    print("\n>>> Calculate the mean in the Length column (in the original dataframe)\n")
    print(mean_col(dataframe, "Length"))

    print("\n>>> Unique values in the Sex column, and the frequency of their occurrence (in the original dataframe)\n")
    print(count(dataframe, "Sex"))

    print("\n>>> Display 'Height' and 'Diameter' column's scatter plot\n")
    scatter(dataframe, "Height", "Diameter")
 
