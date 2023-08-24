import pickle
import pandas as pd
import numpy as np

df=pd.read_csv("C:\\Users\\Manan\\Downloads\\Symptom-severity.csv")

inp_symp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

model_symp = pickle.load(open("C:\\Users\\Manan\\PycharmProjects\\hackathon\\vitals\\model", 'rb'))

def symptommodel(symp):
    print(symp)
    for i in range(3):
        df_new = df.loc[df.Symptom == symp[i]]
        inp_symp[i] = df_new.iloc[0, 1]
    input_symp = np.array(inp_symp)
    return (model_symp.predict([input_symp]))