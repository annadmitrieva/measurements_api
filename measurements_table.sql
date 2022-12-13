--
-- PostgreSQL database dump
--

-- Dumped from database version 12.13 (Ubuntu 12.13-1.pgdg20.04+1)
-- Dumped by pg_dump version 12.13 (Ubuntu 12.13-1.pgdg20.04+1)

-- Started on 2022-12-13 13:11:49 EET

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 16388)
-- Name: measurements; Type: TABLE; Schema: public; Owner: api_user
--

CREATE TABLE public.measurements (
    id integer DEFAULT nextval('public.measurement_id'::regclass) NOT NULL,
    sensor_id integer,
    measurement_type character varying,
    "timestamp" timestamp with time zone,
    measurement_value double precision
);


ALTER TABLE public.measurements OWNER TO api_user;

--
-- TOC entry 2963 (class 0 OID 16388)
-- Dependencies: 203
-- Data for Name: measurements; Type: TABLE DATA; Schema: public; Owner: api_user
--

COPY public.measurements (id, sensor_id, measurement_type, "timestamp", measurement_value) FROM stdin;
7	12	temperature celsius	2022-12-12 14:48:11.966+02	44.333
10	13	temperature celsius	2022-12-11 14:49:11.966+02	42.2
11	13	temperature celsius	2022-12-11 14:50:11.966+02	41.1
4	12	relative humidity	2022-12-12 14:36:03.256+02	50.5
5	12	relative humidity	2022-12-12 14:40:44.256+02	55.4
6	12	relative humidity	2022-12-12 15:35:03.256+02	52.1
8	12	temperature celsius	2022-12-11 14:48:11.966+02	44.332
9	12	temperature celsius	2022-12-11 14:48:11.966+02	43.333
12	13	temperature celsius	2022-12-12 16:51:15.834+02	39.99
13	13	temperature celsius	2022-12-12 16:52:15.834+02	38.3
14	13	temperature celsius	2022-12-12 16:53:15.834+02	40.4
15	13	temperature celsius	2022-12-12 16:54:15.834+02	42.2
16	13	relative humidity	2022-12-12 15:36:00.256+02	53.2
\.


--
-- TOC entry 2836 (class 2606 OID 16396)
-- Name: measurements measurements_pkey; Type: CONSTRAINT; Schema: public; Owner: api_user
--

ALTER TABLE ONLY public.measurements
    ADD CONSTRAINT measurements_pkey PRIMARY KEY (id);


-- Completed on 2022-12-13 13:11:49 EET

--
-- PostgreSQL database dump complete
--

