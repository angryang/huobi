create table btc_market(
	last varchar(20), --last BTC price
	high varchar(20), -- last 24 hours price high
	low varchar(20), -- last 24 hours price low
	vwap varchar(40), -- last 24 hours volume weighted average price
	vol varchar(40), -- last 24 hours volume
	buy varchar(20), -- highest buy order
	sell varchar(20) -- lowest sell order
);