def number_columns_schema_and_df(df,schema):

    df_columns_list_names = df.schema.fielNames()

    schema_columns_list_names = schema.fieldNames()

    print(f'Nomes colunas dataframe: \n{df_columns_list_names}')

    print(f'Nomes colunas schema: \n{schema_columns_list_names}')

    len_columns_df = len(df.schema)

    len_columns_schema = len(schema)

    print(f'Número de colunas dataframe: {len_columns_df}')

    print(f'Número de colunas schema: {len_columns_schema}')

    print(f'Diferença colunas datafra,es e schema: {len_columns_df - len_columns_schema}')

    assert len_columns_df == len_columns_schema