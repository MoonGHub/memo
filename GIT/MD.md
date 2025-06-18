# GIT - MD

# Big title : `#`

## A little Big title : `##`

### More smaller : `###`

#### ... : `####`

##### .. : `#####`

###### Most smaller one : `######`

---

Drawing Line : `---` or `***`

---

- 단락 -

* 단락 \*
  - 1 tab
    - 2 tab

<br>

---

**Bold Text**: `**TEXT**` or `__TEXT__`

_italic_: `*TEXT*` or `_TEXT_`

**_Bold and Italic_**: `***TEXT***` or `___TEXT___`

~~strikethrough~~: `~~TEXT~~`

`<sup>`: 윗 첨자<sup>윗윗</sup>

`<sub>`: 아랫 첨자<sub>아랫아랫</sub>

> Quote : `>`
>
> > Quote : `>>`

---

[기본 서식 구문 - 경고](https://docs.github.com/ko/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts)

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

---

Inline code is used `like this` using <strong style="background:#8056ff;color:yellow">``</strong>

Code Block is the followings :

- [supported language](https://docs.github.com/en/contributing/writing-for-github-docs/using-markdown-and-liquid-in-github-docs#code-sample-syntax-highlighting)

<div style="background:#6a69f1;border-radius:5px;">
    <span>```language</span></br>
    <span>CODE</span></br>
    <span>```</span></br>
</div>

<br>

```javascript
console.log("print");
```

---

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

---

- [x] #739 `#0d1117`
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
- ```markdown
  - [x] #739 `#0d1117`
  - [ ] https://github.com/octo-org/octo-repo/issues/740
  - [ ] Add delight to the experience when all tasks are complete :tada:
  ```

---

## Link

- [test](naver.com) : `[test](naver.com)`
- <a href="#">link</a> : `<a href="#">link</a>`
- `<img src="https://cdnb.artstation.com/p/assets/images/images/025/923/221/medium/-goblin-export.jpg?1587352888" width="10%" height="10%"/>`\
  <img src="https://cdnb.artstation.com/p/assets/images/images/025/923/221/medium/-goblin-export.jpg?1587352888" width="10%" height="10%"/>
- `![image](https://cdnb.artstation.com/p/assets/images/images/025/923/221/medium/-goblin-export.jpg?1587352888)`\
  ![image](https://cdnb.artstation.com/p/assets/images/images/025/923/221/medium/-goblin-export.jpg?1587352888)

<br>

---

## 테이블

- ```markdown
  | 헤더1   |  헤더2  |   헤더3 |
  | :------ | :-----: | ------: |
  | 왼쪽    |  중앙   |  오른쪽 |
  | 데이터1 | 데이터2 | 데이터3 |
  ```

  | 헤더1   |  헤더2  |   헤더3 |
  | :------ | :-----: | ------: |
  | 왼쪽    |  중앙   |  오른쪽 |
  | 데이터1 | 데이터2 | 데이터3 |

- 테이블도 태그로 가능, 대부분 사용 가능..

    <table style="border:1px solid black">
        <thead style="background:#956e98">
            <tr>
                <th>th1</th>
                <th>th2</th>
                <th>th3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>td1</td>
                <td>td2</td>
                <td>td3</td>
            </tr>
        </tbody>
    </table>

<br>

---

escape char : \

---

<br>

$ 수식 $

[참고](https://velog.io/@d2h10s/LaTex-Markdown-%EC%88%98%EC%8B%9D-%EC%9E%91%EC%84%B1%EB%B2%95)

- `$x + y = 10$`\
   $x + y = 10$
- `$$x + y = 10$$`
  $$x + y = 10$$

- 기본 연산 기호

  - `y = A \times x + B`\
    $y = A \times x + B$

- 기타 기호

  - `$\gt$ and $\lt$`\
    $\gt$ and $\lt$
  - `$\geq$ and $\leq$`\
    $\geq$ and $\leq$
  - `$\fallingdotseq$`\
    $\fallingdotseq$
  - `$\pm$`\
    $\pm$
  - `$\larr$ and $\rarr$ or $\to$`\
    $\larr$ and $\rarr$ or $\to$
  - `$\cdots$ and $ldots$`\
    $\cdots$ and $\ldots$

- 띄어쓰기

  - `스페이스`는 띄어쓰기 적용 안됨
  - `$test\, test$`\
    $test\, test$
  - `$test\; test$`\
    $test\; test$
  - `$test\quad test$`\
    $test\quad test$

- 첨자 - 밑, 지수

  - `$a_1, a^2, a_1^2$`\
    $a_1, a^2, a_1^2$
  - `$y_i=x_i^3+x_{i-1}^2+x_{i-2}$`\
    $y_i=x_i^3+x_{i-1}^2+x_{i-2}$

- 분수

  - `$s^2+2s+s\over s+\sqrt s+1$`\
    $s^2+2s+s\over s+\sqrt s+1$
  - `$\frac{1+s}{s(s+2)}$`\
    $\frac{1+s}{s(s+2)}$

- 절대값

  - `$\vert x \vert$`\
    $\vert x \vert$
  - `$\left\lvert \frac{s^2+1}{s^3+2s^2+3s+1} \right\rvert$`\
    $\left\lvert \frac{s^2+1}{s^3+2s^2+3s+1} \right\rvert$

- Sin 및 Log

  - `$\log_{10}{(x+1)}$`\
    $\log_{10}{(x+1)}$
  - `$A\sin(bx+c)$`\
    $A\sin(bx+c)$

- 극한 및 시그마

  - `$\displaystyle\lim_{s\rarr\infin}{s^2}$`\
    $\displaystyle\lim_{s\rarr\infin}{s^2}$
  - `$\displaystyle\sum_{i=0}^{\infin}{(y_i-t_i)^2}$`\
    $\displaystyle\sum_{i=0}^{\infin}{(y_i-t_i)^2}$

- 행렬

  - `$\begin{matrix}1&2\\3&4\\ \end{matrix}$`\
    $\begin{matrix}1&2\\3&4\\ \end{matrix}$
  - `$\begin{pmatrix}1&2\\3&4\\ \end{pmatrix}$`\
    $\begin{pmatrix}1&2\\3&4\\ \end{pmatrix}$
  - `$\begin{bmatrix}1&2\\3&4\\ \end{bmatrix}$`\
    $\begin{bmatrix}1&2\\3&4\\ \end{bmatrix}$
  - `$\begin{Bmatrix}1&2\\3&4\\ \end{Bmatrix}$`\
    $\begin{Bmatrix}1&2\\3&4\\ \end{Bmatrix}$
  - `$\begin{vmatrix}1&2\\3&4\\ \end{vmatrix}$`\
    $\begin{vmatrix}1&2\\3&4\\ \end{vmatrix}$
  - `$\begin{Vmatrix}1&2\\3&4\\ \end{Vmatrix}$`\
    $\begin{Vmatrix}1&2\\3&4\\ \end{Vmatrix}$
