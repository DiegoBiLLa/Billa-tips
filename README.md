# Billa Tips - Betting Simulator

Um simulador de apostas virtual desenvolvido em **Python** com **FastAPI** para fins educacionais e de diversão. Permite que usuários pratiquem estratégias de apostas sem riscos reais.

## 🎯 Funcionalidades Principais

### ✅ Autenticação de Usuários
- Registro com validação de email
- Login seguro com JWT
- Senha criptografada com bcrypt
- Perfil de usuário

### 💰 Carteira Virtual
- Saldo inicial de R$ 1.000,00
- Depósitos e saques
- Histórico de transações
- Estatísticas de ganhos/perdas

### 🎲 Histórico de Apostas
- Rastreamento completo de apostas
- Status da aposta (pendente, ganho, perdido)
- Lucro/prejuízo de cada aposta
- ROI e taxa de vitória

### 🎰 Simulador de Diferentes Tipos de Apostas
1. **Moneyline** - Aposta simples no vencedor
2. **Spread** - Aposta com margem de pontos
3. **Over/Under** - Aposta em total de pontos
4. **Parlay** - Aposta múltipla (maior risco, maior recompensa)
5. **Live** - Apostas em tempo real

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- pip

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/DiegoBiLLa/Billa-tips.git
cd Billa-tips
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```

5. Execute o servidor:
```bash
uvicorn main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

### Swagger UI
Acesse: `http://localhost:8000/docs`

### ReDoc
Acesse: `http://localhost:8000/redoc`

## 🔐 Endpoints Principais

### Autenticação

#### POST `/api/auth/register`
Registrar novo usuário
```json
{
  "username": "usuario",
  "email": "user@example.com",
  "password": "senha123",
  "confirm_password": "senha123"
}
```

#### POST `/api/auth/login`
Fazer login
```json
{
  "username": "usuario",
  "password": "senha123"
}
```

#### GET `/api/auth/me`
Obter dados do usuário autenticado

### Carteira

#### GET `/api/wallet/balance`
Obter saldo da carteira

#### POST `/api/wallet/deposit`
Realizar depósito
```json
{
  "amount": 100.00
}
```

#### POST `/api/wallet/withdraw`
Realizar saque
```json
{
  "amount": 50.00
}
```

#### GET `/api/wallet/stats`
Obter estatísticas da carteira

### Apostas

#### POST `/api/bets/place`
Colocar uma aposta
```json
{
  "bet_type": "moneyline",
  "sport": "futebol",
  "event": "Brasil vs Argentina",
  "amount": 100.00,
  "odds": 2.50
}
```

#### POST `/api/bets/simulate`
Simular uma aposta (não usa saldo real)
```json
{
  "bet_type": "parlay",
  "sport": "basquete",
  "event": "Lakers vs Celtics",
  "amount": 50.00,
  "odds": 3.00
}
```

#### GET `/api/bets/history`
Obter histórico de apostas

#### GET `/api/bets/active`
Obter apostas pendentes

#### POST `/api/bets/resolve/{bet_id}`
Resolver uma aposta (simular resultado)
```json
{
  "status": "won",
  "result_data": "Time venceu com 2-1"
}
```

## 📊 Estrutura do Banco de Dados

```
Users (id, username, email, hashed_password, created_at, is_active)
  ↓
Wallets (id, user_id, balance, total_bet, total_won, total_lost)

Bets (id, user_id, bet_type, sport, event, amount, odds, potential_win, status, resolved_at)
```

## 🎓 Tipos de Apostas Suportados

### Moneyline (52% de chance de vitória)
- Aposta direta no vencedor
- Odds variáveis
- Exemplo: Brasil vence Argentina

### Spread (50% de chance)
- Aposta com margem de pontos
- Time deve ganhar/perder por margem específica
- Exemplo: Lakers -5 pontos

### Over/Under (50% de chance)
- Aposta no total de pontos/gols
- Exemplo: Mais de 2.5 gols no jogo

### Parlay (30% de chance)
- Múltiplas apostas combinadas
- Maior risco, maior recompensa
- Todas devem ganhar para vencer

### Live (48% de chance)
- Apostas durante o evento
- Odds mudam em tempo real
- Maior emoção e dinamismo

## 🧪 Testes

Execute os testes:
```bash
pytest
```

## 📝 Variáveis de Ambiente

```
DATABASE_URL - URL de conexão do banco de dados
SECRET_KEY - Chave secreta para JWT (mude em produção!)
ALGORITHM - Algoritmo de criptografia (padrão: HS256)
ACCESS_TOKEN_EXPIRE_MINUTES - Tempo de expiração do token
```

## 🔒 Segurança

- ✅ Senhas hasheadas com bcrypt
- ✅ Autenticação com JWT
- ✅ Validação de email
- ✅ CORS configurado
- ✅ Rate limiting (recomendado adicionar)

## 🚀 Próximas Melhorias

- [ ] Integração com APIs de sports reais
- [ ] Notificações em tempo real
- [ ] Dashboard com gráficos
- [ ] Sistema de ranking/leaderboard
- [ ] Bônus e promoções
- [ ] Multi-idiomas
- [ ] Aplicativo mobile

## 👨‍💻 Autor

**DiegoBiLLa**

## 📄 Licença

Este projeto é fornecido como está para fins educacionais.

## ⚠️ Aviso Legal

Este é um **simulador** e não uma plataforma de apostas real. As apostas usam moeda virtual e não representam ganhos ou perdas reais. Para não confundir dados: saldo inicial é R$ 1.000,00 (virtual).