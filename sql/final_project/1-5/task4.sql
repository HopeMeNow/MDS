truncate table company_abc ;

insert into company_abc
select cid,
	salestotal,	
	case
        when sum(salestotal) over (partition by "year" order by salestotal DESC) <= 0.8 * sum(salestotal) over (partition by  "year")
            then 'A'
        when sum(salestotal) over (partition by  "year" order by salestotal DESC) <= 0.95 * sum(salestotal) over (partition by  "year")
            then 'B'
        else 'C'
    end as cls,
    year
from (
	select c.id as cid,
		spcy.companyname,
		spcy.salestotal,
		spcy."year"
	from company c 
	inner join (
		select sum(s.subtotal) as salestotal,
			date_part('year', s.orderdate) as "year",
			c.companyname
		from salesorderheader s 
		inner join customer c 
		on s.customerid = c.customerid 
		where c.companyname notnull -- ignore not company
		group by c.companyname, "year"
		order by salestotal DESC
	) as spcy
	on c.cname = spcy.companyname
) as s
where "year" = 2012 or "year" = 2013; -- we should do this classification only for 2012 and 2013, right?
