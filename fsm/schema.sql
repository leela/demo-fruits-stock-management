
create table fruits (
    id integer primary key,
    name text not null,
    price float not null,
    quantity float default 0,
    created timestamp default (current_timestamp)
);
