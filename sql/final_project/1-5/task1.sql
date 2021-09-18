revoke all ON all tables IN schema public FROM PUBLIC, planadmin, planmanager;
drop user if exists ivan, sophie, kirill;
truncate table country_managers;

grant select ON all tables IN schema public TO planadmin, planmanager;
grant select, insert, delete, update ON plan_data, plan_status, country_managers TO planadmin;

grant select, insert, delete, update ON plan_data TO planmanager;
grant select, update ON plan_status, v_plan_edit TO planmanager;
grant select ON v_plan TO planmanager;

create user ivan with role planadmin;
create user kirill with role planmanager;
create user sophie with role planmanager;

insert into 
    country_managers 
VALUES
    ('kirill','FR'),
    ('kirill','GB'),
    ('kirill','DE'),
    ('kirill','AU'),
    ('sophie', 'US'),
    ('sophie', 'CA');