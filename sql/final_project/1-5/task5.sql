drop table if exists temp_4;
drop table if exists temp_3;
drop table if exists temp_2;
drop table if exists temp_1;

select customerid,
	sod.linetotal, 
	sod.productid,
	date_part('year', soh.orderdate) as "year",
	date_part('quarter', soh.orderdate) as quarter_yr,
	date_part('year', soh.orderdate) || '.' || date_part('quarter', soh.orderdate) as qr 
into temp_1	
from salesorderdetail sod
inner join salesorderheader soh
on sod.salesorderid = soh.salesorderid;

select * from temp_1 where "year" = 2012 or "year" = 2013;

select t1.*, cc.cid
into temp_2
from temp_1 t1
inner join (
	select c2.id as cid,
		c.customerid 
	from customer c 
	inner join company c2
	on c.companyname = c2.cname 
) as cc
on t1.customerid = cc.customerid;

select * from temp_2 where "year" = 2012 or "year" = 2013;


select t2.*,
	p2.pcid 
into temp_3	
from temp_2 t2
inner join product2 p2 
on t2.productid = p2.productid;

select * from temp_3 where "year" = 2012 or "year" = 2013;

select t3.*,
	ccls.cls
into temp_4
from temp_3 t3
inner join company_abc ccls
on t3."year" = ccls."year" and t3.cid = ccls.cid ;

select * from temp_4; -- no need to specify year, coz we assigned categories only for 2012 and 2013

select cid,
	sum(linetotal) as salesamt,
	"year",
	quarter_yr,
	qr,
	pcid as categoryid,
	cls
from temp_4
group by qr, cid, pcid, "year", quarter_yr, cls

--drop table if exists temp_3;
--drop table if exists temp_2;
--drop table if exists temp_1;