<h3>Sintaxe básica:</h3>
<br>
string[início:fim:passo]
<br>
<ul>
  <li>início: índice onde começa o fatiamento (inclusivo).</li>
  <li>fim: índice onde termina o fatiamento (exclusivo).</li>
  <li>passo: define o intervalo entre caracteres.</li>
</ul>
<br>
<h3>Exemplos práticos:</h3>
s = "Python"

<p>print(s[0:4])     # 'Pyth' (pega do índice 0 ao 3)
<p>print(s[:3])      # 'Pyt' (do início até o índice 2)
<p>print(s[2:])      # 'thon' (do índice 2 até o final)
<p>print(s[::2])     # 'Pto' (pula de 2 em 2)
<p>print(s[::-1])    # 'nohtyP' (inverte a string)

