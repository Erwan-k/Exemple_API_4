DROP TABLE IF EXISTS "Utilisateur";
CREATE TABLE "public"."Utilisateur" (
    "user" text NOT NULL,
    "mdp" text NOT NULL
) WITH (oids = false);

ALTER TABLE `Utilisateur`
  ADD PRIMARY KEY (`user`);

