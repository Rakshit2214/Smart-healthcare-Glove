import pickle

att = [[98, 62, 18, 131, 89, 98]]
print(att)

scalar = pickle.load(open("C:\\Users\\Manan\\PycharmProjects\\hackathon\\vitals\\scalar.pkl", 'rb'))
model_vitals = pickle.load(open("C:\\Users\\Manan\\PycharmProjects\\hackathon\\vitals\\model_hscore", 'rb'))

def vitalmodel(att):
    # from sklearn.preprocessing import StandardScaler
    # scalar = StandardScaler()
    # inp = scalar.transform(att)
    att = scalar.transform(att)
    return model_vitals.predict(att)

print(vitalmodel(att))
