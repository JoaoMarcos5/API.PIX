# API.PIXColetor de Dados Pix – Banco Central do Brasil

Este projeto coleta dados públicos do Pix diretamente da API de Dados Abertos do Banco Central (BCB) e organiza em arquivos CSV separados por categoria:

Chaves Pix

Estatísticas de Transações

Transações por Município

Os dados são consolidados em apenas um arquivo CSV por categoria, contendo todos os anos configurados no script.

⚙️ Tecnologias utilizadas

Python 3.9+

Pandas

Requests

📂 Estrutura dos Arquivos Gerados

Após a execução, serão criados 3 arquivos CSV:

chavespix_todos.csv → Contém todas as informações de chaves Pix.

estatisticas_todos.csv → Contém estatísticas gerais de transações Pix.

transacoes_municipio_todos.csv → Contém transações Pix detalhadas por município.

🚀 Como executar
1. Clonar ou baixar o repositório
git clone https://github.com/seu-usuario/projeto-pix-api.git
cd projeto-pix-api

2. Criar ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Instalar dependências
pip install -r requirements.txt


📌 Se não existir o requirements.txt, basta rodar:

pip install pandas requests

4. Executar o script
python coletar_pix.py

📊 Exemplos de saída (CSV)

Trecho do arquivo estatisticas_todos.csv:

DataReferencia	QuantidadeTransacoes	ValorTotal	...
2023-01-01	1000000	200000000	...
2024-01-01	1200000	250000000	...
2025-01-01	1350000	30000000
