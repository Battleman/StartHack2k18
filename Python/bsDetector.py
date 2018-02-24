import pickle
def load_dico():
    with open('bsDetectorDico.pkl', 'rb') as f:
        return pickle.load(f)
		
def bsDetctorAdvice (url , bsDico) :
    return bsDico.get(url,'Unknown')