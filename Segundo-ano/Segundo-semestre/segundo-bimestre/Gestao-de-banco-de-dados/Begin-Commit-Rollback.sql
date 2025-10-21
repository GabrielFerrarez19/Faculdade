-- Criar tabela mesas
CREATE TABLE IF NOT EXISTS mesas (
    id SERIAL PRIMARY KEY,
    mesa_codigo VARCHAR(10) NOT NULL,
    mesa_situacao CHAR(1) NOT NULL
);

-- Inserir dados na tabela mesas
INSERT INTO mesas(mesa_codigo, mesa_situacao) VALUES ('00003', 'A');

-- Consultar mesas
SELECT * FROM mesas;

-- Criar tabela contas
CREATE TABLE IF NOT EXISTS contas (
    id SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL,
    saldo DECIMAL(10,2) NOT NULL,
    CONSTRAINT ck_saldo_positivo CHECK (saldo >= 0)
);

-- Inserir dados
INSERT INTO contas(nome_cliente, saldo)
VALUES
    ('Ana', 1000.00),
    ('Bruno', 500.00),
    ('Maria', 0.00),
    ('Joao', 10.00);

-- Consultar contas
SELECT * FROM contas;

-- Transferência de 200 entre contas (transação segura)
BEGIN;
UPDATE contas SET saldo = saldo - 200 WHERE id = 1;
UPDATE contas SET saldo = saldo + 200 WHERE id = 2;
COMMIT;

SELECT * FROM contas;

-- Transferência de 1000 entre contas (vai falhar se saldo insuficiente)
BEGIN;
UPDATE contas SET saldo = saldo - 1000 WHERE id = 1;  -- pode gerar erro se saldo < 1000
UPDATE contas SET saldo = saldo + 1000 WHERE id = 2;
COMMIT;

SELECT * FROM contas;

-- Limpa qualquer transação abortada
ROLLBACK;

-- Inicia transação
BEGIN;

-- Atualização de Ana
UPDATE contas
SET saldo = saldo - 50
WHERE nome_cliente = 'Ana' AND saldo >= 50;

-- Atualização de Bruno (id=2)
UPDATE contas
SET saldo = saldo - 50
WHERE id = 2 AND saldo >= 50;

-- Confirma transação
COMMIT;

-- Verificar resultados
SELECT * FROM contas;

begin;
update contas set saldo = saldo -50 where id=1;
update contas set saldo = saldo +50 where id=3;
update contas set saldo = saldo -50 where id=2;
update contas set saldo = saldo +50 where id=4;
commit;

SELECT * FROM contas
ORDER BY id ASC;


