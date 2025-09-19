% Cargar datos desde archivo CSV
data = readtable('TPIMPEDANCIA.csv', Delimiter=';');  % Cambiá 'datos.csv' por el nombre de tu archivo

% Extraer columnas
lnR = data.lnR;
invT = data.invT_K;

% Crear matriz de diseño
X = [ones(size(lnR)), lnR, lnR.^3];

% Ajuste por mínimos cuadrados
coeffs = X \ invT;

% Mostrar coeficientes
A = coeffs(1);
B = coeffs(2);
C = coeffs(3);
fprintf('Coeficientes Steinhart-Hart:\nA = %.6e\nB = %.6e\nC = %.6e\n', A, B, C);

% Graficar datos y curva ajustada
lnR_fit = linspace(min(lnR), max(lnR), 500);
invT_fit = A + B * lnR_fit + C * lnR_fit.^3;
T_fit = 1 ./ invT_fit - 273.15;  % Convertir a °C

figure;
scatter(1 ./ invT - 273.15, exp(lnR), 'b', 'DisplayName', 'Datos originales');
hold on;
plot(T_fit, exp(lnR_fit), 'r', 'LineWidth', 2, 'DisplayName', 'Ajuste Steinhart-Hart');
xlabel('Temperatura (°C)');
ylabel('Resistencia (Ohm)');
title('Ajuste Steinhart-Hart');
legend;
grid on;
