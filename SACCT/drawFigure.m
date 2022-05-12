clear
%Get log CSV
step_log = readmatrix('step_log.csv');
gain_log = readmatrix('gain_log.csv');
energy_con_log = readmatrix('energy_con_log.csv');

%Get average Value

mean_energu_con_log = mean(reshape(energy_con_log,[201,(1000176 / 201)]));
mean_gain_log = mean(reshape(gain_log,[201,(1000176 / 201)]));
mean_step_log = mean(reshape(gain_log,[201,(1000176 / 201)]));


%Print figure
figure;
plot(step_log);
title('Reward pre step');

figure;
title('Gian pre Step');
plot(gain_log);

figure;
title('Energy_con_log pre Step');
plot(mean_energu_con_log);

%Function Define
% function averageValuePreBlock = average(DataSet)
% %   201 steps pre epsoid
%     NumberPerBlock = [201,(1000176 / 201)];
%     meanValue = mean(reshape(DataSet,NumberPerBlock));
%     averageValuePreBlock = meanValue;
% end