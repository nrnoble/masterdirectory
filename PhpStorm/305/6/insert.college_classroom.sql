USE nnoble_sakila;
TRUNCATE TABLE college_classroom;
INSERT INTO college_classroom (room_num, location, room_size, phone, occupancy)
VALUES ('101','Building-A','200','253-833-1101',40),
       ('102','Building-A','200','253-833-1102',40),
       ('103','Building-A','300','253-833-1103',50),
       ('201','Building-A','200','253-833-1201',40),
       ('202','Building-A','200','253-833-1102',40);