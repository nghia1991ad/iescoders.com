clear, close all
figure(1) 
x = [1 14 14 12 12 6 6 1 1]; 
y = [1 1 7 7 5 5 7 7 1]; 
h = fill(x,y,'r','EdgeColor','none'); 
m = 130;
n = 130;
%Transform x and y to the range [1, m] and [1, n]
scalex = (1*m)/(max(x)-min(x));
scaley = (1*n)/(max(y)-min(y));
curr_center_x = ((max(x)-min(x))/2+min(x))*scalex;
curr_center_y = ((max(y)-min(y))/2+min(y))*scaley;
shiftx = curr_center_x-(m-1)/2;
shifty = curr_center_y-(n-1)/2;
BW = poly2mask(x*scalex-shiftx, y*scaley-shifty, m, n);
figure;
imshow(BW);
axis xy