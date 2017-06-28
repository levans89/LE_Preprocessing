%Label Plate Map 96
% Louise Evans
function [template] = LabelPlateMap96_LE()
rows = 'ABCDEFGH';
template = cell(9, 13);
for i = 2:9
    template (i, 1) = {rows(i-1)};
end
for i = 2:13
    template(1, i) = {num2str(i-1)};
end
end