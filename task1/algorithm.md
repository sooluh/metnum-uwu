# Algorithm

<table>
<tr>
<td>
<strong>Judul</strong>
</td>
<td>:</td>
<td>PROGRAM_ALGORITMA_BISECTION</td>
</tr>
<tr>
<td>
<strong>Deklarasi</strong>
</td>
<td>:</td>
<td>
f(x) : function<br>
a : integer<br>
b : integer<br>
e : integer = 10^-4 // nilai toleransi<br>
n : integer = 100 // batasan iterasi<br>
</td>
</tr>
</table>

**Algoritma :**

```
def f(x)

read a, b, e dan n

if f(a) x f(b) > 0 then
else
  step = 1
  condition = true

  while condition = true then
    c = (a + b) / 2

    if f(a) x f(c) < 0
      b = c
    else
      a = c

    step + 1
    condition = |f(c)| > e dan step <= n

  print ditemukan akar = c
```

# Flowchart

```mermaid
flowchart TD
  A(["start"]) --> B[["definisikan fungsi f(x)"]];
  B --> C["tentukan nilai a, b, nilai toleransi\n(e = 10^-4) dan batasan iterasi (n = 100)"];
  C --> D{"f(a) x f(b) > 0"};
  D --> |"false"| E["step = 1\ncondition = true"];
  E --> F{"condition = true"};
  F --> |"true"| G["c = (a + b) / 2"];
  G --> H{"f(a) x f(c) < 0"};
  H --> |"true"| I["b = c"];
  H --> |"false"| J["a = c"];
  I --> K["step + 1\ncondition = |(f(c)| > e dan step <= n"];
  J --> K;
  K --> F;
  F --> |"false"| L[/ditemukan akar = c/];
  D --> |"true"| M(["finish"]);
  L --> M;
```
