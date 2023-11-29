CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL
);

CREATE TABLE scenarios(
	id integer NOT NULL UNIQUE PRIMARY KEY,
	property_valuation DECIMAL(16,2) NOT NULL,
	financing_rate DECIMAL(16,2) NOT NULL
);


INSERT INTO scenarios (id, property_valuation, financing_rate) VALUES (1, 8.50, 11);
INSERT INTO scenarios (id, property_valuation, financing_rate) VALUES (2, 15, 8);

CREATE TABLE historic (
  id SERIAL PRIMARY KEY,
  user_id integer NOT NULL,

  scenario_id integer NOT NULL,
   valor_aluguel_imovel DECIMAL(16,2) NOT NULL,
   valor_compra_imovel DECIMAL(16,2) NOT NULL,
   entrada_imovel DECIMAL(16,2) NOT NULL,
   tempo_imovel INTEGER NOT NULL,

  soma_aluguel DECIMAL(16,2) NOT NULL,
  total_pago_pela_compra DECIMAL(16,2) NOT NULL,
  compensar_aluguel integer NOT NULL,
  opcao VARCHAR(255) NOT NULL,
  somatorio_aluguel DECIMAL(16,2) NOT NULL,

  created_at TIMESTAMP NOT NULL DEFAULT NOW(),    
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (scenario_id) REFERENCES scenarios (id)
)