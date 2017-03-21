% Louise Evans
function [currexp] = getplates(expt, exp_DB)
%select a subset of plates by expt name
%   Detailed explanation goes here
theseplates=ismember(exp_DB.Experiment_,expt);
exp_DB = exp_DB(:,1:22);
currexp=exp_DB(theseplates,:);
end

