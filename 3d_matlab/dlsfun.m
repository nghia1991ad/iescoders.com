function y = dlsfun(v,transp_flag)
global G epsilon;
temp = G*v;
y = epsilon * v + G'*temp;
return