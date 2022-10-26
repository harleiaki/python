#para instalar o pandas e numpy no pycharm,
#settings, Project:python, project interpreter, clicar no sinal de +, escrever pandas instalar,
# fazer o mesmo para numpy.

import pandas
import numpy as np
mydataset = {
'cursos'

: ["Dados", np.nan,"Web"],

'linguagem'

: [np.nan,'SQL','Javascript']

}
df = pandas.DataFrame(mydataset)
print(df)
print(df)

df.fillna('Sem dado'

, inplace = True)

print(df)
print(df)

df['linguagem'].fillna('Sem dado'

, inplace =

True)

print(df)