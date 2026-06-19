"""
=========================================================
SALES AI
=========================================================

Assistente Inteligente para Prospecção,
Relacionamento e Conversão de Clientes.

Projeto Educacional baseado em um Caso Real de Negócio
utilizado em aulas de Inteligência Artificial Aplicada
aos Negócios.

Autor:
Frederico Rodrigues de Oliveira

Objetivo:
Demonstrar como a Inteligência Artificial Generativa
pode apoiar vendedores e gestores comerciais na
análise de clientes e tomada de decisão.

Tecnologias:
- Python
- Inteligência Artificial Generativa
- LLMs (Large Language Models)
- Engenharia de Prompt
- CRM
- OpenAI / ChatGPT

=========================================================
"""

# =====================================================
# INSTALAÇÃO DA BIBLIOTECA
# =====================================================
#
# Se estiver utilizando o Google Colab,
# execute previamente em uma célula separada:
#
# !pip install -q openai
#
# =====================================================

from openai import OpenAI

# =====================================================
# CONFIGURAÇÃO DA API
# =====================================================
#
# IMPORTANTE:
#
# Substitua SUA_API_KEY pela sua chave.
#
# Exemplo:
#
# api_key="sk-proj-xxxxxxxxxxxxxxxxxxxxx"
#
# Nunca publique sua chave real no GitHub.
#
# =====================================================

client = OpenAI(
    api_key="SUA_API_KEY"
)

# =====================================================
# DADOS DO CLIENTE
# =====================================================
#
# Simulação de informações obtidas a partir
# de um sistema CRM.
#
# Durante as aulas os estudantes poderão
# alterar os dados e verificar como a IA
# responde a diferentes cenários.
#
# =====================================================

cliente = {
    "empresa": "Alpha Tecnologia",
    "segmento": "Software",
    "porte": "Médio",
    "dias_sem_contato": 120,
    "numero_reunioes": 3,
    "interesse": "Alto",
    "valor_potencial": "R$ 50.000"
}

# =====================================================
# PROMPT
# =====================================================
#
# O prompt define o comportamento da IA.
#
# Neste caso ela atuará como uma consultora
# especializada em CRM, estratégia comercial
# e conversão de oportunidades.
#
# =====================================================

prompt = f"""
Você é um consultor sênior de vendas
especializado em CRM, Inteligência Comercial
e Relacionamento com Clientes.

Analise as informações abaixo e gere:

1. Resumo Executivo;
2. Oportunidades Identificadas;
3. Possíveis Riscos;
4. Probabilidade de Conversão (%);
5. Estratégia de Abordagem;
6. Próxima Ação Recomendada;
7. E-mail Comercial Personalizado.

Dados do cliente:

Empresa: {cliente["empresa"]}
Segmento: {cliente["segmento"]}
Porte: {cliente["porte"]}
Dias sem contato: {cliente["dias_sem_contato"]}
Número de reuniões realizadas: {cliente["numero_reunioes"]}
Interesse declarado: {cliente["interesse"]}
Valor potencial da oportunidade: {cliente["valor_potencial"]}

Utilize linguagem profissional,
objetiva e voltada para gestores.
"""

# =====================================================
# CHAMADA DA IA GENERATIVA
# =====================================================
#
# O próximo bloco envia os dados para um
# Modelo de Linguagem de Grande Escala (LLM).
#
# Neste exemplo está sendo utilizado um
# modelo compatível com a plataforma OpenAI.
#
# =====================================================

resposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": """
            Você é especialista em:

            - CRM
            - Gestão Comercial
            - Inteligência de Mercado
            - Prospecção de Clientes
            - Vendas Consultivas
            - Relacionamento com Clientes
            - Estratégias de Conversão
            """
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7
)

# =====================================================
# RESULTADO
# =====================================================
#
# Exibe a análise gerada pela IA.
#
# =====================================================

print("\n")
print("=" * 80)
print("RELATÓRIO GERADO PELO SALESCOPILOT AI")
print("=" * 80)
print("\n")

print(resposta.choices[0].message.content)

print("\n")
print("=" * 80)
print("FIM DA ANÁLISE")
print("=" * 80)

# =====================================================
# APLICAÇÃO EDUCACIONAL
# =====================================================
#
# Este projeto foi desenvolvido para apoiar
# atividades práticas em disciplinas de
# Inteligência Artificial Aplicada aos Negócios.
#
# Competências trabalhadas:
#
# ✅ Inteligência Artificial Generativa
#
# ✅ Modelos de Linguagem de Grande Escala
#
# ✅ Engenharia de Prompt
#
# ✅ CRM
#
# ✅ Análise Comercial
#
# ✅ Tomada de Decisão
#
# ✅ Python aplicado à IA
#
# ✅ Resolução de Problemas Reais
#
# Possíveis atividades em sala:
#
# - Alterar perfil do cliente;
# - Comparar cenários comerciais;
# - Simular oportunidades;
# - Construir novos prompts;
# - Avaliar a qualidade das respostas da IA.
#
# =====================================================
