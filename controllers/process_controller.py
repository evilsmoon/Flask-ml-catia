import re
import nltk
import numpy as np
from nltk.stem import SnowballStemmer
import re
from controllers import jaccard_controller as jcc
from controllers import coseno_controller as csc
from controllers import read_text_controller as rtc
from controllers import nlp_controller as nlp_c
import numpy as np
import json



def predict_text(text):
    nltk.download('stopwords')
    def stemmerBolsaPalabras(list_text):
        data =[]
        st = SnowballStemmer('spanish')
        for i,temp in enumerate(list_text):
          data.append( re.sub('[^A-Za-záéíóúñ]+',' ',st.stem(temp)))
        return data
    txt_clean = []
    txt_clean.append(text)
    
    txt_nlp = nlp_c.lowercase(txt_clean)
    txt_nlp = nlp_c.deleteChars(txt_nlp)
    txt_nlp = nlp_c.tokenizertext(txt_nlp)
    txt_nlp = nlp_c.stemmer(txt_nlp)
    txt_nlp = nlp_c.stopWords(txt_nlp,1)
    # print(txt_nlp)
    #obtener bolsa de palabras
    dic_epc = rtc.readTxt("models/data/dic_epc.txt")
    dic_mbm = rtc.readTxt("models/data/dic_mbm.txt")
    dic_ecc  = rtc.readTxt("models/data/dic_ecc.txt")
    print(dic_epc)
    print(dic_mbm)
    print(dic_ecc)
    dic_epc_SBP = stemmerBolsaPalabras(dic_epc)
    dic_mbm_SBP = stemmerBolsaPalabras(dic_mbm)
    dic_ecc_SBP  = stemmerBolsaPalabras(dic_ecc)
    print(dic_epc_SBP)
    print(dic_mbm_SBP)
    print(dic_ecc_SBP)

    jacc_epc_mbm_ec = jcc.jaccard(txt_nlp[0],[dic_epc_SBP,dic_mbm_SBP,dic_ecc_SBP])

    print(jacc_epc_mbm_ec)
    cos_epc_mbm_ec   = np.array([csc.coseno(txt_nlp,dic_epc_SBP) ,csc.coseno(txt_nlp,dic_mbm_SBP) ,csc.coseno(txt_nlp,dic_ecc_SBP)])
    print(cos_epc_mbm_ec)
    txt_nlp.clear()

    return json.dumps({"jacc_epc":jacc_epc_mbm_ec[0],"jacc_mbm":jacc_epc_mbm_ec[1],"jacc_ec":jacc_epc_mbm_ec[2],"cos_epc":cos_epc_mbm_ec[0],"cos_mbm":cos_epc_mbm_ec[1],"cos_ec":cos_epc_mbm_ec[2]
})













