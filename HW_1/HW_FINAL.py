import pandas as pd

x=int(input('本金(萬）'))
y=int(input('期數（年）'))
z=float(input('年利率(%)'))
    
PV=x*10000      
Y=y        
m=12         
n=m*Y        
r=z*0.01      

Principal=round(PV/n)
PV_F=PV
Principal_F=[]
interest_F=[]
TOTAL = []
TOTAL_F=[]
for j in range(1,n+1):
  Principal_F.append(Principal) 
  interest_i=round(PV*r/m)
  interest_F.append(interest_i)
  TOTAL_0=round(Principal+ interest_i)
  TOTAL.append(TOTAL_0)
  ALL_TO=sum(TOTAL)
  TOTAL_F.append(ALL_TO)
  PV=PV-Principal
  
ADJ=n*Principal-PV_F
ADJ_F=Principal-ADJ
Principal_F.pop()
Principal_F.append(ADJ_F)
ADJ_TF=TOTAL_F[n-1]
TOTAL_F.pop()
ADJ_TFF=ADJ_TF-ADJ
TOTAL_F.append(ADJ_TFF)
interest_F.pop()
ADJ_IN=round(ADJ_F*r/m)
interest_F.append(ADJ_IN)



pd.set_option("display.max_columns", None)
final = {
    "本金 ":Principal_F, 
    "利息 ": interest_F,
    "本金利息累計": TOTAL_F,
}
pd.set_option("display.max_row", None)
df = pd.DataFrame(final)
df.index=df.index+1
print(df)

