DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario (
    usu_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    email TEXT NOT NULL,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL
);

DROP TABLE IF EXISTS eventos;
CREATE TABLE eventos (
    eve_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    eve_nome TEXT NOT NULL,
    eve_desc TEXT NOT NULL

);

DROP TABLE IF EXISTS parteve;
CREATE TABLE parteve (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    par_eve_id INTEGER NOT NULL,
    par_usu_id INTEGER NOT NULL,
    FOREIGN KEY (par_eve_id) REFERENCES eventos (eve_id),
    FOREIGN KEY (par_usu_id) REFERENCES usuario (usu_id)
);