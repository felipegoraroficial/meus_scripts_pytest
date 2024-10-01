def schema_equals_df_schema(df,schema):

    df_columns_list_names = df.schema.fieldNames()

    schema_columns_list_names = schema.fieldNames()

    diferences_array = ['| Nome Dataframe | Nome Schema | Coluna |']

    for i, name in enumerate(df_columns_list_names):

        if name != schema_columns_list_names[i]:

            diferences_array.append(f'| {name} | {schema_columns_list_names[i]} | {i_+ 1} |')

    print('Nomes')

    print(f'Nomes colunas dataframes: \n{df_columns_list_names}')

    print(f'Nomes colunas schema: \n{schema_columns_list_names}')

    if(len(diferences_array) > 1):

        print(f'Diferença ({len(diferences_array) - 1}):')

        for item in diferences_array:

            print(item)

    assert df_columns_list_names == schema_columns_list_names

    df_columns_list_types = [field.dataType for field in df.schema.fields]

    schema_columns_list_types = [field.dataType for field in schema.fields]

    diferences_array = ['| Tipo Dataframe | Tipo Schema | Coluna |']

    for i, _type in enumerate(df_columns_list_types):

        if _type != schema_columns_list_types[i]:

            diferences_array.append(f'| {_type} | {schema_columns_list_types[i]} | {i_+ 1} |')

    print('Tipos')

    print(f'Tipos colunas dataframes: \n{df_columns_list_types}')

    print(f'Tipos colunas schema: \n{schema_columns_list_types}')

    if(len(diferences_array) > 1):

        print(f'Diferença ({len(diferences_array) - 1}):')

        for item in diferences_array:

            print(item)

    assert df_columns_list_types == schema_columns_list_types