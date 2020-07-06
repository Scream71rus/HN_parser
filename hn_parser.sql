
create schema hn_parser;

create table hn_parser.hacker_news(
    id serial primary key,
    title text not null,
    link text unique not null,
    created timestamp not null default now()
);
