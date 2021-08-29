--commands for creating tables

CREATE TABLE RawCards(
    oracle_id UUID PRIMARY KEY,
    uri varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    type_line varchar(255) NOT NULL,
    cmc float NOT NULL,
    mana_cost varchar(50),
    oracle_text varchar(1000),
    power varchar(10),
    toughness varchar(10),
    loyalty varchar(10),
    colors varchar(15),
    color_identity varchar(15),
    produced_mana varchar(15),
    edhrec_rank integer,
    layout varchar(50) NOT NULL
);

CREATE TABLE Tokens(
    oracle_id UUID PRIMARY KEY,
    uri varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    type_line varchar(255) NOT NULL,
    oracle_text varchar(1000),
    power varchar(10),
    toughness varchar(10),
    colors varchar(15)
);

CREATE TABLE CardKeywords(
    oracle_id UUID PRIMARY KEY,
    keyword varchar(50)
);