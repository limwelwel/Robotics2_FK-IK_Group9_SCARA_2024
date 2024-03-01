disp('SCARA MANIPULATOR')

syms a1 a2 a3 a4 a5 d3

%% Link lengths

a1 = 4;
a2 = 3;
a3 = 4;
a4 = 3;
a5 = 3;

%% Joint Variables

d3 = 4;

%% D-H Parameters [theta,d,r,alpha,offset]

H0_1 = Link([0,a1,a2,0,0,0]);
H0_1.qlim = pi/180*[-90 90];
