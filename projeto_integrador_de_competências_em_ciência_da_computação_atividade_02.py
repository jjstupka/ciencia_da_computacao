"""PROJETO INTEGRADOR DE COMPETÊNCIAS EM CIÊNCIA DA COMPUTAÇÃO - Atividade 02.ipynb

contador=0
obrigatorio=0
facultativo=0
naovota=0
controle=0

#neste bloco 
controle = int(input("Você deseja cadastrar algum usuário? Digite 1-sim 2-não:"))

#enquanto usuário digitar 1, vai executar os próximos testes lógicos:
while controle == 1:
  #agora o programa pede a idade do usuário:
  idade = int(input("Digite a tua idade: ")) 
    
  if idade >= 18 and idade < 70:
          obrigatorio += 1
          contador += 1  
  elif idade == 16 or idade==17 or idade>=70:1
          facultativo += 1
          contador += 1  
  elif idade <16:
          naovota += 1
          contador += 1 

#este bloco exibe a contagem parcial enquanto os cadastros estão sendo feitos
  print("Número de Habitantes: ", contador)
  print("Número de Eleitores obrigatórios: ",obrigatorio)
  print("Número de Eleitores Facultativos: ",facultativo)
  print("Número de Habitantes que não vota é: ",naovota)

  controle = int(input("Você deseja cadastrar algum usuário? Digite 1-sim 2-não:"))

#este bloco exibe a contagem final de usuarios cadastrados
if controle==2:
  print("Número de Habitantes Cadastrados: ", contador)
  print("Número de Eleitores obrigatórios cadastrados: ",obrigatorio)
  print("Número de Eleitores Facultativos cadastrados: ",facultativo)
  print("Número de Habitantes que não vota cadastrado é: ",naovota)

else:
  print("Valor inválido.")
