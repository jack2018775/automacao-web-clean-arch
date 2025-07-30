# 🛠️ Workflow Manual: Alterar Setor do Parâmetro da OS no Sistema Web

Este documento descreve o passo a passo automatizado que o sistema executa para alterar o setor de um **parâmetro da Ordem de Serviço (OS)** dentro da aplicação web.

---

## 🔐 Etapa 1: Login

1. Acessar a página de login.
2. Preencher os campos:
   - **Email**
   - **Senha**
3. Clicar em "Próximo" e depois em "Entrar".
4. Se existir o botão de 2FA:
   - Elemento: `button[class="styles-module__button2FACancel___ahPHx"]`
   - Clicar em **"Lembrar-me por 10 dias"**, se disponível.

---

## ⚙️ Etapa 2: Acessar Configurações de Ordem de Serviço

1. Clicar no menu **Configurações**:
   - Elemento: `a[title="Configurações"]`
2. Aguardar a abertura do submenu:
   - Elemento: `div[id="menua648352b6f304a5155942c5a60d1dc15"]`
3. Clicar duas vezes em **"Configuração de Ordem de Serviço"**:
   - Elemento: `a[rel="cria_grid('#1_grid','wfl_parametro_oss','S');"]`

---

## 🔎 Etapa 3: Filtrar Parâmetro pelo ID

1. Clicar na seleção de campo do filtro:
   - Elemento: `span[class="selectedColumn"]`
2. Selecionar a coluna **ID**:
   - Elemento: `li[data-nome="ID"]`
3. Digitar o ID desejado e pressionar Enter:
   - Elemento: `input[class="gridActionsSearchInput"]`

---

## 📋 Etapa 4: Acessar Detalhes do Parâmetro

1. Clicar duas vezes na linha correspondente ao ID pesquisado:
   - Elemento: `tr[id="rowIDQUEFOIPESQUISADO"]`

---

## 📝 Etapa 5: Alterar o Setor do Parâmetro

1. Localizar o campo de edição de setor:
   - Elemento: `input[id="id_setor"]`
2. Digitar o ID do novo setor (ex: `200`).

---

## ✅ Resultado Esperado

O setor do parâmetro da OS deve ser atualizado corretamente com o novo valor informado.

---

## 📌 Observações

- O login é feito uma única vez e utilizado por todas as features que exigem autenticação.
- Este fluxo é parte da automação de alteração de parâmetros em ordens de serviço, usada para controle e roteamento de processos no sistema.
