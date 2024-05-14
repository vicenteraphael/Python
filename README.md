<h1 align="center">Estudo de Lógica e Python</h1>

<center>

![a whiz glancing at the sky](https://th.bing.com/th/id/OIG2.XvRDmxoPL274Bo4806r7?w=1024&h=1024&rs=1&pid=ImgDetMain)

</center>

## Índice:

- <a href="#introdução">Introdução</a>
- <a href="descrição">Descrição</a>
- <a href="#calculadoras">Calculadoras</a>
    1. <a href="#1--calculadora-de-sequência-de-fibonacci">Calculadora de Sequência de Fibonacci</a>
    2. <a href="#2-calculadora-de-equação-quadrática">Calculadora de Equação Quadrática</a>
    3. <a href="#3-calculadora-de-fatorial">Calculadora de Fatorial</a>
    4. <a href="#4-calculadora-de-tabuada">Calculadora de Tabuada</a>
    5. <a href="#5--calculadora-convencional-em-desenvolvimento">Calculadora Convencional (em desenvolvimento)</a>
    6. <a href="#analizador-de-triângulos-em-desenvolvimento">Analisador de Triângulos (em desenvolvimento)</a>
    7. <a href="#calculadora-de-progressão-aritmética">Calculadora de Progressão Aritmética</a>
    8. <a href="#calculadora-de-progressão-geométrica">Calculadora de Progressão Geométrica</a>
    9. <a href="#calculadora-de-juros-simples">Calculadora de Juros Simples</a>
    10. <a href="#calculadora-de-juros-compostos">Calculadora de Juros Compostos</a>

- <a href="#trivia-quiz">Trivia Quiz</a>
- <a href="#mais-sobre-o-desenvolvedor">Mais sobre o Desenvolvedor</a>
- <a href="#próximos-passos">Próximos passos</a>

## Introdução:

<p>
print ("Caro(a) Leitor(a),\n\nSeja muito bem-vindo(a) ao Repositório de Estudo de Python do Raphael Vicente\n")<br>
print ("Desejas: \n\n1) Ler a descrição do projeto \n2) Ler a introdução do projeto \n3) Sair") <br>
r = input () <br>
while r != "1" and r != "2" and r != "3": <br> 
    print ("*alternativa inválida*\nDesejas: \n\n1) Ler a descrição do projeto \n2) Ler a introdução do projeto \n3) Sair") <br>
    r = input () <br>

Ops! Perdão, eu passei tanto tempo fritando a cabeça para fazer as gambiarras dos meus códigos <br>
funcionar que eu até esqueci que este é o arquivo README.md do meu projeto... Bem, talvez esta não seja a melhor maneira de se iniciar um arquivo README.md... Mas de qualquer modo... <br><br>
Caro(a) Leitor(a), <br>
Seja muito bem-vindo(a) ao Repositório de Estudo de Python do Raphael Vicente <br><br>
Caso algum dia eu me torne um programador ou desenvolvedor renomado, pessoas dos mais remotos cantos<br>
do mundo poderão apreciar, enquanto batem suas taças, chorosas, o que para sempre <br>
ficará marcado na história da computação como <b> o 1º repositório git de Raphael Vicente! </b><br><br>
Bem, isso daqui tá mais pra um romance do que uma obra realizada por um programador... <br><br>
E eu imagino que você não está aqui para ficar ouvindo histórias, então vamos logo para os projetos. <br><br>
<p>

## Descrição

Repositório criado com o intuito de promover para mim o bom estudo de Python, GitHub, Git Bash e Lógica, equanto minha escola está de greve :/ <br><br>
Transformando-o em um repositório git, eu posso, indiretamente, fornecer este bom estudo para outras pessoas que podem aprender analisando meus códigos e estruturas. <br><br>
E não, eu não sou tarado por calculadoras, é apenas um modo de treinar lógica!

## Calculadoras

### 1 . Calculadora de Sequência de Fibonacci

<p>
Este programa calcula e exibe a Sequência de Fibonacci até um certo número, de acordo com a vontade do usuário. É pedido ao usuário um índice <code>(cont)</code>, que representa o número até o qual se deseja ser calculada a sequência.<br><br>
Por exemplo, tendo <code>cont = 15</code>, será exibida a Sequência de Fibonacci até o 15º número.

</p>

### 2. Calculadora de Equação Quadrática

<p>
Este programa calcula as equações quadráticas do tipo
<code>ax² +/- bx +/- c</code>, ou seja, é preciso de que a equação já esteja simplificada. <br><br>
É pedido que o usuário entre com os valores dos coeficientes <code>(a, b e c</code>, respectivamente) da equação. A partir disto, é calculado o <code>delta (dt)</code> e as raízes da equação: <code>x'</code> e <code>x''</code>.<br><br>
<ul>
<li>Caso <code>a < 0</code>, o programa deverá retornar que os valores dados não formm uma equação quadrática</li>
<li>Caso <code>dt < 0</code>, o programa deverá retornar que a equação não possui solução real.</li>
<li>Caso <code>dt = 0</code>, o programa deverá ponderar que a equação possui raízes iguais.</li>
</ul><br>
Na ausência dos casos citados, o programa deverá retornar apenas o valor de <code>x'</code> e <code>x''</code>.
</p>

### 3. Calculadora de Fatorial

O usuário deverá fornecer um número para que o programa calcule o fatorial deste número.

### 4. Calculadora de Tabuada

<p>
O usuário deverá fornecer o valor para a tabuada desejada <code>(tab)</code> e o índice para esta tabuada <code>(index)</code>.<br><br>
Por exemplo, tendo <code>tab = 5</code> e <code>index = 30</code> , o programa deverá exibir a tabuada do 5 começando pelo 1 <code>(5 * 1 = 5)</code> e parando quando chegar ao 30 <code>(5 * 30 = 150)</code>.
</p>

### 5 . Calculadora Convencional (em desenvolvimento)

<p>
Ela deverá funcionar como uma calculadora convencional (vide o título). No entanto, eu ainda não consegui programá-la para respeitar regra de sinais; nem parêntesis, colchetes e chaves :/
</p>

## 6. Calculadora de Triângulos (em desenvolvimento)

<p>
O usuário deverá fornecer o valor para os 3 lados de, supostamente, um triângulo. A partir disto, o programa deverá dizer se os lados formam:<br><br>
<ul>
    <li>Um triângulo (de acordo com a condição de existência de um triângulo)</li>
    <li>Um Triângulo Equilátero</li>
    <li>Um Triângulo Isósceles</li>
    <li>Um Triângulo Escaleno</li>
    <li>Um Triângulo Retângulo</li>
</ul> <br>
Após esta checagem, o programa deverá pedir o valor dos ângulos para, deste modo, informar:<br><br>
<ul>
<li>Seno</li>
<li>Cosseno</li>
<li>Tangente</li>
</ul>
</p>

## 7. Calculadora de Progressão Aritmética
 
## 8. Calculadora de Progressão Geométrica

## 9. Calculadora de Juros Simples

## 10. Calculadora de Juros Compostos

## Trivia Quiz

<p>
Trata-se de um Quiz de Conhecimentos Gerais, descontraído, com 10 perguntas simples, feitas por mim.
</p>

## Mais sobre o desenvolvedor

<p>
Meu nome é Raphael Vicente de Oliveira.<br>
Atualmente, sou aluno do Instituto Federal de São Paulo.<br>
Sou um garoto cheio de grandes sonhos e ambições.<br>
Pretendo atuar na área de Programação / Tecnologia da Informação e cursar Ciências da Computação.<br><br>
Tenho interesses nas mais diversas áreas do conhecimento, mas as principais são:<br><br>
<ul>
<li>Programação</li>
<li>Matemática</li>
<li>Estudo de idiomas</li>
<li>Música e Piano</li>
<li>Poesia</li>
</ul>
</p>

## Próximos passos

<p>
Após terminar o Analisador de Triângulos e corrigir a Calculadora Convencional, pretendo, ainda neste repositório:<br><br>
<ul>
<li>Condensar todas as calculadoras em um único arquivo</li>
<li>Criar um arquivo que leia um texto e informe quantas palavras tem</li>
<ul>
</p>