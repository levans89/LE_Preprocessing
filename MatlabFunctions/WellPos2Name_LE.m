% Louise Evans July 2016

function [well] = WellPos2Name_LE(wellName)
well.r = strfind('ABCDEFGHIJKLMNOPQ', wellName(1));
well.c = str2num(wellName(2:3));
end