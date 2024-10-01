def list_names_equal_df_names(df,list_name):

    df_columns_list_names = df.schema.fieldNames()

    diferences_array = ['| Nome Dataframe | Nome Lista | Coluna |']

    for i, name in enumerate(df_columns_list_names):

        if name != list_name[i]:

            diferences_array.append(f'| {name} | {list_name[i]} | {i + 1} |')

    print('Nomes')

    print(f'Nomes colunas dataframe:\n{df_columns_list_names}')

    print(f'Lista de nomes:\n{list_name}')

    if(len(diferences_array) > 1):

        print(f'Diferenças ({len(diferences_array) - 1}):')

        for item in diferences_array:

            print(item)

    assert df_columns_list_names == list_name