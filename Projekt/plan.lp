<<<<<<< Updated upstream
% variables

#const roomNo = 10. 	%rooms
#const roomNoSmall = 5.	%small rooms
#const subjNo = 10.		%courses
#const classNo = 8. 	%classes
#const slotNo = 3.		%timeslots
#const small = 1.		%small room capacity (group)
#const medium = 2.		%medium room capacity (class)
#const lectorNo = 4.	%lectors
=======
#const roomNo = 15.
#const roomNoSmall = 10.
#const subjNo = 8.
#const classNo = 10.
#const slotNo = 4.
% variables

%#const roomNo = var. 		%rooms	10
%#const roomNoSmall = var.	%small rooms	5
%#const subjNo = var.		%courses	4
%#const classNo = var. 		%classes	4
%#const slotNo = var.		%timeslots	5
#const dayNo = 5.
#const small = 1.			%small room capacity (group)
#const medium = 2.			%medium room capacity (class)
#const lectorNo = 4.		%lectors
>>>>>>> Stashed changes

% instance

room(1..roomNo).
subject(1..subjNo).
class(1..classNo).
group(1..classNo,(a;b)).
slot(1..slotNo).
day(mo;di;mi;do;fr).
roomSize(1..roomNoSmall,small;roomNoSmall+1..roomNo,medium).

% not only 1 subj a day (optional), not more than 4

1  != {occupied(W,We,X,Y,Ye,Z): slot(W),room(X),subject(Z)} :- day(We),group(Y,Ye).
5  > {occupied(W,We,X,Y,Ye,Z): slot(W),room(X),subject(Z)} :- day(We),group(Y,Ye).

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

#show occupied/6.