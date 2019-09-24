clear all; close all; clc;
load slab.mat;
idx1 = tmp(:,2) > 17.5;
idx2 = tmp(:,2) < 17.5;
% idx1 = inpoly([tmp(:,1) tmp(:,2)], [119 16.5; 121 19; 119 19]);
% idx2 = inpoly([tmp(:,1) tmp(:,2)], [119 16.5; 121 19; 121 14; 119 14]);
S_slab = tmp(idx1,:,:);
N_slab = tmp(idx2,:,:);
save('slab.mat');

slab = vertcat(N_slab, S_slab);
Lon = slab(:,1);
Lat = slab(:,2);
Dep = slab(:,3);
[xx1, yy1, zz1] = slabfit(N_slab,119,124,14,17);
[xx2, yy2, zz2] = slabfit(S_slab,119,124,17,20);
[xx3, yy3, zz3] = slabfit(slab,119,124,14,20);

% plot points and surface
figure('Renderer','opengl')
hold on;
fig = scatter3(Lon, Lat, Dep);
surface(xx1, yy1, zz1, ...
    'FaceColor','interp', 'EdgeColor','b', 'FaceAlpha',0.2);
surface(xx2, yy2, zz2, ...
    'FaceColor','interp', 'EdgeColor','b', 'FaceAlpha',0.2);
xlabel 'Lon'; ylabel 'Lat'; zlabel 'Dep';
xlim([119 124]);
ylim([14 19]);
zlim([-300 0]);
daspect([ 1 1 110]);

figure('Renderer','opengl')
hold on;
fig = scatter3(Lon, Lat, Dep);
surface(xx3, yy3, zz3, ...
    'FaceColor','interp', 'EdgeColor','b', 'FaceAlpha',0.2);
xlabel 'Lon'; ylabel 'Lat'; zlabel 'Dep';
xlim([119 124]);
ylim([14 19]);
zlim([-300 0]);
daspect([ 1 1 110]);