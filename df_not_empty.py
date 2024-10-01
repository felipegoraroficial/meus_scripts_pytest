def df_not_empty(df):

    is_empty = df.isEmpty()

    print(f'Está vazio? {is_empty}')

    assert is_empty == False

    count_lines_df = df.count()

    print(f'Quantidade de linhas: {count_lines_df}')

    assert count_lines_df != 0    