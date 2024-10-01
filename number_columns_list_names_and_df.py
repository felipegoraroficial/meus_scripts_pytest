def number_columns_list_names_and_df(df,list_names):

    len_columns_df = len(df.schema)

    len_list_names = len(list_names)

    print(f'Número de colunas dataframe: {len_columns_df}')

    print(f'Número de nomes lista> {len_list_names}')

    print(f'Diferença colunas dataframe e nomes lista: {len_columns_df - len_list_names}')

    assert len_columns_df == len_list_names