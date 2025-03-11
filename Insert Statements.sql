USE Tegridy;
INSERT INTO Users (Email, FirstName, LastName, Phone, Title)
VALUES ('ts1103@jagmail.southalabama.edu', 'Todd', 'Stringfellow', '251-654-8956', 'Investigator'),
	   ('jh2354@jagmail.southalabama.edu', 'John', 'Hampton', '251-554-8975', 'Investigator');
       
SELECT * FROM Users;
SELECT * FROM Cases WHERE UserID=1;
 
INSERT INTO Cases (CaseNumber, Jurisdiction, DateOpened, SuspectFirst, SuspectLast, CasePath, UserID)
VALUES ("1001", "Mobile County Sheriff's Office", "2020-12-15", "Brad", "Thompson", "C:\Users\zlcox\OneDrive\Desktop\ITE 485", "1"),
	   ("1002", "Mobile County Sheriff's Office", "2020-12-25", "Rico", "Suave", "C:\Users\zlcox\OneDrive\Desktop\ITE 497_498", "1"),
	   ("1003", "Mobile County Sheriff's Office", "2020-12-31", "Marlo", "Thompson", "C:\Users\zlcox\OneDrive\Desktop\TegridyProject", "2");
