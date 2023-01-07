create table players(
    Player_ID varchar(10),
    First_Name varchar(20),
    Last_Name varchar(20),
    Age integer default 18,
    Team_ID varchar(10),
    primary key(Player_ID)
);

create table team(
    Team_ID varchar(10),
    Team_Name varchar(20),
    Owner_ID varchar(10),
    primary key(Team_ID)
);

create table matches(
    Match_ID varchar(10),
    MDate DATE,
    Winning_Team varchar(20),
    POTM varchar(20),
    Stadium varchar(20),
    primary key(Match_ID));

create table coach(
    Coach_ID varchar(10),
    Coach_Name varchar(20),
    CType varchar(10),
    Team_ID varchar(10),
    primary key(Coach_ID)
);

create table owner(
    Owner_ID varchar(10),
    First_Name varchar(20),
    Last_Name varchar(20),
    primary key(Owner_ID)
);

create table umpire(
    Umpire_ID varchar(10),
    Umpire_Name varchar(20),
    Experience integer,
    primary key(Umpire_ID)
);

create table stat(
    Player_ID varchar(10),
    Match_ID varchar(10),
    Runs integer,
    Wickets integer,
    primary key(Player_ID,Match_ID)
);

create table plays(
    Team_ID varchar(10),
    Match_ID varchar(10),
    primary key(Team_ID,Match_ID)
);

create table referee(
    Match_ID varchar(10),
    Umpire_ID varchar(10)  
);

alter table players add constraint players_team foreign key(Team_ID) references team(Team_ID) on delete cascade;


alter table team add constraint team_owner foreign key(owner_ID) references owner(owner_ID) on delete cascade;


alter table coach add constraint coach_team foreign key(Team_ID) references team(Team_ID) on delete cascade;


alter table stat add constraint stat_players foreign key(Player_ID) references players(Player_ID) on delete cascade;

alter table stat add constraint stat_matches foreign key(Match_ID) references matches(Match_ID) on delete cascade;


alter table plays add constraint plays_team foreign key(Team_ID) references team(Team_ID) on delete cascade;

alter table plays add constraint plays_matches foreign key(Match_ID) references matches(Match_ID) on delete cascade;


alter table referee add constraint referee_matches foreign key(Match_ID) references matches(Match_ID) on delete cascade;

alter table referee add constraint referee_umpire foreign key(Umpire_ID) references umpire(Umpire_ID) on delete cascade;

