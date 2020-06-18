
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
BB=pd.read_excel("0050component.xlsx")
BB.columns=["a","number"]
AAA=pd.DataFrame(columns=["High","Low","Open","Close","Volume","Adj Close","5day mean","20day mean","60day mean","5day std","20day std","60day std","5day mean delta","5day mean delta delta","20day mean delta","20day mean delta delta","60day mean delta","60day mean delta delta","deal 5day percent","index"])
for x in BB["number"]:
    df=web.DataReader(x,"yahoo", start="2019-1-18", end="2020-6-18")
    A=df["Open"]
    AA=df["Close"]
    B=A.rolling(window=5).mean()
    C=A.rolling(window=20).mean()
    D=A.rolling(window=60).mean()
    E=A.rolling(window=5).std()
    F=A.rolling(window=20).std()
    G=A.rolling(window=60).std()
    H=-B.diff(periods=-1)
    I=-H.diff(periods=-1)
    J=-C.diff(periods=-1)
    K=-J.diff(periods=-1)
    L=-D.diff(periods=-1)
    M=-L.diff(periods=-1)
    N=-100*AA.diff(periods=-5)/AA


    df["5day mean"]=B
    df["20day mean"]=C
    df["60day mean"]=D
    df["5day std"]=E
    df["20day std"]=F
    df["60day std"]=G
    df["5day mean delta"]=H
    df["5day mean delta delta"]=I
    df["20day mean delta"]=J
    df["20day mean delta delta"]=K
    df["60day mean delta"]=L
    df["60day mean delta delta"]=M
    df["deal 5day percent"]=N
    #df["strategy"]=df["5day mean"]>df["20day mean"]+0.5*df["20day std"]
    fi1=(df["5day mean delta"]>0)&(df["5day mean delta delta"]>0)
    fi2=(df["20day mean delta"]>0)&(df["20day mean delta delta"]>0)
    fi3=(df["60day mean delta"]>0)&(df["60day mean delta delta"]>0)
    fi4=(df["5day mean"]>df["20day mean"])
    fi5=(df["20day mean"]>df["60day mean"])
    result=df[fi1&fi2&fi3&fi4&fi5]
    #    result["index"]=result.index
    AAA=AAA.append(result)
print(AAA["deal 5day percent"].describe())

"""
    for y in ["15","16","17","18"]:
        if "2020-06-"+y in result["index"]:
            print("2020-06-"+y+" "+x)    
    else: 
        print("none")
"""
#print(result["deal 5day percent"].describe())
#print(result)
#result.to_excel("2330result.xlsx")
#filter1=(df["strategy"]==True)
#filter2=(df["deal 5day"]<0)
#A.plot()
#A.rolling(window=5).mean().plot()
#A.rolling(window=20).mean().plot()
#A.rolling(window=60).mean().plot()
#B=A.diff(periods=3)
#r=100*B/A
#r[-100:].plot()
#plt.show()