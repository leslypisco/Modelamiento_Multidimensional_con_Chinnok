--		Lesly Pisco

--Consulta paea la dimensión albums de la base de datos chinook.
SELECT Title AS TitleAlbum 
FROM albums;

--Consulta para la dimensión artists de la base de datos chinook.
SELECT Name AS NameArtist 
FROM artists;

--Consulta consulta para la dimensión customers de la base de datos chinook.
SELECT  FirstName,
	LastName,
	Phone,
	Fax,
	Email 
FROM customers;

--Consulta para la dimensión invoice_itemms de la base de datos chinook.
SELECT  UnitPrice,
	Quantity 
FROM invoice_items;

--Consulta para la dimensión location de la base de datos chinook.
SELECT BillingAddress AS Address,
       BillingCity AS City,
       BillingState AS State,
       BillingCountry AS Country,
       BillingPostalCode AS PostalCode
FROM invoices;


--Consulta para la dimensión tracks de la base de datos chinook.
SELECT tracks.Name AS NameTrack, 
       media_types.Name AS MediaType,
       genres.Name AS NameGenre,
       tracks.Composer,
       tracks.Milliseconds,
       tracks.Bytes,
       tracks.UnitPrice
FROM tracks INNER JOIN media_types
ON tracks.MediaTypeId = media_types.MediaTypeId
INNER JOIN genres
ON tracks.GenreId = genres.GenreId;

--Consulta para la tabla de hechos de la base de datos chinook.
SELECT   invoices.InvoiceId as InvoiceId,
         customers.CustomerId,
         dim_time.Time_id as TimeId,
         invoices.InvoiceId AS LocationId,
         tracks.TrackId,
         artists.ArtistId,
         albums.AlbumId,
         invoices.Total
FROM invoices INNER JOIN customers
ON invoices.CustomerId= customers.CustomerId
INNER JOIN invoice_items
ON invoice_items.InvoiceId= invoices.InvoiceId
INNER JOIN tracks
ON tracks.TrackId=  invoice_items.TrackId
INNER JOIN albums
ON tracks.AlbumId= albums.AlbumId
INNER JOIN artists 
ON albums.ArtistId= artists.ArtistId 
INNER JOIN dim_time
ON invoices.InvoiceDate= substr(dim_time.date,0,20);








