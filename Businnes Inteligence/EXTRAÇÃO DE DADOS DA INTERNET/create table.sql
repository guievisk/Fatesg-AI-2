CREATE TABLE consulta_moedas (
    id SERIAL PRIMARY KEY,
    moeda VARCHAR(50),
    preco_usd NUMERIC(20, 2),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);