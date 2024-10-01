def count_union_df(df_union, df_list):

    count_lines_df_list = 0

    for df in df_list:
        count_lines_df_list += df.count()

    count_lines_df_union = df_union.count()

    print(f'Quantidade de linhas da lista de Dataframes: {count_lines_df_list}')

    print(f'Quantidade de linhas do Dataframe Resultante: {count_lines_df_union}')

    print(f'Diferença entre lista de dataframes e dataframe resultante: {count_lines_df_list - count_lines_df_union}')

    assert count_lines_df_list == count_lines_df_union