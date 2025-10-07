--
-- PostgreSQL database dump
--

\restrict JfPVuJVPQQFsHSg67dDtX59CmtpANQfA2FvgLQW3pgzBNAsgt4j4S92v2EoNPbP

-- Dumped from database version 16.10 (Ubuntu 16.10-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.10 (Ubuntu 16.10-0ubuntu0.24.04.1)

-- Started on 2025-10-06 21:24:13 -03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 223 (class 1255 OID 16436)
-- Name: calcular_bonus(numeric); Type: FUNCTION; Schema: public; Owner: rhuser
--

CREATE FUNCTION public.calcular_bonus(salario numeric) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
BEGIN
  RETURN salario * 0.10;
END;
$$;


ALTER FUNCTION public.calcular_bonus(salario numeric) OWNER TO rhuser;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 16398)
-- Name: cargos; Type: TABLE; Schema: public; Owner: rhuser
--

CREATE TABLE public.cargos (
    id_cargo character varying(20) NOT NULL,
    nome_cargo character varying(50) NOT NULL
);


ALTER TABLE public.cargos OWNER TO rhuser;

--
-- TOC entry 216 (class 1259 OID 16392)
-- Name: departamentos; Type: TABLE; Schema: public; Owner: rhuser
--

CREATE TABLE public.departamentos (
    id_departamento integer NOT NULL,
    nome_departamento character varying(50) NOT NULL
);


ALTER TABLE public.departamentos OWNER TO rhuser;

--
-- TOC entry 215 (class 1259 OID 16391)
-- Name: departamentos_id_departamento_seq; Type: SEQUENCE; Schema: public; Owner: rhuser
--

CREATE SEQUENCE public.departamentos_id_departamento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.departamentos_id_departamento_seq OWNER TO rhuser;

--
-- TOC entry 3441 (class 0 OID 0)
-- Dependencies: 215
-- Name: departamentos_id_departamento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rhuser
--

ALTER SEQUENCE public.departamentos_id_departamento_seq OWNED BY public.departamentos.id_departamento;


--
-- TOC entry 219 (class 1259 OID 16404)
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: rhuser
--

CREATE TABLE public.funcionarios (
    id_funcionario integer NOT NULL,
    nome character varying(50) NOT NULL,
    sobrenome character varying(50) NOT NULL,
    data_nascimento date,
    id_cargo character varying(20),
    id_departamento integer,
    salario numeric(10,2)
);


ALTER TABLE public.funcionarios OWNER TO rhuser;

--
-- TOC entry 218 (class 1259 OID 16403)
-- Name: funcionarios_id_funcionario_seq; Type: SEQUENCE; Schema: public; Owner: rhuser
--

CREATE SEQUENCE public.funcionarios_id_funcionario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.funcionarios_id_funcionario_seq OWNER TO rhuser;

--
-- TOC entry 3442 (class 0 OID 0)
-- Dependencies: 218
-- Name: funcionarios_id_funcionario_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rhuser
--

ALTER SEQUENCE public.funcionarios_id_funcionario_seq OWNED BY public.funcionarios.id_funcionario;


--
-- TOC entry 221 (class 1259 OID 16411)
-- Name: treinamentos; Type: TABLE; Schema: public; Owner: rhuser
--

CREATE TABLE public.treinamentos (
    id_treinamento integer NOT NULL,
    nome_treinamento character varying(100) NOT NULL,
    data_inicio date,
    data_fim date,
    carga_horaria integer,
    trei_local character varying(100),
    ministrante character varying(100),
    id_funcionario integer
);


ALTER TABLE public.treinamentos OWNER TO rhuser;

--
-- TOC entry 220 (class 1259 OID 16410)
-- Name: treinamentos_id_treinamento_seq; Type: SEQUENCE; Schema: public; Owner: rhuser
--

CREATE SEQUENCE public.treinamentos_id_treinamento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.treinamentos_id_treinamento_seq OWNER TO rhuser;

--
-- TOC entry 3443 (class 0 OID 0)
-- Dependencies: 220
-- Name: treinamentos_id_treinamento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rhuser
--

ALTER SEQUENCE public.treinamentos_id_treinamento_seq OWNED BY public.treinamentos.id_treinamento;


--
-- TOC entry 222 (class 1259 OID 16432)
-- Name: vw_funcionarios_info; Type: VIEW; Schema: public; Owner: rhuser
--

CREATE VIEW public.vw_funcionarios_info AS
 SELECT f.nome,
    f.sobrenome,
    c.nome_cargo,
    d.nome_departamento,
    f.salario
   FROM ((public.funcionarios f
     JOIN public.cargos c ON (((f.id_cargo)::text = (c.id_cargo)::text)))
     JOIN public.departamentos d ON ((f.id_departamento = d.id_departamento)));


ALTER VIEW public.vw_funcionarios_info OWNER TO rhuser;

--
-- TOC entry 3270 (class 2604 OID 16395)
-- Name: departamentos id_departamento; Type: DEFAULT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.departamentos ALTER COLUMN id_departamento SET DEFAULT nextval('public.departamentos_id_departamento_seq'::regclass);


--
-- TOC entry 3271 (class 2604 OID 16407)
-- Name: funcionarios id_funcionario; Type: DEFAULT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.funcionarios ALTER COLUMN id_funcionario SET DEFAULT nextval('public.funcionarios_id_funcionario_seq'::regclass);


--
-- TOC entry 3272 (class 2604 OID 16414)
-- Name: treinamentos id_treinamento; Type: DEFAULT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.treinamentos ALTER COLUMN id_treinamento SET DEFAULT nextval('public.treinamentos_id_treinamento_seq'::regclass);


--
-- TOC entry 3430 (class 0 OID 16398)
-- Dependencies: 217
-- Data for Name: cargos; Type: TABLE DATA; Schema: public; Owner: rhuser
--

COPY public.cargos (id_cargo, nome_cargo) FROM stdin;
ANALISTA	Analista de Sistemas
GERENTE	Gerente de Projetos
ESTAGIARIO	Estagiário
ASSISTENTE	Assistente Administrativo
DIRETOR	Diretor
\.


--
-- TOC entry 3429 (class 0 OID 16392)
-- Dependencies: 216
-- Data for Name: departamentos; Type: TABLE DATA; Schema: public; Owner: rhuser
--

COPY public.departamentos (id_departamento, nome_departamento) FROM stdin;
1	Tecnologia da Informação
2	Desenvolvimento
3	Administração
4	Marketing
5	Financeiro
\.


--
-- TOC entry 3432 (class 0 OID 16404)
-- Dependencies: 219
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: rhuser
--

COPY public.funcionarios (id_funcionario, nome, sobrenome, data_nascimento, id_cargo, id_departamento, salario) FROM stdin;
1	João	Silva	1980-01-01	ANALISTA	1	5000.00
2	Maria	Santos	1985-05-15	GERENTE	2	8000.00
3	Pedro	Almeida	1990-12-25	ESTAGIARIO	1	1500.00
4	Ana	Oliveira	1995-08-10	ASSISTENTE	3	2500.00
5	Carlos	Souza	1978-03-20	DIRETOR	3	12000.00
11	Ana	Silva	1995-03-20	GERENTE	2	5200.00
\.


--
-- TOC entry 3434 (class 0 OID 16411)
-- Dependencies: 221
-- Data for Name: treinamentos; Type: TABLE DATA; Schema: public; Owner: rhuser
--

COPY public.treinamentos (id_treinamento, nome_treinamento, data_inicio, data_fim, carga_horaria, trei_local, ministrante, id_funcionario) FROM stdin;
1	Introdução ao SQL	2025-07-01	2025-07-05	20	Sala de treinamento	João Silva	1
2	Gestão de Projetos	2025-08-15	2025-08-20	30	Auditório	Maria Santos	2
3	Desenvolvimento Web	2025-09-10	2025-09-25	40	Laboratório	Pedro Almeida	3
4	Curso Avançado de SQL	2025-12-01	2025-12-05	25	Sala 1	Professor X	1
5	Gestão Ágil de Projetos	2025-11-15	2025-11-20	20	Sala 2	Professor Y	2
\.


--
-- TOC entry 3444 (class 0 OID 0)
-- Dependencies: 215
-- Name: departamentos_id_departamento_seq; Type: SEQUENCE SET; Schema: public; Owner: rhuser
--

SELECT pg_catalog.setval('public.departamentos_id_departamento_seq', 1, false);


--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 218
-- Name: funcionarios_id_funcionario_seq; Type: SEQUENCE SET; Schema: public; Owner: rhuser
--

SELECT pg_catalog.setval('public.funcionarios_id_funcionario_seq', 11, true);


--
-- TOC entry 3446 (class 0 OID 0)
-- Dependencies: 220
-- Name: treinamentos_id_treinamento_seq; Type: SEQUENCE SET; Schema: public; Owner: rhuser
--

SELECT pg_catalog.setval('public.treinamentos_id_treinamento_seq', 5, true);


--
-- TOC entry 3276 (class 2606 OID 16402)
-- Name: cargos cargos_pkey; Type: CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.cargos
    ADD CONSTRAINT cargos_pkey PRIMARY KEY (id_cargo);


--
-- TOC entry 3274 (class 2606 OID 16397)
-- Name: departamentos departamentos_pkey; Type: CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.departamentos
    ADD CONSTRAINT departamentos_pkey PRIMARY KEY (id_departamento);


--
-- TOC entry 3278 (class 2606 OID 16409)
-- Name: funcionarios funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (id_funcionario);


--
-- TOC entry 3280 (class 2606 OID 16416)
-- Name: treinamentos treinamentos_pkey; Type: CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.treinamentos
    ADD CONSTRAINT treinamentos_pkey PRIMARY KEY (id_treinamento);


--
-- TOC entry 3281 (class 2606 OID 16417)
-- Name: funcionarios fk_funcionarios_cargos; Type: FK CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT fk_funcionarios_cargos FOREIGN KEY (id_cargo) REFERENCES public.cargos(id_cargo) ON DELETE RESTRICT;


--
-- TOC entry 3282 (class 2606 OID 16422)
-- Name: funcionarios fk_funcionarios_departamentos; Type: FK CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT fk_funcionarios_departamentos FOREIGN KEY (id_departamento) REFERENCES public.departamentos(id_departamento) ON DELETE RESTRICT;


--
-- TOC entry 3283 (class 2606 OID 16427)
-- Name: treinamentos fk_treinamentos_funcionarios; Type: FK CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.treinamentos
    ADD CONSTRAINT fk_treinamentos_funcionarios FOREIGN KEY (id_funcionario) REFERENCES public.funcionarios(id_funcionario) ON DELETE RESTRICT;


--
-- TOC entry 3440 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT ALL ON SCHEMA public TO rhuser;


-- Completed on 2025-10-06 21:24:13 -03

--
-- PostgreSQL database dump complete
--

\unrestrict JfPVuJVPQQFsHSg67dDtX59CmtpANQfA2FvgLQW3pgzBNAsgt4j4S92v2EoNPbP

