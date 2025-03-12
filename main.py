import pandas as pd

# dados é um dicionário
dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [25, 36, 29],
}

df = pd.DataFrame(dados)
# print(df)

s = pd.Series([10,20,30])
# print(s)

df = pd.read_csv("funcionarios.csv", sep=";", encoding="utf-8")

# Para tabela muito grande use head
print(df.head)
# ID           Nome Completo  Idade Data de Nascimento     Gênero   Salário  Peso (kg)  Altura (m) Departamento Data de Admissão                        
# Email             Telefone
# 0      1       João Miguel Costa     58         09/12/1967  Masculino  12045.31       86.9        1.64    Logística       13/01/2018         barbosaigor@rocha.br     +55 84 4554-1291    
# 1      2           Luiza Freitas     25         22/03/2004   Feminino   9491.13       71.6        1.80       Vendas       05/07/2020          leandro93@gmail.com        0300-167-7401    
# 2      3      Valentina Oliveira     19         06/06/1961  Masculino  12730.28       65.4        1.92    Marketing       17/12/2018            efarias@gmail.com  +55 (084) 6952 6333    
# 3      4         Lorenzo Cardoso     65         07/05/1987   Feminino  13131.53      118.9        1.84   Engenharia       10/01/2017    juliasilveira@oliveira.br  +55 (021) 8323 6186    
# 4      5        Giovanna Cardoso     35         18/07/1966  Masculino  15962.48       53.8        1.64           TI       18/08/2024     isabellacorreia@gomes.br  +55 (061) 7507-4719    

print(df.tail)
# 495  496        Augusto Silveira     65         29/01/1964      Outro  11222.23       77.5        1.99   Financeiro       13/11/2020     rezendebianca@bol.com.br      (021) 6790-3775    
# 496  497        Dra. Bruna Gomes     33         28/09/1968   Feminino   8213.11       82.0        1.99           TI       18/12/2021       cunhabarbara@gmail.com  +55 (031) 2242 1106    
# 497  498  João Gabriel das Neves     35         01/09/1969  Masculino   3996.02       66.9        1.95           RH       20/08/2021  maria-cecilia42@hotmail.com     +55 71 9061-0958    
# 498  499       Emanuel Fernandes     28         16/06/2003  Masculino  14207.92       90.8        1.96           TI       24/04/2016   carvalhootavio@hotmail.com      (081) 1164 0522    
# 499  500     Vitor Gabriel Jesus     62         15/01/1977  Masculino  12676.42       53.4        1.61   Financeiro       28/01/2019   maria-vitoria66@bol.com.br         84 7115-5517    


# Apenas uma coluna
print(df["Nome Completo"])
# 0           João Miguel Costa
# 1               Luiza Freitas
# 2          Valentina Oliveira
# 3             Lorenzo Cardoso
# 4            Giovanna Cardoso

# Duas colunas
print(df[["Nome Completo","Salário"]])
# 495        Augusto Silveira  11222.23
# 496        Dra. Bruna Gomes   8213.11
# 497  João Gabriel das Neves   3996.02
# 498       Emanuel Fernandes  14207.92
# 499     Vitor Gabriel Jesus  12676.42

print(df['Salário'] > 1000)
# 0      True
# 1      True
# 2      True
# 3      True
# 4      True

# Filtro
print(df[df['Idade'] > 50])
# 483  484     Sr. Bruno Campos     65         16/07/1965   Feminino  18945.33      117.4        2.00   Engenharia       15/05/2022              zdias@lima.org  +55 (031) 5408-6545        
# 491  492        Emilly da Paz     65         07/09/1995      Outro   9632.27       82.7        1.54    Marketing       04/10/2019   luiz-henrique34@ig.com.br     +55 11 5503-9549        
# 494  495       Gabriel Santos     60         27/08/1999  Masculino   5880.24       56.3        1.67    Logística       26/04/2016           lorenasouza@da.br     +55 31 3324-9229        
# 495  496     Augusto Silveira     65         29/01/1964      Outro  11222.23       77.5        1.99   Financeiro       13/11/2020    rezendebianca@bol.com.br      (021) 6790-3775        
# 499  500  Vitor Gabriel Jesus     62         15/01/1977  Masculino  12676.42       53.4        1.61   Financeiro       28/01/2019  maria-vitoria66@bol.com.br         84 7115-5517        

filtro1 = df['Salário'] > 10000
filtro2 = df['Idade'] > 60
print(df[filtro1 & filtro2])
# 450  451             Eloah Gomes     65         20/04/1966      Outro  ...        1.73    Engenharia        12/08/2021               barrosleonardo@da.org         81 8894 3782
# 459  460          Enrico Rezende     62         11/07/1982  Masculino  ...        1.51    Financeiro        14/01/2019            iansilveira@yahoo.com.br     +55 41 1473-0481
# 475  476    Dra. Manuela Martins     61         29/03/2000   Feminino  ...        1.54     Logística        30/03/2021        benjaminmonteiro@costela.com        0900 344 1336
# 483  484        Sr. Bruno Campos     65         16/07/1965   Feminino  ...        2.00    Engenharia        15/05/2022                      zdias@lima.org  +55 (031) 5408-6545
# 495  496        Augusto Silveira     65         29/01/1964      Outro  ...        1.99    Financeiro        13/11/2020            rezendebianca@bol.com.br      (021) 6790-3775
# 499  500     Vitor Gabriel Jesus     62         15/01/1977  Masculino  ...        1.61    Financeiro        28/01/2019          maria-vitoria66@bol.com.br         84 7115-5517

df['Custo Salário'] = df['Salário'] * 2.1
print(df[['Nome Completo', 'Salário', 'Custo Salário']])
# 1             Luiza Freitas   9491.13      19931.373
# 2        Valentina Oliveira  12730.28      26733.588
# 3           Lorenzo Cardoso  13131.53      27576.213
# 4          Giovanna Cardoso  15962.48      33521.208

# Remover coluna
df = df.drop('Salário', axis=1)
print(df)

#  Coluna classificada como object ocupa muito mais memória
print(df.info())
#  #   Column              Non-Null Count  Dtype
# ---  ------              --------------  -----
#  0   ID                  500 non-null    int64
#  1   Nome Completo       500 non-null    object
#  2   Idade               500 non-null    int64
#  3   Data de Nascimento  500 non-null    object
#  4   Gênero              500 non-null    object
#  5   Peso (kg)           500 non-null    float64
#  6   Altura (m)          500 non-null    float64
#  7   Departamento        500 non-null    object
#  8   Data de Admissão    500 non-null    object
#  9   Email               500 non-null    object
#  10  Telefone            500 non-null    object
#  11  Custo Salário       500 non-null    float64
# dtypes: float64(3), int64(2), object(7)
# memory usage: 47.0+ KB

#  Descritivo estatistico
print(df.describe())
#                ID       Idade   Peso (kg)  Altura (m)  Custo Salário
# count  500.000000  500.000000  500.000000  500.000000     500.000000
# mean   250.500000   40.988000   84.590600    1.754140   22935.776976
# std    144.481833   14.189663   20.074835    0.141262   10858.102347
# min      1.000000   18.000000   50.100000    1.500000    4243.512000
# 25%    125.750000   28.000000   66.850000    1.640000   14199.249750
# 50%    250.500000   40.000000   83.100000    1.750000   22035.867000
# 75%    375.250000   53.000000  100.425000    1.870000   32561.214000
# max    500.000000   65.000000  120.000000    2.000000   41976.312000

# Soma
print(df['Custo Salário'].sum())
#                ID       Idade   Peso (kg)  Altura (m)  Custo Salário
# count  500.000000  500.000000  500.000000  500.000000     500.000000
# mean   250.500000   40.988000   84.590600    1.754140   22935.776976
# std    144.481833   14.189663   20.074835    0.141262   10858.102347
# min      1.000000   18.000000   50.100000    1.500000    4243.512000
# 25%    125.750000   28.000000   66.850000    1.640000   14199.249750
# 50%    250.500000   40.000000   83.100000    1.750000   22035.867000
# 75%    375.250000   53.000000  100.425000    1.870000   32561.214000
# max    500.000000   65.000000  120.000000    2.000000   41976.312000
# 11467888.488000002

# Média
print(df['Custo Salário'].mean())
#                ID       Idade   Peso (kg)  Altura (m)  Custo Salário
# count  500.000000  500.000000  500.000000  500.000000     500.000000
# mean   250.500000   40.988000   84.590600    1.754140   22935.776976
# std    144.481833   14.189663   20.074835    0.141262   10858.102347
# min      1.000000   18.000000   50.100000    1.500000    4243.512000
# 25%    125.750000   28.000000   66.850000    1.640000   14199.249750
# 50%    250.500000   40.000000   83.100000    1.750000   22035.867000
# 75%    375.250000   53.000000  100.425000    1.870000   32561.214000
# max    500.000000   65.000000  120.000000    2.000000   41976.312000
# 11467888.488000002
# 22935.776976000005

# Remover linhas que contém NaN
df = pd.read_csv("funcionarios.csv", sep=";", encoding="utf-8")
df = df.dropna()
print(df)
#      ID           Nome Completo  Idade Data de Nascimento     Gênero   Salário  Peso (kg)  Altura (m) Departamento Data de Admissão                        Email             Telefone
# 2      3      Valentina Oliveira     19         06/06/1961  Masculino  12730.28       65.4        1.92    Marketing       17/12/2018            efarias@gmail.com  +55 (084) 6952 6333    
# 3      4         Lorenzo Cardoso     65         07/05/1987   Feminino  13131.53      118.9        1.84   Engenharia       10/01/2017    juliasilveira@oliveira.br  +55 (021) 8323 6186    
# 4      5        Giovanna Cardoso     35         18/07/1966  Masculino  15962.48       53.8        1.64           TI       18/08/2024     isabellacorreia@gomes.br  +55 (061) 7507-4719    
# 5      6      Luiz Henrique Dias     33         01/06/1974  Masculino   8846.80       64.3        1.50           RH       13/09/2019        enogueira@pereira.com        0300 753 3535    
# 6      7          Melissa Castro     32         04/09/1978   Feminino  18353.08      116.2        1.55           RH       23/04/2023  fernandoda-cunha@uol.com.br      (021) 7955-2451    
# ..   ..


# Remover linhas que a coluna contém NaN
df = pd.read_csv("funcionarios.csv", sep=";", encoding="utf-8")
df = df.dropna(subset='Departamento')
print(df)
#       ID           Nome Completo  Idade Data de Nascimento     Gênero   Salário  Peso (kg)  Altura (m) Departamento Data de Admissão                        Email             Telefone
# 0      1       João Miguel Costa     58         09/12/1967  Masculino  12045.31       86.9         NaN    Logística       13/01/2018         barbosaigor@rocha.br     +55 84 4554-1291    
# 1      2           Luiza Freitas     25         22/03/2004   Feminino   9491.13       71.6         NaN       Vendas       05/07/2020          leandro93@gmail.com        0300-167-7401    
# 2      3      Valentina Oliveira     19         06/06/1961  Masculino  12730.28       65.4        1.92    Marketing       17/12/2018            efarias@gmail.com  +55 (084) 6952 6333    
# 3      4         Lorenzo Cardoso     65         07/05/1987   Feminino  13131.53      118.9        1.84   Engenharia       10/01/2017    juliasilveira@oliveira.br  +55 (021) 8323 6186    
# 4      5        Giovanna Cardoso     35         18/07/1966  Masculino  15962.48       53.8        1.64           TI       18/08/2024     isabellacorreia@gomes.br  +55 (061) 7507-4719    

# Preencher os valores NaN com um novo valor
df['Altura (m)'] = df['Altura (m)'].fillna(1.7)
print(df)
#       ID           Nome Completo  Idade Data de Nascimento     Gênero   Salário  Peso (kg)  Altura (m) Departamento Data de Admissão                        Email             Telefone
# 0      1       João Miguel Costa     58         09/12/1967  Masculino  12045.31       86.9        1.70    Logística       13/01/2018         barbosaigor@rocha.br     +55 84 4554-1291    
# 1      2           Luiza Freitas     25         22/03/2004   Feminino   9491.13       71.6        1.70       Vendas       05/07/2020          leandro93@gmail.com        0300-167-7401    
# 2      3      Valentina Oliveira     19         06/06/1961  Masculino  12730.28       65.4        1.92    Marketing       17/12/2018            efarias@gmail.com  +55 (084) 6952 6333    
# 3      4         Lorenzo Cardoso     65         07/05/1987   Feminino  13131.53      118.9        1.84   Engenharia       10/01/2017    juliasilveira@oliveira.br  +55 (021) 8323 6186    
# 4      5        Giovanna Cardoso     35         18/07/1966  Masculino  15962.48       53.8        1.64           TI       18/08/2024     isabellacorreia@gomes.br  +55 (061) 7507-4719    

# Define o tipo da coluna
df['Salário'] = df['Salário'].astype(float)
df["Data de Nascimento"] = pd.to_datetime(df["Data de Nascimento"], format="%d/%m/%Y")
df["Idade"] = df["Idade"].astype(int)
print(df.info())
#  #   Column              Non-Null Count  Dtype
# ---  ------              --------------  -----
#  0   ID                  500 non-null    int64
#  1   Nome Completo       500 non-null    object
#  2   Idade               500 non-null    int64
#  3   Data de Nascimento  500 non-null    datetime64[ns]
#  4   Gênero              500 non-null    object
#  5   Salário             500 non-null    float64
#  6   Peso (kg)           500 non-null    float64
#  7   Altura (m)          500 non-null    float64
#  8   Departamento        500 non-null    object
#  9   Data de Admissão    500 non-null    object
#  10  Email               500 non-null    object
#  11  Telefone            500 non-null    object
# dtypes: datetime64[ns](1), float64(3), int64(2), object(6)
# memory usage: 47.0+ KB

# Contar ocorrencias
print(df['Gênero'].value_counts())

df.groupby('Departamento')
df.groupby('Departamento')['Salário'].mean()
print(df)
# Departamento
# Engenharia    11219.628140
# Financeiro    11177.066912
# Logística     10777.290303
# Marketing     10176.181096
# RH            10551.688889
# TI            10889.100000
# Vendas        11579.544085

# Ordernar por salário
print(df.sort_values(by='Idade', ascending=True))
#       ID           Nome Completo  Idade Data de Nascimento    Gênero   Salário  Peso (kg)  Altura (m) Departamento Data de Admissão                      Email          Telefone
# 456  457  Pedro Henrique da Mota     18         1991-03-30  Feminino   9724.02       71.1        1.51       Vendas       31/10/2020              iaraujo@da.br   (011) 1892-9793
# 35    36             Raul Mendes     18         1961-06-21  Feminino   4065.97       75.3        1.76    Marketing       07/07/2016          ycostela@costa.br      21 6693 7458
# 444  445         Carolina Novaes     18         1995-12-16     Outro   7177.33      110.5        1.50   Engenharia       03/03/2021        yuri00@yahoo.com.br   (011) 3271-0478
# 412  413          Sr. Raul Ramos     18         1991-09-18     Outro  13784.83      108.0        1.93    Marketing       06/07/2017         fmoura@hotmail.com   (061) 6134 9940
# 388  389       Emanuella Pereira     18         2004-02-06     Outro  13860.26       65.7        1.60           TI       23/05/2020          gsales@peixoto.br  +55 84 5687-9819
# ..   ...                     ...    ...                ...       ...       ...        ...         ...          ...              ...                        ...               ...
# 131  132         Esther Caldeira     65         2002-09-07  Feminino  15908.15       59.0        1.64   Engenharia       08/08/2018       lorenzo02@ribeiro.br  +55 51 4313 2497
# 422  423           Isabelly Dias     65         1989-12-30  Feminino   7625.87       61.3        1.62    Marketing       09/05/2016        bryanpinto@dias.com      84 3787 7493
# 450  451             Eloah Gomes     65         1966-04-20     Outro  17250.95       90.0        1.73   Engenharia       12/08/2021      barrosleonardo@da.org      81 8894 3782
# 491  492           Emilly da Paz     65         1995-09-07     Outro   9632.27       82.7        1.54    Marketing       04/10/2019  luiz-henrique34@ig.com.br  +55 11 5503-9549
# 495  496        Augusto Silveira     65         1964-01-29     Outro  11222.23       77.5        1.99   Financeiro       13/11/2020   rezendebianca@bol.com.br   (021) 6790-3775

#  Unificar tabelas
df1 = pd.read_csv("funcionarios.csv", sep=";", encoding="utf-8")
df2 = pd.read_csv("cpf_rg.csv", sep=";", encoding="utf-8")
df = pd.merge(df1, df2, left_on='ID', right_on='ID')
print(df)
#       ID           Nome Completo  Idade Data de Nascimento     Gênero  ...  Data de Admissão                        Email             Telefone             CPF         RG
# 0      1       João Miguel Costa     58         09/12/1967  Masculino  ...        13/01/2018         barbosaigor@rocha.br     +55 84 4554-1291  615.748.293-19  762051383
# 1      2           Luiza Freitas     25         22/03/2004   Feminino  ...        05/07/2020          leandro93@gmail.com        0300-167-7401  752.638.491-09  216540379
# 2      3      Valentina Oliveira     19         06/06/1961  Masculino  ...        17/12/2018            efarias@gmail.com  +55 (084) 6952 6333  138.796.542-55  382640718
# 3      4         Lorenzo Cardoso     65         07/05/1987   Feminino  ...        10/01/2017    juliasilveira@oliveira.br  +55 (021) 8323 6186  093.216.485-42  147283504
# 4      5        Giovanna Cardoso     35         18/07/1966  Masculino  ...        18/08/2024     isabellacorreia@gomes.br  +55 (061) 7507-4719  497.261.850-76  214058670

# Unificar tabelas
df = pd.concat([df1, df1])
print(df)

# Salvar
df.to_csv('final.csv')