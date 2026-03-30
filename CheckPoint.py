alunos = " Matheus, João, Ricardo, Cesar, Mariana "


nota_Aluno = (f"Qual aluno gostaria de digitiar a nota ? {alunos}\n")
input (nota_Aluno)
cp1 = float(input("Nota do Primeiro CheckPoint:\n"))
cp2 = float(input("Nota do Segundo CheckPoint:\n"))
cp3 = float(input("Nota do Terceiro CheckPoint:\n"))
spr1 = float(input("Nota da Sprint 1:\n"))
spr2 = float(input("Nota do Sprint 2:\n"))
globals = float(input("Nota da Global Solution: \n "))

#media primeiro semestre 

if cp1 <= cp2 and cp1 <=cp3:  
    menorNota = cp1
elif cp2 <= cp1 and cp2 <= cp3:
    menorNota = cp2    
else:
    menorNota = cp3

media = ( (cp1 + cp2 + cp3 - menorNota +spr1+spr2) /4) * 0.4 + globals * 0.6

media_peso = media * 0.4

print("===============================A Media do Aluno foi:===============================\n")
print("Media do semestre:", format(media, ".1f"))
print("Media com peso:", format(media_peso, ".1f")) 
