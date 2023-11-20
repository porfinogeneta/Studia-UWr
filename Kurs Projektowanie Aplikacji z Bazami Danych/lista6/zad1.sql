DROP TABLE IF EXISTS Patients;
GO

CREATE TABLE Patients (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Patient VARCHAR(20),
    PatientAddress VARCHAR(30),
    Appointment_time_and_location VARCHAR(30),
    Price VARCHAR(10),
    Phisician VARCHAR(20),
    Appointment_cause VARCHAR(50)
)
GO

SET IDENTITY_INSERT Patients ON
INSERT INTO Patients (ID, Patient, PatientAddress, Appointment_time_and_location, Price, Phisician, Appointment_cause) VALUES
(1, 'Jan Kot', '6 Dolna Street, 44-444 Bór', '2029-02-01 12:30, room 12', '300 zł', 'Oleg Wyrwiząb', 'Dental: Denture fitting in (...)'),
(2, 'Maria Mysz', '9 Górna Street, 55-555 Las', '2030-01-04 11:45, room 7', '150 zł', 'Ewa Ciarka', 'Dermatology: Birthmark inspection (...)')
SET IDENTITY_INSERT Patients OFF

-- SELECT * FROM Patients

-- optymalizacja w wersji 1NF
/*
CECHY:
- wartości są atomowe, brak list, kolekcji, itp.
- brak powtarzających się nazw kolumn „Składnik1” „Składnik2”, „Składnik3”
*/

DROP TABLE IF EXISTS Patients1NF;
GO

CREATE TABLE Patients1NF (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Patient VARCHAR(20),
    Address VARCHAR(30),
    PostalCode VARCHAR(6),
    Town VARCHAR(20),
    Appointment_Date DATETIME,
    Room INT,
    PricePLN Decimal(10, 2),
    Phisician VARCHAR(20),
    Category VARCHAR(20),
    Description VARCHAR(50)
)
GO

SET IDENTITY_INSERT Patients1NF ON
INSERT INTO Patients1NF (ID, Patient, Address, PostalCode, Town, Appointment_Date, Room, PricePLN, Phisician, Category, Description) VALUES
(1, 'Jan Kot', '6 Dolna Street', '44-444', 'Bór', '2029-02-01 12:30', 12, 300, 'Oleg Wyrwiząb', 'Dental', 'Denture fitting in (...)'),
(2, 'Maria Mysz', '9 Górna Street', '55-555', 'Las', '2030-01-04 11:45', 7, 150, 'Ewa Ciarka', 'Dermatology', 'Birthmark inspection (...)')
SET IDENTITY_INSERT Patients1NF OFF

-- SELECT * FROM Patients1NF

-- 2NF
/*
CECHY:
- każda tabela ma przechowywać dane dotyczące tylko tej jednej klasy obiektów
- rozszerzamy strukturę o nowe tabelki i nowe kolumny
- zmiany wykonujemy na tabelce powstałej z 1NF

W naszym przypadku widać 3 tabelki:
- klient
- wizyta klienta
- rodzaj zabiegu
*/

DROP TABLE IF EXISTS Patients2NF;
GO

CREATE TABLE Patients2NF (
    IDPatient INT IDENTITY(1,1) PRIMARY KEY,
    Patient VARCHAR(20),
    Address VARCHAR(30),
    PostalCode VARCHAR(6),
    Town VARCHAR(20),
)
GO

SET IDENTITY_INSERT Patients2NF ON
INSERT INTO Patients2NF (IDPatient, Patient, Address, PostalCode, Town) VALUES
(1, 'Jan Kot', '6 Dolna Street', '44-444', 'Bór'),
(2, 'Maria Mysz', '9 Górna Street', '55-555', 'Las')
SET IDENTITY_INSERT Patients2NF OFF



DROP TABLE IF EXISTS Appointment2NF;
GO


CREATE TABLE Appointment2NF(
    IDAppointment INT IDENTITY(1,1) PRIMARY KEY,
    IDPatient INT,
    Appointment_Date DATETIME,
    Room INT,
    PricePLN Decimal(10, 2), -- cena ile kosztował ten konkretnie zabieg, mógł np wyjść drożej
    Phisician VARCHAR(20),
    -- aby dodawać kolejne zabiegi dodaje się po prostu nową wizytę
)
GO

SET IDENTITY_INSERT Appointment2NF ON
INSERT INTO Appointment2NF (IDAppointment, IDPatient, Appointment_Date, Room, PricePLN, Phisician) VALUES
(101, 1, '2029-02-01 12:30', 12, 300, 'Oleg Wyrwiząb'),
(102, 2, '2030-01-04 11:45', 7, 150, 'Ewa Ciarka')
SET IDENTITY_INSERT Appointment2NF OFF

DROP TABLE IF EXISTS Operation2NF;
GO

CREATE TABLE Operation2NF(
    IDAppointment INT, -- każda wizyta ma ma swoją kategorię, opis i normalną cenę
    Category VARCHAR(20),
    Description VARCHAR(50),
    NormalPricePLN Decimal(10, 2),
)


-- SET IDENTITY_INSERT Operation2NF ON
INSERT INTO Operation2NF (IDAppointment, Category, Description, NormalPricePLN) VALUES
(101, 'Dental', 'Denture fitting in (...)', 300),
(102, 'Dermatology', 'Birthmark inspection (...)', 150)
-- SET IDENTITY_INSERT Operation2NF OFF

-- SELECT * FROM Patients2NF
-- SELECT * FROM Appointment2NF
-- SELECT * FROM Operation2NF

-- 3NF
/*
CECHY:
- kolumna informacyjna nie należąca do klucza nie zależy też od innej kolumny informacyjnej, nie należącej do klucza,
    czyli w praktyce usuwamy duplikaty, które mogą istnieć tylko w jednej tabelce,
    Czyli każdy niekluczowy argument jest bezpośrednio zależny tylko od klucza głównego a nie od innej kolumny.
*/
-- u nas nie ma redundancji danych poza dodaną przeze mnie NormalPrice i Price, z nich możemy zrezygnować
DROP TABLE IF EXISTS Patients3NF;
GO

CREATE TABLE Patients3NF (
    IDPatient INT IDENTITY(1,1) PRIMARY KEY,
    Patient VARCHAR(20),
    Address VARCHAR(30),
    PostalCode VARCHAR(6),
    Town VARCHAR(20),
)
GO

SET IDENTITY_INSERT Patients3NF ON
INSERT INTO Patients3NF (IDPatient, Patient, Address, PostalCode, Town) VALUES
(1, 'Jan Kot', '6 Dolna Street', '44-444', 'Bór'),
(2, 'Maria Mysz', '9 Górna Street', '55-555', 'Las')
SET IDENTITY_INSERT Patients3NF OFF



DROP TABLE IF EXISTS Appointment3NF;
GO


CREATE TABLE Appointment3NF(
    IDAppointment INT IDENTITY(1,1) PRIMARY KEY,
    IDPatient INT,
    Appointment_Date DATETIME,
    Room INT,
    Phisician VARCHAR(20),
    -- aby dodawać kolejne zabiegi dodaje się po prostu nową wizytę
)
GO

-- od teraz cena jest przypisana do Operacji
SET IDENTITY_INSERT Appointment3NF ON
INSERT INTO Appointment3NF (IDAppointment, IDPatient, Appointment_Date, Room, Phisician) VALUES
(101, 1, '2029-02-01 12:30', 12, 'Oleg Wyrwiząb'),
(102, 2, '2030-01-04 11:45', 7, 'Ewa Ciarka')
SET IDENTITY_INSERT Appointment3NF OFF

DROP TABLE IF EXISTS Operation3NF;
GO

CREATE TABLE Operation3NF(
    IDAppointment INT, -- każda wizyta ma ma swoją kategorię, opis i normalną cenę
    Category VARCHAR(20),
    Description VARCHAR(50),
    PricePLN Decimal(10, 2),
)


INSERT INTO Operation3NF (IDAppointment, Category, Description, PricePLN) VALUES
(101, 'Dental', 'Denture fitting in (...)', 300),
(102, 'Dermatology', 'Birthmark inspection (...)', 150)

SELECT * FROM Patients3NF
SELECT * FROM Appointment3NF
SELECT * FROM Operation3NF