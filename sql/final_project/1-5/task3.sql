drop table if exists company;

create table company as (
	select row_number() over () as id, 
		cname, 
		a.countryregioncode as countrycode, 
		a.city 
	from address a
	inner join (
		select distinct c.companyname as cname,
			ca.addressid
		from customer c 
		inner join customeraddress ca 
		on c.customerid = ca.customerid 
		where ca.addresstype = 'Main Office'
	) as caa
	on a.addressid = caa.addressid
);