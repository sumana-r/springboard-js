CREATE DATABASE soccerleague;

\c soccerleague

CREATE TABLE teams (
    teamid SERIAL PRIMARY KEY   NOT NULL,
    team_name VARCHAR(30)   NOT NULL
);
INSERT INTO teams
  (teamid, team_name)
VALUES
  (1, 'liverpool'),
  (2, 'chelsea');

CREATE TABLE player (
    playerid SERIAL PRIMARY KEY NOT NULL,
    player_name VARCHAR(15)   NOT NULL,
    teamid INTEGER REFERENCES teams(teamid) NOT NULL
);

INSERT INTO player
  (playerid, player_name, teamid)
VALUES
  (1, 'Salah'),
  (2, 'Firmino');

CREATE TABLE referee (
    refereeid SERIAL PRIMARY KEY NOT NULL,
    referee_name VARCHAR(18)   NOT NULL
    
);
INSERT INTO referee
  (refereeid, referee_name)
VALUES
  (1, 'Martin Atkinson'),
  (2, 'Chris Kavanagh');


CREATE TABLE match (
    matchid SERIAL PRIMARY KEY NOT NULL,
    teamid_a INTEGER REFERENCES teams(teamid)   NOT NULL,
    teamid_b INTEGER REFERENCES teams(teamid) NOT NULL,
    date DATE   NOT NULL,
    refereeid INTEGER REFERENCES referee(refereeid)  NOT NULL,
    stadium TEXT   NOT NULL,
    location TEXT   NOT NULL
);

INSERT INTO match
  (matchid, teamid_a, teamid_b, date, refereeid, stadium, location)
VALUES
   (1, 1 , 2, '10-02-2021', 2 , 'Aston Villa', 'Trinity Road, Birmingham B6 6HE'),
   (2, 2 , 1, '10-02-2022', 1 , 'Brentford', 'Braemar Road TW8 0NT London');


CREATE TABLE goals (
    playerid INTEGER REFERENCES player(playerid) NOT NULL,
    matchid INTEGER REFERENCES match(matchid) NOT NULL,
    teamid INTEGER REFERENCES teams(teamid)  NOT NULL,
    score INTEGER   NOT NULL
);

INSERT INTO goals
  (playerid, matchid, teamid, score)
VALUES
   (1, 1 , 1, 2),
   (2, 2 , 1, 3);

