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
    11. <a href="#11-calculadora-de-médias">Calculadora de Médias</a>
    12. <a href="#12-calculadora-de-dsp-mmc-mdc">Calculadora de DSP (Divisores Sequênciais e Números Primos), MMC, MDC </a>
- <a>Conversor DBOH (Decimal, Binário, Octal e Hexadecimal)</a>
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

### 6. Calculadora de Triângulos (em desenvolvimento)

<p>
O usuário deverá fornecer o valor para os 3 lados de, supostamente, um triângulo. A partir disto, o programa deverá dizer se os lados formam:<br><br>
<ul>
    <li>Um triângulo (de acordo com a condição de existência de um triângulo);</li>
    <li>Um Triângulo Equilátero;</li>
    <li>Um Triângulo Isósceles;</li>
    <li>Um Triângulo Escaleno e</li>
    <li>Um Triângulo Retângulo.</li>
</ul> <br>
Após esta checagem, o programa deverá pedir o valor dos ângulos para, deste modo, informar:<br><br>
<ul>
<li>Seno;</li>
<li>Cosseno e</li>
<li>Tangente.</li>
</ul>
</p>

### 7. Calculadora de Progressão Aritmética

<p>
Aparentemente, nada demais. É pedido:
<ul>
<li>Primeiro número da sequência (a1);</li>
<li>Último número da sequência (an) e</li>
<li>Razão da sequência (r)</li>
</ul>
A fim de calcular e exibir a sequência inteira. Também é possível encontrar um termo n (an); a razão (r) e a soma dos termos da sequência (Sn), em que::
<ul>
<li><code>an = a1 + (n - 1) * r</code></li>
<li><code>r = an - a(n-1)</code></li>
<li><code>Sn = ((a1 + an) * n) / 2</code></li>
</ul>
</p>
 
### 8. Calculadora de Progressão Geométrica

<p>
Aparentemente, nada demais. É pedido:
<ul>
<li>Primeiro número da sequência (a1);</li>
<li>Último número da sequência (an) e</li>
<li>Razão da sequência (r)</li>
</ul>
A fim de calcular e exibir a sequência inteira. Também é possível encontrar um termo n (an); a razão (r) e a soma dos termos da sequência (Sn), em que::
<ul>
<li><code>an = a1 + (n - 1) * r</code></li>
<li><code>r = an - a(n-1)</code></li>
<li><code>Sn = ((a1 + an) * n) / 2</code></li>
</ul>
</p>

### 9. Calculadora de Juros Simples

<p>
A calculadora cumpre sua finalidade principal, que é calcular juros e montante a partir das fórmulas <code>J = (C + i + t) 100</code> e <code>M = C + J</code>. <br><br>
No entanto, eu manipulei algebricamente esta fórmula de modo a tornar possível descobrir o resto das variáveis, me deparando, assim, com as seguintes fórmulas:

<ul>
<li><code>C = (100 * J) / (i * t)</code> ou</li>
<li><code>C = M - J</code>;</li>
<li><code>i = (100 * J) / (C * t)</code> e</li>
<li><code>t = (100 * J) / (C * i)</code>.</li>
</ul>
</p>

### 10. Calculadora de Juros Compostos

<p>
Novamente, eu peguei as fórmulas <code>M = C * (1 + i ^ t)</code> e <code>M = C + J</code>, usei e depois as manipulei, de modo a encontrar: <br>
<ul>
<li><code>J = (C * (1 + i) ** t -) C</code>;</li>
<li><code>C = M / (1 + i) ** t</code> ou</li>
<li><code>C = J / (((1 + i) ** t) - 1)</code>;</li>
<li><code>i = (M / C) ** (1 / t) - 1</code> e</li>
<li><code>t =</code>.</li>
</ul>
</p>

### 11. Calculadora de Médias

<p>
Trata-se de uma calculadora para Média Aritmética, Média Ponderada, Moda e Mediana, operações que durante a maior parte do tempo, ninguém liga, exceto para quem é estudante e/ou participa de concursos. Para refrescar vossa memória:
<ul>
<li>Média Aritmética: Soma dividida pela quantidade de termos: <code>(x + y + z) / 3</code>;</li>
<li>Média Ponderada: Soma em que cada termo tem um 'peso', dividida pela soma dos pesos: <code>(5 * x + 2 * y + 3 * z) / 10</code>;</li>
<li>Moda: A moda de uma sequência é o número que mais se repete. O nome já diz tudo: é o que tá na moda! Na sequência: <code>x, x, z, y, y, x, y, z, x, y, y</code>; a moda é o <code>y</code> (se houver 'empate' entre termos, a moda deverá ser todos os termos em empate) e</li>
<li>Mediana: Dada uma sequência em ordem crescente, se a sequência for ímpar, como <code>2, 5, 9, 12, 13</code> (há uma quantidade ímpar de termos), a mediana é o termo do meio; neste caso, o <code>9</code>. Se a sequência for par, a mediana será a média aritmética dos termos do meio.</li>
</ul>
</p>

### 12. Calculadora de DSP, MMC, MDC

<p>
Acredito que este foi o programa mais difícil e demorado de se realizar, o que mais me fez esquentar a cabeça e perder os cabelos...<br><br>
Acredito também, que, neste momento, você deve estar se perguntando: "Mas o que diacho seria uma 'Calculadora de Divisores Sequênciais e Números Primos (DSP)'?". <br><br>
Pois bem, trata-se de uma calculadora para uma finalidade muito específica, por isso o nome longo e estranho e a necessidade de uma sigla -- aliás, acredito que esta deve ser a única existente para tal finalidade. "Mas que finalidade é esta?" você me pergunta. <br><br>
Vamos à explicação: dada uma sequência de números, ela deverá calcular quantos e quais termos da sequência são divisíveis pelos números escolhidos pelo usuário. Para o usuário não ter que cansar seus delicados dedos digitando a sequência de ponta a ponta, nós a tratamos como uma Progressão Aritmética, em que é necessário apenas: <br>
<ul>
<li>O primeiro número da sequência (a1)</li>
<li>O último número da sequência (an)</li>
<li>A razão da sequência (r)</li>
</ul><br>
Então, a calculadora calcula por si só a sequência númerica inteira -- por isso eu te peço, encarecidamente, que não entre com números estrondosos para o cálculo da sequência, a não ser que você queira gastar uma eternidade do seu precisoso tempo e da CPU da sua máquina para fazer um cálculo que, convenhamos, será desnecessário. Após este cálculo inicial, é pedido que o usuário entre com os divisores e o programa logo fará a mágica acontecer. <br><br>
Você deverá notar que os divisores são tratados com 'e'. Isto é, ao entrar com 2, 3 e 4; por exemplo, o programa retornará os divisores de 2 E 3 E 4 presentes na sequência. Ou seja, os divisores de 2 * 3 * 4 = 24 <br><br>
Quanto à parte que diz respeito aos números primos, a ideia é a mesma: dada uma sequência númerica, o programa calcula quantos e quais termos são números primos.<br><br>
Mas a diversão ainda não acaba por aqui, pois esta belezura também calcula MDC e MMC <br><br>
Como são operações já manjadas, irei detalhar apenas como se dá a checagem e os casos para as duas operações. <br><br>
<li><b>MDC:</b> Para todo e qualquer cálculo, sempre existirá os seguintes 3 casos: <br><br>
- Caso 1: O MDC é o menor número. Tomemos os números 60, 45 e 15. Inicialmente, verificamos se o menor número da seqûencia é divisível por todos os outros. Neste caso, já matamos a questão por aqui, pois todos os números dessa sequência são divisíveis por 15. Já para os números 60 45 20, vamos para o <br><br>
- Caso 2: O MDC não é o menor número. Se o menor número não for o MDC da sequência, certamente o MDC deverá ser algum dos divisores do menor número da sequência, neste caso, do 20 -- Veja que, na verdade, o MDC não precisa ser necessariamente um divisor do menor número, pode ser de qualquer um da sequência. Mas fazer a checagem com o menor número é mais fácil e mais rápido -- Para isto, a calculadora literalmente calcula todos os divisores do menor número da sequência e verifica um a um se eles são divisíveis pelo resto da sequência. Neste caso, os números divisores de 20 são: 2, 4, 5 e 10. Como a checagem se dá do maior para o menor termo, temos, então, que o primeiro divisor do menor número da sequência que for divisível, necessariamente, por todos os número da sequência, consagramos-o como 'O MDC da Sequência'. Portanto, o MDC de 60, 45 e 20 será o 10. Entretanto, de forma lógica, pode ser que não se haja um divisor comum entre todos os números da sequência, Como é o caso dos números 3, 15, 21 e 14. Entramos, então, no <br><br>
- Caso 3: Os termos da sequência são primos entre si. Nem tudo são rosas, amigo(a), nem sempre poderemos confirmar asseguradamente que haja um MDC de uma sequência númerica, às vezes nem sequer um mero divisor comum entre eles.<br><br>
Você notará que, não precisa haver, necessariamente, um número primo para que os termos da sequência sejam primos entre si. Mas é claro que, na existência de um, é anulada a existência de um MDC também.
</li><br>
<li><b>MMC:</b> O Cálculo do MMC é basicamente o mesmo do MDC só que ao contrário. Tomamos o maior número da sequência e calculamos os seus múltiplos até encontrarmos algum que seja divisível por todos os números da sequência -- sim, literalmente a tabuada do maior número. Fazemos assim, pois, novamente, a checagem se torna mais fácil e mais rápida --; Fazemos isso do menor para o maior número. Então, para o primeiro número que der certo, batizamos-o de 'O MMC da Sequência'. <br><br>
Exemplo para os números: 22, 13. Calculando os múltiplos de 22: 22, 44, 66, 88, 110, 132, 154, 176, 198, 220, 242, 264, 286... Opa!... 286 % 13 = 0. Então o MMC de 22 e 13 é o 286!
</li><br><br>
Bom, se você leu até aqui, então agora sim: a diversão deste programa acaba por aqui...
</p>

## Conversor DBOH

<p>
Trata-se de mais uma invenção genuína minha que também precisou de uma sigla a fim de evitar um nome gigante.<br><br>
É um conversor para as bases Decimal, Binária, Octal e Hexadecimal. Se você manja de Análise Combinatória, já deve ter sacado que existem 4 * 3 = 12 tipos de conversões, a saber:
<ol type=1>
<li>Decimal para Binário</li>
<li>Decimal para Octal</li>
<li>Decimal para Hexadecimal</li>
<li>Binário para Decimal</li>
<li>Binário para Octal</li>
<li>Binário para Hexadecimal</li>
<li>Octal para Decimal</li>
<li>Octal para Binário</li>
<li>Octal para Hexadecimal</li>
<li>Hexadecimal para Decimal</li>
<li>Hexadecimal para Binário</li>
<li>Hexadecimal para Octal</li>
</ol>
Achei que fosse dar um trampo danado fazer isso aqui funcionar devidamente. Mas eu estava enganado. Foi absurdamente fácil por conta da existência de funções já presentes na sintaxe do Python ao meu favor. Tais como <code>int(x, y)</code> e <code>format(x, "y")</code>.
</p>

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