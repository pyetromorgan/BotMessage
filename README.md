# BOTMESSAGE

Um bot em Python que lê nomes e telefones de um banco de dados Supabase e envia mensagens automáticas personalizadas pelo WhatsApp usando a Z-API.

##  Como Usar

### 1. Instalar as dependências
Abra o terminal na pasta do projeto e instale as bibliotecas necessárias:
```bash
pip install requests python-dotenv
```

### 2. Atualize o .env
Depois mude .env_example para .env e coloque os dados corretamente em cada lugar

### 3. Estrutura da tabela no Supabase
create table contatos (
  id bigint generated always as identity primary key,
  nome text not null,
  telefone text not null
);

