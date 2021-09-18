drop materialized view IF exists product2;
drop materialized view IF exists country2;

create materialized view product2 as 
	select pcc.categoryid as pcid,
		p.productid,
		pcc.category as pcname,
		p.name as pname
	from product p 
	inner join (
		select psc.productsubcategoryid as subcategoryid, 
			psc.name as subcategory, 
			pc.productcategoryid as categoryid,
			pc.name as category 
		from productsubcategory psc
		inner join productcategory pc 
		on psc.productcategoryid = pc.productcategoryid	
	) as pcc
	on p.productsubcategoryid = pcc.subcategoryid;

create materialized view country2 as
	select DISTINCT a.countryregioncode as countrycode 
	from address a
	inner join (
		select ca.addresstype as addresstype,
			ca.addressid
		from customer c 
		inner join customeraddress ca 
		on c.customerid = ca.customerid 
		where ca.addresstype = 'Main Office'
	) as caa
	on a.addressid = caa.addressid;
	
grant select ON product2, country2 TO planmanager, planadmin;