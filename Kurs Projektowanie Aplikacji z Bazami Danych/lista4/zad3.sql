

-- INSTEAD OF umożliwia ominięcie wykonania INSERT, DELETE, albo UPDATE i wykonanie innych poleceń
-- zdefiniowanych w trigger, ominięcie poleceń DML i wykonanie innych poleceń

-- w przykładzie dodajemy nowe 'brands' do tabelki 'brands'
-- nowe 'brand' będą przechowywane w brand_approvals, zanim zostaną dodane do 'brands'
-- w momencie dodanie do widoku vw_brands uruchomi się trigger, który doda nam 'approved' brand do 'brands'
-- robimy to żeby przejść przez zatwierdzenie, a nie od razu wrzucać do brands, musi to przejść proces approve,
-- łatwo możemy osiągnąć 'access control'

DROP TABLE IF EXISTS brand_approvals
GO

DROP TABLE IF EXISTS brands
GO

DROP VIEW IF EXISTS vw_brands
GO

CREATE TABLE brands (
    brand_id INT IDENTITY PRIMARY KEY,
    brand_name VARCHAR(255)
);

SET IDENTITY_INSERT brands ON
INSERT INTO brands (brand_id, brand_name)
VALUES
    (1, 'Izera'),
    (2, 'Tesla'),
    (3, 'Toyota'),
    (4, 'Volvo');
SET IDENTITY_INSERT Products OFF

CREATE TABLE brand_approvals(
    brand_id INT IDENTITY PRIMARY KEY,
    brand_name VARCHAR(255) NOT NULL
);
GO

CREATE VIEW vw_brands 
AS
-- approved są tylko z brands
SELECT
    brand_name,
    'Approved' approval_status
FROM
    brands
UNION
-- pending są tylko z brand_approvals
SELECT
    brand_name,
    'Pending Approval' approval_status
FROM
    brand_approvals;
GO

DROP TRIGGER IF EXISTS trg_vw_brands 
GO
-- za każdym razem, gdy coś będzie dodane do 'vw_brands' przenosimy to do brand_approvals za pomocą triggera INSTEAD OF
CREATE TRIGGER trg_vw_brands 
ON vw_brands
INSTEAD OF INSERT
AS
BEGIN
    SET NOCOUNT ON; -- wyłączamy wiadomość 'row affected'
    INSERT INTO brand_approvals ( 
        brand_name
    )
    SELECT
        i.brand_name -- ze zmienionych pobieramy nazwę
    FROM
        inserted i
    WHERE
        -- bierzemy nazwę do approval, tylko jeżeli nie była wcześniej dodana do 'brands'
        i.brand_name NOT IN (
            SELECT 
                brand_name
            FROM
                brands
        );
END
GO

-- dodajemy nowy 'brand'
INSERT INTO vw_brands(brand_name)
    VALUES('Eddy Merckx');

SELECT
	brand_name,
	approval_status
FROM
	vw_brands;

SELECT 
	*
FROM 
	brand_approvals;

-- używając INSTEAD OF dodajemy dane do tabelki, będącej 'pod spodem' w stosunku do 'view'
-- dodajemy kolejny 'layer of defense'