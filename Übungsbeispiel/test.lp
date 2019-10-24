
% variables
#const n1 = 5. %no of timeslots
#const n2 = 7. %no of days
#const n3 = 10. %no of workers
#const t1 = 3. %no of minimum shifts
#const t2 = 4. %no of maximum shifts

% instance

slot(1..n1).
day(1..n2).
worker(1..n3).

% encoding

% every shift only given to one worker
:- shift(X,Y,Z1),shift(X,Y,Z2),Z1!=Z2.

% noone works 2 shifts a day
:- shift(X1,Y,Z),shift(X2,Y,Z),X1!=X2.

%all shifts taken
:- {shift(1..n1,1..n2,1..n3)} < n1*n2.

%every worker has between t1 and t2 shifts a week
t1 <= {shift(X,Y,Z) : slot(X),day(Y) } <= t2 :- worker(Z).

#show shift/3.