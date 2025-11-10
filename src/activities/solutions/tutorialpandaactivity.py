from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
def check_csv_file(arg_1, arg_2):
    the_csv_file = Path(__file__).parent.parent.joinpath(arg_1, arg_2)

    return the_csv_file
def check_xlsx_file(arg_1, arg_2):
    the_xlsx_file = Path(__file__).parent.parent.joinpath(arg_1, arg_2)
    return the_xlsx_file
def read_intersted_col_csv_file_ignore_encodingerrors(the_csv_file,intersted_cols):
    df = pd.read_csv(the_csv_file, encoding = "utf-8", encoding_errors = "ignore", usecols = intersted_cols)
    return df
def read_csv_file(the_csv_file):
    variable_name_for_df = pd.read_csv(the_csv_file)
    return variable_name_for_df
def read_xlsx_file_1(the_xlsx_file_path):
    variable_name_for_df_1 = pd.read_excel(the_xlsx_file_path, sheet_name=0)
    return variable_name_for_df_1
def read_xlsx_file_2(the_xlsx_file_path):
    variable_name_for_df_2 = pd.read_excel(the_xlsx_file_path, sheet_name=1)
    return variable_name_for_df_2
def describe_dataframe(df, columns_labels = None):
     """This function describe all of the columns information of the data when 
     not specified columns_labels. 
        Parameters
        df (DataFrame): DataFrame to describe
        columns_labels (list): Name of column labels

        Returns:
        String: Dtype of the columns.
 
     """
     if columns_labels is not None:
         Dtype_info = df[columns_labels].dtypes
     else:
         Dtype_info = df.dtypes
     return Dtype_info
def get_missing_values(df, columns_labels = None):
    """This function describe all of the columns information of the data when 
     not specified columns_labels. 
        Parameters
        df (DataFrame): DataFrame to describe
        columns_labels (list): Name of column labels

        Returns:
        String: Dtype of the columns.
 
     """
    if columns_labels is not None:
        missing_values = df[columns_labels].isna().sum()
    else:
        missing_values = df.isna().sum()
    return missing_values
def get_missing_rows(df):
    """This function describe all of the columns information of the data when 
     not specified columns_labels. 
        Parameters
        df (DataFrame): DataFrame to describe

        Returns:
        DataFrame: Rows with missing values.
 
     """
    missing_rows = df.loc[df.isna().any(axis=1), :]
    return missing_rows
def get_missing_columns(df):
    """This function describe all of the columns information of the data when 
     not specified columns_labels. 
        Parameters
        df (DataFrame): DataFrame to describe

        Returns:
        DataFrame: Columns with missing values.
 
     """
    missing_columns = df.loc[:, df.isna().any(axis=0)]
    return missing_columns
def plot_histogram(df, column_label_1=None, column_label_2=None):
    """This function plot histogram of a specified column in the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_label (str): Name of the column to plot

        Returns:
        None: Displays the histogram plot.
    """
    # Determine which columns to plot based on the provided arguments.
    cols_to_plot = []
    if column_label_1 is not None:
        cols_to_plot.append(column_label_1)
    if column_label_2 is not None:
        cols_to_plot.append(column_label_2)

    # If specific columns were provided, plot only those with a legend.
    if cols_to_plot:
        ax = None
        # use a bit of transparency so overlapping histograms are visible
        for col in cols_to_plot:
            ax = df[col].plot(kind='hist', bins=30, edgecolor='black', alpha=0.6, label=col, ax=ax)
            ax.legend()
    plt.show()
def plot_boxplot(df, column_label=None):
    """This function plot boxplot of a specified column in the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_label (str): Name of the column to plot

        Returns:
        None: Displays the boxplot.
    """
    if column_label is not None:
        ax = df.boxplot(column=column_label)
        plt.show()
def plot_lineplot(df, x_column=None, y_column=None):
    """This function plot lineplot of a specified column in the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        x_column (str): Name of the column for x-axis
        y_column (str): Name of the column for y-axis

        Returns:
        None: Displays the line plot.
    """
def unique_values(df, column_label):
    """This function returns the unique values in a specified column of the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_label (str): Name of the column to check

        Returns:
        array: Unique values in the specified column.
    """
    return df[column_label].unique()
def count_values(df, column_label):
    """This function returns the count of unique values in a specified column of the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_label (str): Name of the column to check

        Returns:
        Series: Count of unique values in the specified column.
    """
    return df[column_label].value_counts()
def change_values_withquery(df, column_label, old_value_list, new_value_list, old_value=None, new_value=None):
    """This function changes occurrences of old_value to new_value in a specified column of the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_label (str): Name of the column to modify
        old_value_list: Values to be replaced
        new_value_list: Values to replace with
        old_value: Single value to be replaced (optional)
        new_value: Single value to replace with (optional)

        Returns:
        DataFrame: DataFrame with updated values in the specified column.
    """
    for i in range(len(old_value_list)):
        old_value = old_value_list[i]
        new_value = new_value_list[i]
        df.loc[df.query(f"{column_label} == '{old_value}'").index, column_label] = new_value
    return df
def change_values_withmask(df, column_label, old_value, new_value):
    """This function changes occurrences of old_value to new_value in a specified column of the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_label (str): Name of the column to modify
        old_value: Value to be replaced
        new_value: Value to replace with

        Returns:
        DataFrame: DataFrame with updated values in the specified column.
    """
    df.loc[df[column_label] == old_value, column_label] = new_value
    return df
def change_values_withat(df, column_label, old_value, new_value):
    """This function only changes the first occurrence of old_value to new_value in a specified column of the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_label (str): Name of the column to modify
        old_value: Value to be replaced
        new_value: Value to replace with

        Returns:
        DataFrame: DataFrame with updated values in the specified column.
    """
    index = df.query(f"{column_label} == '{old_value}'").index[0]
    df.at[index,column_label] = new_value
    return df
def remove_strips(df, column_label):
    """This function removes leading and trailing whitespace from string values in a specified column of the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_label (str): Name of the column to modify

        Returns:
        DataFrame: DataFrame with stripped string values in the specified column.
    """
    df[column_label] = df[column_label].str.strip()
    return df
def remove_columns(df, columns_labels):
    """This function removes specified columns from the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        columns_labels (list): List of column names to remove

        Returns:
        DataFrame: DataFrame with specified columns removed.
    """
    df_new = df.drop(columns_labels, axis=1)
    return df_new
def remove_rows(df, rows_indices, drop):
    """This function removes specified rows from the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        rows_indices (list): List of row indices to remove

        Returns:
        DataFrame: DataFrame with specified rows removed.
    """
    if drop == True:
        df_new = df.drop(rows_indices, axis=0)
        df_new = df_new.reset_index(drop=True)
    else:
        df_new = df.drop(rows_indices, axis=0)
    return df_new
def change_dtype(df, column_labels, new_dtypes):
    """This function changes the data type of a specified list of columns in the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_labels (list): List of column names to modify
        new_dtypes (list): List of new data types to convert to

        Returns:
        DataFrame: DataFrame with updated data type in the specified column.
    """
    for i in range(len(column_labels)):
        column_label, new_dtype = column_labels[i], new_dtypes[i]
        df[column_label] = df[column_label].astype(new_dtype)
    return df
def change_dtype_datetime(df, column_labels, new_dtypes):
    """This function changes the data type of a specified list of columns to datetime in the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_labels (list): List of column names to modify
        new_dtypes (list): List of new data types to convert to

        Returns:
        DataFrame: DataFrame with updated data type in the specified column.
    """
    for i in range(len(column_labels)):
        column_label, new_dtype = column_labels[i], new_dtypes[i]
        df[column_label] = pd.to_datetime(df[column_label], format=new_dtype)
    return df
def add_column_at_end_bycalculation(df, new_column_label,column_1,column_2, operation):
    """This function adds a new column at the end of the DataFrame by performing a calculation on two existing columns.
        Parameters
        df (DataFrame): DataFrame containing the data
        new_column_label (str): Name of the new column to add
        column_1 (str): Name of the first column for calculation
        column_2 (str): Name of the second column for calculation
        operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide')

        Returns:
        DataFrame: DataFrame with the new calculated column added.
    """
    if operation == 'add':
        df[new_column_label] = df[column_1] + df[column_2]
    elif operation == 'subtract':
        df[new_column_label] = df[column_1] - df[column_2]
    elif operation == 'multiply':
        df[new_column_label] = df[column_1] * df[column_2]
    elif operation == 'divide':
        df[new_column_label] = df[column_1] / df[column_2]
    else:
        raise ValueError("Unsupported operation. Use 'add', 'subtract', 'multiply', or 'divide'.")
    return df
def add_column_at_behind_aspecific_column_bycalculation(df, new_column_label, index_position, column_1, column_2, operation, column_dtype=None):
    """This function adds a new column at a specified index position in the DataFrame by performing a calculation on two existing columns.
        Parameters
        df (DataFrame): DataFrame containing the data
        new_column_label (str): Name of the new column to add
        index_position (int): Index position to insert the new column
        column_1 (str): Name of the first column for calculation
        column_2 (str): Name of the second column for calculation
        operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide')
        column_dtype: Data type of the new column (optional)

        Returns:
        DataFrame: DataFrame with the new calculated column added at the specified index.
    """
    if operation == 'add':
        duration_value = (df[column_1] + df[column_2]).dt.days.astype(column_dtype)
    elif operation == 'subtract':
        duration_value = (df[column_1] - df[column_2]).dt.days.astype(column_dtype)
    elif operation == 'multiply':
        duration_value  = (df[column_1] * df[column_2]).dt.days.astype(column_dtype)
    elif operation == 'divide':
        duration_value = (df[column_1] / df[column_2]).dt.days.astype(column_dtype)
    else:
        raise ValueError("Unsupported operation. Use 'add', 'subtract', 'multiply', or 'divide'.")

    if column_dtype is None:
        raise ValueError("Unsupported data type. Please specify a valid data type for the new column.")

    df.insert(df.columns.get_loc(index_position)+1, new_column_label, duration_value)
    return df
def print_column_values(df, column_label=None):
    """This function prints the values of a specified column in the DataFrame.
        Parameters
        df (DataFrame): DataFrame containing the data
        column_label (str): Name of the column to print

        Returns:
        None: Prints the values of the specified column.
    """
    if column_label is not None:
        content_of_column = df.loc[:, column_label]
        print(content_of_column)
    else:
        print(df)
def combine_dataframes_merge(left_df, right_df, how, left_on = None, left_index = False, right_index = False, right_on = None, sort = False, suffixes = ('_x', '_y'), copy = None, indicator = False, validate = None):
    """This function combines two DataFrames using a left merge.
        Parameters
        left_df (DataFrame): Left DataFrame
        right_df (DataFrame): Right DataFrame
        how (str): Type of merge ('left', 'right', 'inner', 'outer')
        left_on (str): Column name from the left DataFrame to join on (optional)
        right_on (str): Column name from the right DataFrame to join on (optional)
        left_index (bool): Whether to use the index from the left DataFrame (optional)
        right_index (bool): Whether to use the index from the right DataFrame (optional)

        Returns:
        DataFrame: Merged DataFrame.
    """
    if left_on is not None and right_on is not None:
        merged_df = pd.merge(left_df, right_df, how=how, left_on=left_on, right_on=right_on)
    elif left_index and right_index:
        merged_df = pd.merge(left_df, right_df, how=how, left_index=True, right_index=True)
    else:
        merged_df = pd.merge(left_df, right_df, how=how)
    return merged_df
def save_dataframe_to_csv(df, output_file_path, index=False):
    """This function saves the DataFrame to a CSV file.
        Parameters
        df (DataFrame): DataFrame to save
        output_file_path (str): Path to the output CSV file
        index (bool): Whether to include the index in the CSV file (default is False)

        Returns:
        None: Saves the DataFrame to the specified CSV file.
    """
    df.to_csv(output_file_path, index=index)
    return merged_df


if __name__ == "__main__":
    #Check
    xlsx_file_path = check_xlsx_file("data","paralympics_all_raw.xlsx")
    #if xlsx_file_path.exists():
        #print(f"The XLSX file found: {xlsx_file_path}")
    #else:
        #print(f"The XLSX file not found")
    csv_file_path = check_csv_file("data","paralympics_raw.csv")
    npc_csv_path = check_csv_file("data","npc_codes.csv")
    #if csv_file_path.exists():
        #print(f"The CSV file found: {csv_file_path}")
    #else:
        #print(f"The CSV file not found")
    # Example of reading the CSV file
    #import csv

    #data_file = check_csv_file()  # Your code that locates the file

    #with open(data_file) as csv_file:
        #csv_reader = csv.reader(csv_file, delimiter=',')
        #first_row = next(csv_reader)
        #print(first_row)
    npc_csv_df = read_intersted_col_csv_file_ignore_encodingerrors(npc_csv_path,intersted_cols=["Code","Name"])
    read_xlsx_file_2(xlsx_file_path)
    read_xlsx_file_1(xlsx_file_path)
    csv_df = read_csv_file(csv_file_path)
    #print(csv_df.shape)
    #column_info = describe_dataframe(csv_df, columns_labels = None)
    #print(column_info)
    #isna = get_missing_values(csv_df, columns_labels = None)
    #print(isna)
    #missing_data_rows = get_missing_rows(csv_df)
    #print(missing_data_rows)
    #missing_data_columns = get_missing_columns(csv_df)
    #print(missing_data_columns)
    #plot_histogram(csv_df, column_label_1="participants_f", column_label_2="participants_m")
    #plot_boxplot(csv_df, column_label="sports")
    #plot_boxplot(csv_df, column_label="durations")
    #plot_lineplot(csv_df, x_column="year", y_column="participants")
    #unique_vals = unique_values(csv_df, column_label="type")
    #print(unique_vals)
    #count_vals = count_values(csv_df, column_label="type")
    #print(count_vals)
    df = change_values_withquery(csv_df, column_label="country", old_value_list=["UK","USA","Korea","Russia","China"], new_value_list=["Great Britain","United States of America","Republic of Korea","Russian Federation","People's Republic of China"])
    #new_csv_df = change_values_withmask(csv_df, column_label="type", old_value="summer", new_value="Summer_modified")
    #new_csv_df = change_values_withat(csv_df, column_label="type", old_value="summer", new_value="Summer_Modified")
    
    df = remove_rows(csv_df, rows_indices=[0,17,31], drop=True)
    df = remove_columns(df, columns_labels=["URL", "disabilities_included","highlights"])
    #print_column_values(new_csv_df, column_label= None)
    #first_three_rows_old_df = csv_df.head(3)
    #print(first_three_rows_old_df)
    df = remove_strips(df, column_label="type")
    df = change_dtype(df, column_labels = ["countries", 'events', 'participants_m', 'participants_f', 'participants',"type" ,"country","host"], new_dtypes = [ int, int, int, int, int, "string", "string", "string"])
    df = change_dtype_datetime(df, column_labels = ['start', 'end'], new_dtypes = ['%d/%m/%Y', '%d/%m/%Y'])
    df = add_column_at_end_bycalculation(df, new_column_label="total_duration_days", column_1="end", column_2="start", operation="subtract")
    df = add_column_at_behind_aspecific_column_bycalculation(df, new_column_label="total_duration_days_2", index_position="end", column_1="end", column_2="start", operation="subtract", column_dtype="int")
    #column_info = describe_dataframe(df, columns_labels = None)
    #print(column_info)
    #first_few_rows_modified_df = df.head(5)
    #print(first_few_rows_modified_df)
    merged_df = combine_dataframes_merge(left_df=df, right_df=npc_csv_df, how="left", left_on="country", right_on="Name")
    merged_df = remove_columns(merged_df, columns_labels=["Name"])
    #print_column_values(merged_df, column_label=["country", "Code"])
    save_path = check_csv_file("data","paralympics_merged.csv")
    save_dataframe_to_csv(merged_df, save_path)