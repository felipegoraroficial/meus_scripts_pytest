def count_df_filtered_is_not_null(df,column):

    df_filter = df.filter(col(column).isNotNull())

    count_lines_filtered = df_filter.count()

    df_unfilter = df.filter(col(column).isNull())

    count_lines_unfiltered = df_unfilter.count()

    count_lines_df = df.count()

    print(f'Quantidade de linhas não nulas: {count_lines_filtered}')

    print(f'Quantidade de linhas nulas: {count_lines_unfiltered}')

    print(f'Quantidade de linhas toais: {count_lines_df}')

    print(f'Resultado: {count_lines_filtered + count_lines_unfiltered} = {count_lines_df}')

    assert (count_lines_filtered + count_lines_unfiltered) == count_lines_df