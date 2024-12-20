DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE "BoardGames" (
    "bg_id" SERIAL PRIMARY KEY,
    "name" VARCHAR,
    "number_of_players" INTEGER,
    "price" INTEGER
);

CREATE TABLE "place" (
    "pl_id" SERIAL PRIMARY KEY,
    "address" VARCHAR NOT NULL
);

CREATE TABLE "warehouse" (
    "wh_id" SERIAL PRIMARY KEY,
    "bg_id" INTEGER NOT NULL,
    "quantity" INTEGER NOT NULL DEFAULT 0,
    "pl_id" INTEGER NOT NULL,
    FOREIGN KEY ("pl_id") REFERENCES "place"("pl_id")
);

CREATE TABLE "shop" (
    "sh_id" SERIAL PRIMARY KEY,
    "pl_id" INTEGER NOT NULL,
    FOREIGN KEY ("pl_id") REFERENCES "place"("pl_id")
);

CREATE TABLE "shopbg" (
    "id" SERIAL PRIMARY KEY,
    "sh_id" INTEGER NOT NULL,
    "bg_id" INTEGER NOT NULL,
    "quantity" INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY ("sh_id") REFERENCES "shop"("sh_id"),
    FOREIGN KEY ("bg_id") REFERENCES "BoardGames"("bg_id")
);

CREATE TABLE "worker" (
    "w_id" SERIAL PRIMARY KEY,
    "full_name" VARCHAR NOT NULL,
    "sh_id" INTEGER,
    FOREIGN KEY ("sh_id") REFERENCES "shop"("sh_id")
);

CREATE TABLE "user" (
    "us_id" SERIAL PRIMARY KEY,
    "full_name" VARCHAR NOT NULL
);

CREATE TABLE "check" (
    "ch_id" SERIAL PRIMARY KEY,
    "us_id" INTEGER NOT NULL,
    "w_id" INTEGER DEFAULT NULL,
    FOREIGN KEY ("us_id") REFERENCES "user"("us_id"),
    FOREIGN KEY ("w_id") REFERENCES "worker"("w_id")
);

CREATE TABLE "bg_check" (
    "id" SERIAL PRIMARY KEY,
    "ch_id" INTEGER NOT NULL,
    "bg_id" INTEGER,
    FOREIGN KEY ("ch_id") REFERENCES "check"("ch_id"),
    FOREIGN KEY ("bg_id") REFERENCES "BoardGames"("bg_id")
);

ALTER TABLE "warehouse" ADD CONSTRAINT "bg_1" FOREIGN KEY ("bg_id") REFERENCES "BoardGames"("bg_id")
