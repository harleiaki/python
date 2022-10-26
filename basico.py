#para instalar o pandas e numpy no pycharm,
#settings, Project:python, project interpreter, clicar no sinal de +, escrever pandas instalar, 
# fazer o mesmo para numpy.
#básico, estruturando pequenos dados.
import pandas

mydataset = {
'cursos'
: ["Dados","Banco","Web"],

'linguagem'
: ['Python','SQL','Javascript']

}
myvar = pandas.DataFrame(mydataset)
print(myvar)
print(myvar['cursos'])
print(myvar['cursos'][0])
print(myvar.loc[0])
print(myvar.loc[0])
