    # #Cache connection used to connect database
    # @st.cache_resource(show_spinner='Connecting...')
        
    #     #Loading environment variables from secret.toml file into a dictionary
    # def load_data():
    #     environment_variables = st.secrets['Database']


    #     #Getting the values for the credentials you set in the '.env' file
    #     server = environment_variables['server']
    #     database = environment_variables['dbname']
    #     username = environment_variables['user']
    #     password = environment_variables['password']

    #     #Creating a connection string
    #     connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};MARS_Connection=yes;MinProtocolVersion=TLSv1.2;'

    #     #establishing a connestion to the database using pyodbc library
    #     conn = pyodbc.connect(connection_string)

    #     #retrieving data from database
    #     query = 'Select * From dbo.LP2_Telco_churn_first_3000'
    #     df = pd.read_sql(query,conn)
    #     df.to_csv('Telco_churn_3000.csv', index=False)



    #     conn.close()
    #     return df

    # df = load_data()

    # Path of the saved data to csv