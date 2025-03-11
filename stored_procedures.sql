-- Drop existing procedures if they exist to avoid duplicates
USE Tegridy;
DROP PROCEDURE IF EXISTS CreateUser;
DROP PROCEDURE IF EXISTS GetUsers;
DROP PROCEDURE IF EXISTS GetUserByID;
DROP PROCEDURE IF EXISTS UpdateUser;
DROP PROCEDURE IF EXISTS DeleteUser;
DROP PROCEDURE IF EXISTS CreateCase;
DROP PROCEDURE IF EXISTS GetCases;
DROP PROCEDURE IF EXISTS GetCaseByID;
DROP PROCEDURE IF EXISTS UpdateCase;
DROP PROCEDURE IF EXISTS DeleteCase;
DROP PROCEDURE IF EXISTS CreateEvidence;
DROP PROCEDURE IF EXISTS GetEvidence;
DROP PROCEDURE IF EXISTS GetEvidenceByID;
DROP PROCEDURE IF EXISTS UpdateEvidence;
DROP PROCEDURE IF EXISTS DeleteEvidence;

-- Create stored procedures for Users table
-- Create a User
DELIMITER //
CREATE PROCEDURE CreateUser(
    IN p_email VARCHAR(255),
    IN p_first VARCHAR(45),
    IN p_last VARCHAR(45),
    IN p_phone VARCHAR(20),
    IN p_title VARCHAR(45)
)
BEGIN
    INSERT INTO Users (Email, FirstName, LastName, Phone, Title) 
    VALUES (p_email, p_first, p_last, p_phone, p_title);
END //
DELIMITER ;

-- Get all Users
DELIMITER //
CREATE PROCEDURE GetUsers()
BEGIN
    SELECT * FROM Users;
END //
DELIMITER ;

-- Get User by UserID
DELIMITER //
CREATE PROCEDURE GetUserByID(IN p_userid INT)
BEGIN
    SELECT * FROM Users WHERE UserID = p_userid;
END //
DELIMITER ;

-- Update a User
DELIMITER //
CREATE PROCEDURE UpdateUser(
    IN p_userid INT,
    IN p_email VARCHAR(255),
    IN p_first VARCHAR(45),
    IN p_last VARCHAR(45),
    IN p_phone VARCHAR(20),
    IN p_title VARCHAR(45)
)
BEGIN
    UPDATE Users 
    SET Email = p_email, FirstName = p_first, LastName = p_last, Phone = p_phone, Title = p_title
    WHERE UserID = p_userid;
END //
DELIMITER ;

-- Delete a User
DELIMITER //
CREATE PROCEDURE DeleteUser(IN p_userid INT)
BEGIN
    DELETE FROM Users WHERE UserID = p_userid;
END //
DELIMITER ;

-- Create a Case
DELIMITER //
CREATE PROCEDURE CreateCase(
    IN p_casenumber VARCHAR(50),
    IN p_jurisdiction VARCHAR(100),
    IN p_dateopened DATE,
    IN p_dateclosed DATE,
    IN p_suspectfirst VARCHAR(45),
    IN p_suspectlast VARCHAR(45),
    IN p_path VARCHAR(255),
    IN p_userid INT
)
BEGIN
    INSERT INTO Cases (CaseNumber, Jurisdiction, DateOpened, DateClosed, SuspectFirst, SuspectLast, CasePath, UserID) 
    VALUES (p_casenumber, p_jurisdiction, p_dateopened, p_dateclosed, p_suspectfirst, p_suspectlast, p_path, p_userid);
END //
DELIMITER ;

-- Get all Cases
DELIMITER //
CREATE PROCEDURE GetCases()
BEGIN
    SELECT * FROM Cases;
END //
DELIMITER ;

-- Get a Case by ID
DELIMITER //
CREATE PROCEDURE GetCaseByID(IN p_caseid INT)
BEGIN
    SELECT * FROM Cases WHERE CaseID = p_caseid;
END //
DELIMITER ;

-- Update a Case
DELIMITER //
CREATE PROCEDURE UpdateCase(
    IN p_caseid INT,
    IN p_casenumber VARCHAR(50),
    IN p_jurisdiction VARCHAR(100),
    IN p_dateopened DATE,
    IN p_dateclosed DATE,
    IN p_suspectfirst VARCHAR(45),
    IN p_suspectlast VARCHAR(45),
    IN p_path VARCHAR(255),
    IN p_userid INT
)
BEGIN
    UPDATE Cases 
    SET CaseNumber = p_casenumber, Jurisdiction = p_jurisdiction, DateOpened = p_dateopened, 
        DateClosed = p_dateclosed, SuspectFirst = p_suspectfirst, SuspectLast = p_suspectlast, 
        CasePath = p_path, UserID = p_userid
    WHERE CaseID = p_caseid;
END //
DELIMITER ;

-- Delete a Case
DELIMITER //
CREATE PROCEDURE DeleteCase(IN p_caseid INT)
BEGIN
    DELETE FROM Cases WHERE CaseID = p_caseid;
END //
DELIMITER ;

-- Create an Evidence Item
DELIMITER //
CREATE PROCEDURE CreateEvidence(
    IN p_filetype VARCHAR(50),
    IN p_md5 VARCHAR(32),
    IN p_md5datetime DATETIME,
    IN p_sha1 VARCHAR(40),
    IN p_sha1datetime DATETIME,
    IN p_path VARCHAR(255),
    IN p_caseid INT
)
BEGIN
    INSERT INTO Evidence (FileType, MD5Value, MD5DateTime, SHA1Value, SHA1DateTime, ItemPath, CaseID) 
    VALUES (p_filetype, p_md5, p_md5datetime, p_sha1, p_sha1datetime, p_path, p_caseid);
END //
DELIMITER ;

-- Get all Evidence
DELIMITER //
CREATE PROCEDURE GetEvidence()
BEGIN
    SELECT * FROM Evidence;
END //
DELIMITER ;

-- Get Evidence by EvidenceID
DELIMITER //
CREATE PROCEDURE GetEvidenceByID(IN p_evidenceid INT)
BEGIN
    SELECT * FROM Evidence WHERE EvidenceID = p_evidenceid;
END //
DELIMITER ;

-- Update Evidence
DELIMITER //
CREATE PROCEDURE UpdateEvidence(
    IN p_evidenceid INT,
    IN p_filetype VARCHAR(50),
    IN p_md5 VARCHAR(32),
    IN p_md5datetime DATETIME,
    IN p_sha1 VARCHAR(40),
    IN p_sha1datetime DATETIME,
    IN p_path VARCHAR(255),
    IN p_caseid INT
)
BEGIN
    UPDATE Evidence 
    SET FileType = p_filetype, MD5Value = p_md5, MD5DateTime = p_md5datetime, 
        SHA1Value = p_sha1, SHA1DateTime = p_sha1datetime, ItemPath = p_path, CaseID = p_caseid
    WHERE EvidenceID = p_evidenceid;
END //
DELIMITER ;

-- Delete Evidence
DELIMITER //
CREATE PROCEDURE DeleteEvidence(IN p_evidenceid INT)
BEGIN
    DELETE FROM Evidence WHERE EvidenceID = p_evidenceid;
END //
DELIMITER ;
