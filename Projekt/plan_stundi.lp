#const roomNo = 10. 		%rooms	10
#const roomNoSmall = 5.	%small rooms	5
#const subjNo = 4.		%courses	4
#const classNo = 8. 		%classes	4
#const slotNo = 5.		%timeslots	5
#const dayNo = 5.
#const small = 1.			%small room capacity (group)
#const medium = 2.			%medium room capacity (class)
#const lectorNo = 4.		%lectors

% instance

room(1..roomNo).
subject(1..subjNo).
class(1..classNo).
group(1..classNo,(a;b)).
slot(1..slotNo).
day(mo;di;mi;do;fr).
roomSize(1..roomNoSmall,small;roomNoSmall+1..roomNo,medium).

% not only 1 subj a day

1 != {occupied(W,We,X,Y,Ye,Z): slot(W),room(X),subject(Z),group(Y,Ye)} :- day(We).

% no calculation, when slotNo*dayNo*(roomNoSmall+roomNoMedium*2) < subjects*classNo*2)

:- slotNo*dayNo*(roomNoSmall+(roomNo-roomNoSmall)*2) < subjNo*classNo*2.

% encoding occupied(slot,day,room,class,group,subject)

% each subject Z one time for every group (Y,Ye)

1 == {occupied(W,We,X,Y,Ye,Z) : slot(W),day(We),room(X)} :- subject(Z),group(Y,Ye).

% only one subject per room

:- occupied(W,We,X,Y1,Ye1,Z1),occupied(W,We,X,Y2,Ye2,Z2),Z1!=Z2.

% not more classes together

:- occupied(W,We,X,Y1,Ye1,Z1),occupied(W,We,X,Y2,Ye2,Z2),Y1!=Y2.

% no groups of one class together, if room is too small

:- occupied(W,We,X,Y,Ye1,Z),occupied(W,We,X,Y,Ye2,Z),Ye1!=Ye2,roomSize(X,small).

% each class has only one subject at the same time

:- occupied(W,We,X1,Y,Ye,Z1),occupied(W,We,X2,Y,Ye,Z2),Z1!=Z2.

#show occupied/6.