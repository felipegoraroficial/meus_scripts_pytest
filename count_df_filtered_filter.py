def count_df_filtered_filter(df,filter):

    df_filter = df.filter(filter)

    count_lines_filtered = df_filter.count()

    df_unfilter = df.filter(~filter)

    count_lines_unfiltered = df_unfilter.count()

    count_lines_df = df.count()

    print(f'Quantidade de linhas filtradas: {count_lines_filtered}')

    print(f'Quantidade de linhas não filtradas: {count_lines_unfiltered}')

    print(f'Quantidade de linhas totais: {count_lines_df}')

    print(f'Resultado: {count_lines_filtered + count_lines_unfiltered} = {count_lines_df}')

    assert (count_lines_filtered + count_lines_unfiltered) == count_lines_df