%Label Plate Map
% Louise Evans
function [template] = LabelPlateMap_LE()
rows = 'ABCDEFGHIJKLMNOP';
template = cell(17, 25);
for i = 2:17
    template (i, 1) = {rows(i-1)};
end
for i = 2:25
    template(1, i) = {num2str(i-1)};
end
end