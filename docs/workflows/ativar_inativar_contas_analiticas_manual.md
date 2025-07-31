Segue o workflow no mesmo padrão do seu exemplo, mas adaptado para a **ativação/inativação de contas contábeis analíticas**.

---

# 🛠️ Workflow Manual: Ativar/Inativar Contas Contábeis Analíticas no Sistema Web

Este documento descreve o passo a passo automatizado que o sistema executa para **ativar** ou **inativar** contas contábeis analíticas dentro da aplicação web.

---

## 🔐 Etapa 1: Login

1. Acessar a página de login.
2. Preencher os campos:

   * **Email**
   * **Senha**
3. Clicar em **"Próximo"** e depois em **"Entrar"**.
4. Se existir o botão de 2FA:

   * Elemento: `button[class="styles-module__button2FACancel___ahPHx"]`
   * Clicar em **"Lembrar-me por 10 dias"**, se disponível.

---

## 📂 Etapa 2: Acessar Listagem de Contas Contábeis Analíticas

1. Clicar no menu **Contabilidade**:

   * Elemento: `div[id="menu5f45d90b6928018b9dbea1365233ee96"]`
2. Dar **duplo clique** no submenu **"Contas Contábeis Analíticas"**:

   * Elemento: `a[rel="cria_grid('#1_grid','planejamento_analitico','N');"]`

---

## 🔎 Etapa 3: Filtrar Conta Contábil pelo ID

1. Clicar na seleção de campo do filtro:

   * Elemento: `span[class="selectedColumn"]`
2. Selecionar o campo **ID**:

   * Elemento: `li[data-valor="planejamento_analitico.id"]`
3. Digitar o ID desejado e pressionar **Enter**:

   * Elemento: `input[class="gridActionsSearchInput"]`

---

## 📋 Etapa 4: Abrir Detalhes da Conta Contábil Analítica

1. Clicar duas vezes na linha que contém a conta contábil filtrada:

   * Elemento: `tr[id="rowIDProcesso"]`

---

## 📝 Etapa 5: Alterar Status da Conta Contábil Analítica

1. Selecionar **Ativo** ou **Inativo**:

   * Ativo → Elemento: `form[name="planejamento_analitico"] input[id="ativoS"]`
   * Inativo → Elemento: `form[name="planejamento_analitico"] input[id="ativoN"]`
2. Confirmar a alteração no formulário de edição.

---

## ✅ Resultado Esperado

A conta contábil analítica deve ser atualizada com o **status correto** de acordo com o que foi definido (Ativo ou Inativo).

---

## 📌 Observações

* Este fluxo utiliza **filtro por ID** para localizar a conta contábil analítica.
* A alteração do status é feita diretamente na tela de edição da conta.
* O login é feito uma única vez e mantido durante toda a execução do fluxo.

---

Se você quiser, já posso criar a **classe UseCase** para essa funcionalidade seguindo o padrão que usamos nas outras, usando o **BaseWebUseCase** e reaproveitando o fluxo de login e filtragem para não repetir código.

Quer que eu faça essa implementação agora?
