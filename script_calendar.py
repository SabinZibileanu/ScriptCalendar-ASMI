import pandas as pd

def obtine_zile_nastere(path_df, luna, departament):
    
    dict_luna_an = {'1' : 'Ianuarie', 
                    '2': 'Februarie', 
                    '3': 'Martie', 
                    '4': 'Aprilie',
                    '5': 'Mai',
                    '6':'Iunie',
                    '7': 'Iulie',
                    '8': 'August',
                    '9': 'Septembrie',
                    '10': 'Octombrie',
                    '11': 'Noiembrie',
                    '12': 'Decembrie'}

    if str(luna) not in dict_luna_an.keys():
        print('Luna introdusa este invalida')
        return 

    lista_nume = []
    lista_data = []
    dataframe = pd.read_csv(path_df)
    dataframe = dataframe.rename(columns={"Data Nașterii": "DataNasterii"})

    for nume, prenume, data_nasterii in zip(dataframe.Nume, dataframe.Prenume, dataframe.DataNasterii):
        
        luna_nasterii = data_nasterii.split('/')[0]

        if luna_nasterii == str(luna):
            nume_complet = nume + " " + prenume
            lista_nume.append(nume_complet)
            lista_data.append(data_nasterii)
    
    dataframe_sarbatoriti =  pd.DataFrame()

    dataframe_sarbatoriti['NumePrenumeSarbatorit'] = lista_nume
    dataframe_sarbatoriti['DataSarbatorit'] = lista_data
    nume_dataframe = 'Sarbatoritii pe luna ' + str(dict_luna_an[str(luna)]) + '(' + str(departament) + ')'

    dataframe_sarbatoriti.to_csv(nume_dataframe +'.csv', index = True)
        

lista_departamente_pozitii = ['Alumn', 'CD', 'Design', 'Edu', 'HR', 'MF']

for poz in lista_departamente_pozitii:
    path_df = poz + '.csv'
    obtine_zile_nastere(path_df, 8, poz)