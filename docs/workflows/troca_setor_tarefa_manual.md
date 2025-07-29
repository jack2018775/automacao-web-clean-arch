# 🛠️ Workflow Manual: Troca de Setor da Tarefa no Sistema Web

Este documento descreve o passo a passo automatizado que o sistema executa para alterar o setor de uma tarefa associada a um processo, dentro da aplicação web.

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

## 📂 Etapa 2: Acessar Processos

1. Clicar no menu de configurações:
   - Elemento: `a[title="Configurações"]`
2. Clicar duas vezes no submenu **"Processo"**:
   - Elemento: `a[rel="cria_grid('#1_grid','wfl_processo','S');"]`

---

## 🔎 Etapa 3: Filtrar Processo pelo ID

1. Clicar na seleção de campo do filtro:
   - Elemento: `span[class="selectedColumn"]`
2. Selecionar o campo **ID**:
   - Elemento: `li[data-valor="wfl_processo.id"]`
3. Digitar o ID desejado e pressionar Enter:
   - Elemento: `input[class="gridActionsSearchInput"]`

---

## 📋 Etapa 4: Abrir Detalhes do Processo

1. Clicar duas vezes na linha que contém o processo filtrado:
   - Elemento: `tr[id="rowIDProcesso"]`

---

## ✅ Etapa 5: Acessar a Aba de Tarefas

1. Clicar na aba de tarefas:
   - Elemento: `a[rel="2"]`

---

## 📝 Etapa 6: Alterar o Setor da Tarefa

1. Clicar duas vezes na linha da tarefa:
   - Elemento: `tr[id="rowIDTarefa"]`
2. Digitar o ID do novo setor:
   - Elemento: `input[id="id_setor"]`

---

## ✅ Resultado Esperado

O setor da tarefa deve ser atualizado corretamente com o novo valor informado.

---

## 📌 Observações

- Este fluxo é utilizado por todas as features que dependem de login e manipulação de tarefas.
- O login é feito uma única vez e mantido durante a execução do fluxo.
