/*To recreate the database please follow the steps provided*/

/*Step1: Create a database name P_Element */
create database P_Element;

/*Step2: Create a table name element inside the P_Element Database*/
create table elements(
Esymbol varchar(20) not null,
Ename varchar(20) not null,
atomicNums int primary key auto_increment,
atomicMass varchar(20) not null,
Egroup varchar(20) not null
);

/*Step 3: Insert the indormation needed for the Periodic table*/
insert into elements(
Esymbol,
Ename,
atomicMass,
Egroup
) values("H","Hydrogen","1.0078 u","Reactive nonmetals"),
("He","Helium","4.0026 u","Noble Gases"),
("Li","Lithium","6.9410 u","Alkali metals"),
("Be","Beryllium","9.0122 u","Alkaline Earth metal"),
("B","Boron","10.811 u","Metalloids"),
("C","Carbon","12.011 u","Reactive Nonmetals"),
("N","Nitrogen","14.007 u","Reactive Nonmetals"),
("C","Carbon","12.011 u","Reactive Nonmetals"),
("N","Nitrogen","14.007 u","Reactive Nonmetals"),
("0","Oxygen","15.999 u","Reactive Nonmetals"),
("F","Fluorine","18.998403 u","Reactive Nonmetals"),
("Ne","Neon","20.179 u","Noble Gases"),
("Na","Sodium","22.98977 u","Alkali Metals"),
("Mg","Magnesium","24.305 u","Alkaline Earth metal"),
("Al","Aluminum","26.98154 u","PostTransition metal"),
("Si","Silicon","28.0855 u","Metalloids"),
("P","Phosphorous","30.97376 u","Reactive Nonmetals"),
("S","Sulfur","32.06 u","Reactive Nonmetals"),
("Cl","Chlorine","35.453 u","Reactive Nonmetals")
