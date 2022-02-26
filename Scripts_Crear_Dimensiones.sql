--		LESLY PISCO 		--
--################################--
-- Creación de la dimension album --

CREATE TABLE dim_album (
AlbumId INTEGER   PRIMARY KEY 
    AUTOINCREMENT NOT NULL UNIQUE,
TitleAlbum NVARCHAR (160) NOT NULL);

--################################--
-- Creación de la dimension artist --

CREATE TABLE dim_artist (
ArtistId INTEGER PRIMARY KEY 
    AUTOINCREMENT NOT NULL UNIQUE,
NameArtist NVARCHAR (120));

--################################--
-- Creación de la dimension customer --

CREATE TABLE dim_customer (
CustomerId INTEGER PRIMARY KEY 
    AUTOINCREMENT NOT NULL UNIQUE,
FirstName  NVARCHAR (40) NOT NULL,
LastName   NVARCHAR (20) NOT NULL,
Phone      NVARCHAR (24),
Fax        NVARCHAR (24),
Email      NVARCHAR (60) NOT NULL);

--################################--
-- Creación de la dimension invoice_items --

CREATE TABLE dim_invoice_items (
InvoiceLineId INTEGER PRIMARY KEY 
AUTOINCREMENT NOT NULL UNIQUE,
UnitPrice     NUMERIC (10, 2) NOT NULL,
Quantity      INTEGER         NOT NULL);



--################################--
-- Creación de la dimension location--

CREATE TABLE dim_location (
LocationId INTEGER PRIMARY KEY 
AUTOINCREMENT NOT NULL UNIQUE,
Address    NVARCHAR (70),
City       NVARCHAR (40),
State      NVARCHAR (40),
Country    NVARCHAR (40),
PostalCode NVARCHAR (10));


--################################--
-- Creación de la dimension time--

CREATE TABLE dim_time (
Time_id  INTEGER PRIMARY KEY 
AUTOINCREMENT NOT NULL UNIQUE,
date     DATETIME,
Year     INTEGER,
Quarter  INTEGER,
Month    INTEGER,
Week     INTEGER,
Day      INTEGER,
Day_Week INTEGER,
Day_Name VARCHAR (12) );


--################################--
-- Creación de la dimension tracks--

CREATE TABLE dim_tracks (
TrackId INTEGER PRIMARY KEY 
AUTOINCREMENT NOT NULL UNIQUE,
NameTrack    NVARCHAR (200)  NOT NULL,
MediaType    NVARCHAR (120),
NameGenre    NVARCHAR (120),
Composer     NVARCHAR (220),
Milliseconds INTEGER         NOT NULL,
Bytes        INTEGER,
UnitPrice    NUMERIC (10, 2) NOT NULL);



--################################--
-- Creación de la dimension Fact_sales--

CREATE TABLE fact_sales (
FactSalesId INTEGER NOT NULL
PRIMARY KEY AUTOINCREMENT UNIQUE,
InvoiceId   INTEGER,
CustomerId  INTEGER,
TimeId      INTEGER,
LocationId  INTEGER,
TrackId     INTEGER,
ArtistId    INTEGER,
AlbumId     INTEGER,
Total       NUMERIC (10, 2) NOT NULL,
FOREIGN KEY (InvoiceId)
REFERENCES dim_invoice_items (InvoiceLineId),
FOREIGN KEY (CustomerId)
REFERENCES dim_customer (CustomerId),
FOREIGN KEY (LocationId)
REFERENCES dim_location (LocationId),
FOREIGN KEY (TrackId)
REFERENCES dim_tracks (TrackId),
FOREIGN KEY (ArtistId)
REFERENCES dim_artist (ArtistId),
FOREIGN KEY (AlbumId)
REFERENCES dim_album (AlbumId),
FOREIGN KEY (TimeId)
REFERENCES dim_time (Time_id));